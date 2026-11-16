#!/usr/bin/env python3
"""Pre-flight check before an agent starts driving the gitcode CLI.

Answers the four questions that decide whether a gitcode task can proceed at
all, and the one that decides whether the bundled references are trustworthy:

1. Is the CLI installed, and which version / channel is it?
2. Is this machine authenticated?  (never prints or stores a token)
3. Which repository would a command without ``-R`` act on?
4. Do the bundled references match the installed CLI?

Exit code: 0 = healthy, 1 = a blocker (missing CLI or missing auth).

Usage
-----
    python scripts/gc_preflight.py
    python scripts/gc_preflight.py --json
    python scripts/gc_preflight.py --check-updates
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from typing import Dict, List, Optional

GENERATOR_REL = os.path.join("references", ".schema-meta.json")


def force_utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def run(cmd: List[str], timeout: int = 40) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return subprocess.CompletedProcess(cmd, 127, "", str(exc))


def parse_version(text: str) -> Optional[str]:
    for line in text.splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[0] == "gitcode" and parts[1] == "version":
            return parts[2]
    return None


def repo_from_remote(url: str) -> Optional[str]:
    url = url.strip()
    if not url:
        return None
    match = re.search(r"[/:]([^/:]+)/([^/]+?)(?:\.git)?/?$", url)
    if not match:
        return None
    return f"{match.group(1)}/{match.group(2)}"


def find_git_root(start: str) -> Optional[str]:
    current = os.path.abspath(start)
    while True:
        if os.path.exists(os.path.join(current, ".git")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            return None
        current = parent


def bundled_meta(skill_root: str) -> Dict[str, object]:
    try:
        with open(os.path.join(skill_root, GENERATOR_REL), "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #
def collect(check_updates: bool) -> Dict[str, object]:
    skill_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = shutil.which("gitcode") or shutil.which("gc")
    binary = "gitcode" if shutil.which("gitcode") else (path or "gitcode")

    info: Dict[str, object] = {
        "cli_path": path,
        "binary": binary,
        "version": None,
        "channel": None,
        "conflicts": [],
        "auth_ok": None,
        "username": None,
        "token_source": None,
        "default_repo": None,
        "cwd_repo": None,
        "git_root": find_git_root(os.getcwd()),
        "bundled_version": bundled_meta(skill_root).get("cli_version"),
        "schema_drift": None,
        "update": None,
        "blockers": [],
        "warnings": [],
    }

    if not path:
        info["blockers"].append("gitcode CLI not found on PATH")
        return info

    version_proc = run([binary, "version"])
    info["version"] = parse_version(version_proc.stdout or "")

    doctor = run([binary, "doctor", "install", "--json"])
    try:
        doctor_json = json.loads(doctor.stdout)
        info["channel"] = doctor_json.get("distribution")
        info["conflicts"] = doctor_json.get("conflicts") or []
    except ValueError:
        info["warnings"].append("`gitcode doctor install --json` did not return JSON")

    auth = run([binary, "auth", "status", "--json"])
    try:
        auth_json = json.loads(auth.stdout)
        info["auth_ok"] = bool(auth_json.get("logged_in"))
        info["username"] = auth_json.get("username")
        info["token_source"] = auth_json.get("token_source")
    except ValueError:
        info["auth_ok"] = auth.returncode == 0
    if not info["auth_ok"]:
        info["blockers"].append(
            f"not authenticated: run `{binary} auth login` yourself in an interactive terminal"
        )

    default = run([binary, "repo", "set-default", "--view", "--json"])
    try:
        info["default_repo"] = json.loads(default.stdout).get("default_repo") or None
    except ValueError:
        pass

    root = info["git_root"]
    if root:
        origin = run(["git", "-C", root, "config", "--get", "remote.origin.url"])
        info["cwd_repo"] = repo_from_remote(origin.stdout or "")

    if info["version"] and info["bundled_version"] and info["version"] != info["bundled_version"]:
        info["schema_drift"] = True
        info["warnings"].append(
            f"installed {info['version']} != bundled references {info['bundled_version']}; "
            "run `python scripts/gen_references.py` after upgrading, "
            "or trust `gitcode schema` at runtime"
        )
    elif info["version"] and info["bundled_version"]:
        info["schema_drift"] = False

    if check_updates:
        upd = run([binary, "update", "--check", "--json"])
        try:
            info["update"] = json.loads(upd.stdout)
        except ValueError:
            info["update"] = {"raw": (upd.stdout or upd.stderr).strip()}

    if not (info["default_repo"] or info["cwd_repo"]):
        info["warnings"].append(
            "no default repository and not inside a git repo: pass `-R owner/repo` explicitly"
        )
    return info


def render(info: Dict[str, object]) -> str:
    def line(label: str, value: object) -> str:
        return f"{label:<14} {value if value not in (None, '') else '—'}"

    lines = [
        line("cli_path", info["cli_path"]),
        line("version", f"{info['version']} (channel: {info['channel']})"),
        line("auth", f"{'ok' if info['auth_ok'] else 'MISSING'}" + (f" as {info['username']}" if info.get("username") else "")),
        line("default_repo", info["default_repo"]),
        line("cwd_repo", f"{info['cwd_repo']} ({info['git_root']})" if info.get("cwd_repo") else None),
        line("bundled_docs", info["bundled_version"]),
        line("schema_drift", "yes" if info["schema_drift"] else "no"),
    ]
    if info.get("update"):
        lines.append(line("update", json.dumps(info["update"], ensure_ascii=False)))
    for conflict in info.get("conflicts") or []:
        lines.append(line("conflict", conflict))
    for warning in info.get("warnings") or []:
        lines.append(f"! {warning}")
    for blocker in info.get("blockers") or []:
        lines.append(f"x {blocker}")
    lines.append("healthy" if not info.get("blockers") else "blocked")
    return "\n".join(lines) + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="gitcode CLI pre-flight for agents")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--check-updates", action="store_true", help="also query the update channel")
    args = parser.parse_args(argv)

    force_utf8_stdio()

    info = collect(args.check_updates)
    if args.json:
        print(json.dumps(info, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(render(info))
    return 0 if not info["blockers"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
