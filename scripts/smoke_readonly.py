#!/usr/bin/env python3
"""Read-only smoke test: proves the documented command surface really works.

Every case here is a *read* operation against a public repository, so the test
can run unattended and never mutates anything.  Results are written to
``verification/`` as JSON + Markdown so a reviewer can see evidence instead of
taking "it works" on faith.

Usage
-----
    python scripts/smoke_readonly.py
    python scripts/smoke_readonly.py --repo owner/repo --json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import time
from typing import Dict, List, Optional

DEFAULT_REPO = "atomgit-cli/cli"


def force_utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def cases(repo: str) -> List[Dict[str, object]]:
    r = repo
    return [
        {"id": "repo-view", "argv": ["repo", "view", r, "--json"], "json": True},
        {"id": "repo-list", "argv": ["repo", "list", "--limit", "2", "--json"], "json": True},
        {"id": "repo-log", "argv": ["repo", "log", "-R", r, "--limit", "2", "--json"], "json": True},
        {"id": "repo-branch-list", "argv": ["repo", "branch", "list", "-R", r, "--json"], "json": True},
        {"id": "repo-stats", "argv": ["repo", "stats", "-R", r, "--branch", "main", "--json"], "json": True},
        {"id": "repo-set-default-view", "argv": ["repo", "set-default", "--view", "--json"], "json": True},
        {"id": "issue-list", "argv": ["issue", "list", "-R", r, "--limit", "2", "--json"], "json": True},
        {"id": "pr-list", "argv": ["pr", "list", "-R", r, "--limit", "2", "--json"], "json": True},
        {"id": "release-list", "argv": ["release", "list", "-R", r, "--json"], "json": True},
        {"id": "label-list", "argv": ["label", "list", "-R", r, "--json"], "json": True},
        {"id": "milestone-list", "argv": ["milestone", "list", "-R", r, "--json"], "json": True},
        {"id": "search-repos", "argv": ["search", "repos", "gitcode-cli", "--json"], "json": True},
        {"id": "user-view", "argv": ["user", "view", "--json"], "json": True},
        {"id": "actions-run-list", "argv": ["actions", "run", "list", "-R", r, "--limit", "2", "--json"], "json": True},
        {"id": "actions-workflow-list", "argv": ["actions", "workflow", "list", "-R", r, "--json"], "json": True},
        {"id": "commit-comments-list", "argv": ["commit", "comments", "list", "-R", r, "--json"], "json": True},
        {"id": "auth-status", "argv": ["auth", "status", "--json"], "json": True},
        {"id": "version", "argv": ["version"], "json": False},
        {"id": "api-raw", "argv": ["api", f"repos/{r}"], "json": True},
        {"id": "api-jq", "argv": ["api", f"repos/{r}", "--jq", ".full_name"], "json": False},
    ]


def run_case(binary: str, case: Dict[str, object]) -> Dict[str, object]:
    argv = [binary, *case["argv"], "--no-update-check"]
    started = time.time()
    proc = subprocess.run(
        argv,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    elapsed = time.time() - started
    result: Dict[str, object] = {
        "id": case["id"],
        "command": " ".join(argv),
        "exit_code": proc.returncode,
        "duration_s": round(elapsed, 2),
        "stdout_bytes": len(proc.stdout.encode("utf-8")),
        "stderr": proc.stderr.strip()[:400],
        "json_ok": None,
    }
    if case.get("json"):
        try:
            json.loads(proc.stdout)
            result["json_ok"] = True
        except ValueError:
            result["json_ok"] = False
    result["ok"] = proc.returncode == 0 and result["json_ok"] is not False
    return result


def render_markdown(results: List[Dict[str, object]], repo: str, binary: str, version: str) -> str:
    passed = sum(1 for r in results if r["ok"])
    lines = [
        "# 只读命令 Smoke 结果",
        "",
        f"- 时间: {dt.datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"- CLI: `{binary}` {version}",
        f"- 仓库: `{repo}`",
        f"- 结果: **{passed}/{len(results)}** 通过",
        "",
        "| 用例 | 命令 | 退出码 | JSON | 耗时(s) | 结果 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in results:
        json_mark = "—" if row["json_ok"] is None else ("✓" if row["json_ok"] else "✗")
        lines.append(
            f"| {row['id']} | `{row['command']}` | {row['exit_code']} | {json_mark} | "
            f"{row['duration_s']} | {'✅' if row['ok'] else '❌'} |"
        )
    failures = [r for r in results if not r["ok"]]
    if failures:
        lines.extend(["", "## 失败详情", ""])
        for row in failures:
            lines.append(f"### {row['id']}")
            lines.append("")
            lines.append(f"```\n{row['command']}\nexit={row['exit_code']}\n{row['stderr']}\n```")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="read-only smoke test for the gitcode CLI surface")
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--binary", default="gitcode")
    parser.add_argument("--json", action="store_true", help="print JSON instead of markdown")
    args = parser.parse_args(argv)

    force_utf8_stdio()

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "verification")
    os.makedirs(out_dir, exist_ok=True)

    version = ""
    ver = subprocess.run(
        [args.binary, "version"], capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    for line in (ver.stdout or "").splitlines():
        if line.startswith("gitcode version"):
            version = line.split()[-1]
            break

    results = [run_case(args.binary, case) for case in cases(args.repo)]
    stamp = dt.datetime.now().strftime("%Y%m%d")
    payload = {
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "binary": args.binary,
        "version": version,
        "repo": args.repo,
        "passed": sum(1 for r in results if r["ok"]),
        "total": len(results),
        "results": results,
    }
    json_path = os.path.join(out_dir, f"smoke-{stamp}.json")
    md_path = os.path.join(out_dir, f"smoke-{stamp}.md")
    with open(json_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
    markdown = render_markdown(results, args.repo, args.binary, version)
    with open(md_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(markdown)

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(markdown)
        print(f"written: {json_path}")
        print(f"written: {md_path}")

    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
