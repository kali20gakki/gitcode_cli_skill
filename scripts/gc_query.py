#!/usr/bin/env python3
"""Look up the *installed* gitcode CLI's command metadata.

Why this exists: the bundled `references/` are a snapshot generated from one
CLI version.  When the binary on the user's machine is newer (or older) than
that snapshot, the authoritative answer to "which flags does this command
actually accept" is ``gitcode schema`` itself.  This script turns that JSON
into something small enough to read, without dumping 300 KB into the context.

Usage
-----
    python scripts/gc_query.py "pr list"
    python scripts/gc_query.py "pr review" --json
    python scripts/gc_query.py --list --prefix pr
    python scripts/gc_query.py --search artifact
    python scripts/gc_query.py --capabilities
    python scripts/gc_query.py --check --expect 0.17.0     # 版本/漂移自检

Environment
-----------
GC_SCHEMA_JSON   use a saved schema file instead of invoking the CLI (tests/CI).
GITCODE_BIN      override the executable name (default: gitcode, fallback: gc).
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import subprocess
import sys
from typing import Dict, List, Optional

CAPABILITIES = [
    ("json", "--json"),
    ("repo", "-R"),
    ("yes", "--yes"),
    ("dry-run", "--dry-run"),
    ("paginate", "--paginate"),
    ("template", "--template"),
]

GLOBAL_FLAGS = {"no-interactive", "no-update-check", "help"}


def force_utf8_stdio() -> None:
    """Windows consoles default to the locale code page; agents expect UTF-8."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


# --------------------------------------------------------------------------- #
# schema access
# --------------------------------------------------------------------------- #
def binary() -> str:
    if os.environ.get("GITCODE_BIN"):
        return os.environ["GITCODE_BIN"]
    for candidate in ("gitcode", "gc"):
        from shutil import which

        if which(candidate):
            return candidate
    return "gitcode"


def load_schema(use_cli: bool = True) -> dict:
    path = os.environ.get("GC_SCHEMA_JSON")
    if path:
        with open(path, "r", encoding="utf-8-sig") as fh:
            return json.load(fh)
    if not use_cli:
        raise RuntimeError("no schema source: set GC_SCHEMA_JSON")
    proc = subprocess.run(
        [binary(), "schema"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0:
        raise RuntimeError(f"`{binary()} schema` failed (exit {proc.returncode}): {proc.stderr.strip()}")
    return json.loads(proc.stdout)


def walk(node: dict) -> List[dict]:
    out = [node] if node.get("path") else []
    for child in node.get("subcommands") or []:
        out.extend(walk(child))
    return out


def normalize(path: str) -> str:
    tokens = [t for t in path.replace("`", "").split() if t]
    if tokens and tokens[0] == "gitcode":
        tokens = tokens[1:]
    return " ".join(tokens).lower()


def find_node(schema: dict, path: str) -> Optional[dict]:
    wanted = normalize(path)
    if not wanted:
        return schema
    for node in walk(schema):
        if normalize(node["path"]) == wanted:
            return node
    return None


# --------------------------------------------------------------------------- #
# rendering
# --------------------------------------------------------------------------- #
def flag_line(flag: dict) -> str:
    name = f"--{flag.get('name', '')}"
    short = flag.get("shorthand")
    head = f"{name}, -{short}" if short else name
    kind = flag.get("type", "")
    usage = flag.get("usage", "")
    extra = []
    if flag.get("enum"):
        extra.append("可选: " + ", ".join(flag["enum"]))
    if flag.get("default") not in (None, "", "false", "0", "[]"):
        extra.append(f"默认: {flag['default']}")
    if flag.get("required"):
        extra.append("必填")
    tail = f"（{'；'.join(extra)}）" if extra else ""
    return f"  {head:<26} {kind:<7} {usage}{tail}"


def render(node: dict) -> str:
    lines = [node.get("path", "gitcode"), node.get("short", ""), ""]

    use = (node.get("use") or "").strip()
    rest = " ".join(use.split()[1:]) if use else ""
    usage = f"{node.get('path', 'gitcode')} {rest}".strip()
    lines.append(f"用法: {usage}")

    args = node.get("arguments") or []
    if args:
        rendered = [
            f"{a.get('name')}{'（必填）' if a.get('required') else ''}" for a in args
        ]
        lines.append("参数: " + ", ".join(rendered))

    if node.get("aliases"):
        lines.append("别名: " + ", ".join(node["aliases"]))

    children = node.get("subcommands") or []
    if children:
        lines.append("")
        lines.append("子命令:")
        for child in children:
            if child.get("hidden"):
                continue
            lines.append(f"  {child['path'].split()[-1]:<16} {child.get('short', '')}")

    flags = [f for f in (node.get("flags") or []) if f.get("name") not in GLOBAL_FLAGS]
    if flags:
        lines.append("")
        lines.append("Flags:")
        for flag in flags:
            lines.append(flag_line(flag))

    lines.append("")
    lines.append("全局: --no-interactive  --no-update-check  --help")

    example = (node.get("example") or "").strip()
    if example:
        lines.append("")
        lines.append("示例:")
        for line in example.splitlines():
            line = line.strip()
            if line.startswith("$ "):
                lines.append("  " + line[2:])
            elif line.startswith("#"):
                lines.append("  " + line)
    return "\n".join(lines) + "\n"


def list_commands(schema: dict, prefix: Optional[str], as_json: bool) -> str:
    nodes = [n for n in walk(schema) if len(n["path"].split()) > 1]
    if prefix:
        wanted = normalize(prefix)
        nodes = [n for n in nodes if normalize(n["path"]).startswith(wanted)]
    nodes.sort(key=lambda n: n["path"])
    if as_json:
        return json.dumps([{"path": n["path"], "short": n.get("short", "")} for n in nodes], ensure_ascii=False, indent=2)
    width = max((len(n["path"]) for n in nodes), default=10)
    return "\n".join(f"{n['path']:<{width}}  {n.get('short', '')}" for n in nodes) + "\n"


def search(schema: dict, keyword: str, as_json: bool) -> str:
    needle = keyword.lower()
    hits = []
    for node in walk(schema):
        haystack = " ".join(
            str(x) for x in (node.get("path"), node.get("short"), node.get("use"), node.get("long")) if x
        ).lower()
        for flag in node.get("flags") or []:
            haystack += " --" + str(flag.get("name", "")).lower() + " " + str(flag.get("usage", "")).lower()
        if needle in haystack:
            hits.append(node)
    hits.sort(key=lambda n: n["path"])
    if as_json:
        return json.dumps(
            [{"path": n["path"], "short": n.get("short", "")} for n in hits], ensure_ascii=False, indent=2
        )
    if not hits:
        return f"no command matched {keyword!r}\n"
    width = max(len(n["path"]) for n in hits)
    return "\n".join(f"{n['path']:<{width}}  {n.get('short', '')}" for n in hits) + "\n"


def capabilities(schema: dict, as_json: bool) -> str:
    leaves = [n for n in walk(schema) if len(n["path"].split()) > 1 and not (n.get("subcommands") or [])]
    leaves.sort(key=lambda n: n["path"])
    rows = []
    for node in leaves:
        names = {f.get("name") for f in node.get("flags") or []}
        rows.append(
            {
                "path": node["path"],
                **{key: key in names for key, _ in CAPABILITIES},
            }
        )
    if as_json:
        return json.dumps(rows, ensure_ascii=False, indent=2)
    header = "| 命令 | " + " | ".join(label for _, label in CAPABILITIES) + " |"
    out = [header, "| --- | " + " | ".join("---" for _ in CAPABILITIES) + " |"]
    for row in rows:
        out.append(f"| `{row['path']}` | " + " | ".join("✓" if row[key] else "" for key, _ in CAPABILITIES) + " |")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def check_version(expected: Optional[str], as_json: bool) -> int:
    meta_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references", ".schema-meta.json")
    bundled = {}
    try:
        with open(meta_path, "r", encoding="utf-8") as fh:
            bundled = json.load(fh)
    except OSError:
        pass

    installed = "unknown"
    try:
        out = subprocess.run(
            [binary(), "version"], capture_output=True, text=True, encoding="utf-8", errors="replace"
        ).stdout
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[0] == "gitcode" and parts[1] == "version":
                installed = parts[2]
                break
    except OSError:
        pass

    result = {
        "installed_version": installed,
        "bundled_version": bundled.get("cli_version"),
        "expected_version": expected,
        "ok": True,
        "notes": [],
    }
    if expected and installed != expected:
        result["ok"] = False
        result["notes"].append(f"installed {installed} != expected {expected}")
    if bundled.get("cli_version") and installed not in ("unknown", bundled["cli_version"]):
        result["ok"] = False
        result["notes"].append(
            f"installed {installed} differs from bundled docs {bundled['cli_version']}; "
            "run `python scripts/gen_references.py` after upgrading"
        )
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"installed: {installed}")
        print(f"bundled:   {bundled.get('cli_version')}")
        for note in result["notes"]:
            print(f"! {note}")
        print("ok" if result["ok"] else "drift")
    return 0 if result["ok"] else 1


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Query the installed gitcode CLI schema",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("path", nargs="?", help="命令路径，例如 \"pr list\"")
    parser.add_argument("--list", action="store_true", help="列出全部命令")
    parser.add_argument("--prefix", help="配合 --list 按前缀过滤")
    parser.add_argument("--search", help="按关键字搜索命令/flag")
    parser.add_argument("--capabilities", action="store_true", help="打印能力矩阵")
    parser.add_argument("--check", action="store_true", help="检查已安装版本与随包文档是否一致")
    parser.add_argument("--expect", help="配合 --check：期望版本")
    parser.add_argument("--json", action="store_true", help="输出原始 schema JSON / JSON 结构")
    args = parser.parse_args(argv)

    force_utf8_stdio()

    if args.check:
        return check_version(args.expect, args.json)

    try:
        schema = load_schema()
    except (RuntimeError, OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.list:
        sys.stdout.write(list_commands(schema, args.prefix, args.json))
        return 0
    if args.search:
        sys.stdout.write(search(schema, args.search, args.json))
        return 0
    if args.capabilities:
        sys.stdout.write(capabilities(schema, args.json))
        return 0
    if not args.path:
        parser.print_help()
        return 2

    node = find_node(schema, args.path)
    if node is None:
        candidates = [n["path"] for n in walk(schema) if len(n["path"].split()) > 1]
        close = difflib.get_close_matches("gitcode " + normalize(args.path), candidates, n=5, cutoff=0.5)
        print(f"error: unknown command path: {args.path}", file=sys.stderr)
        if close:
            print("did you mean:", file=sys.stderr)
            for c in close:
                print("  " + c, file=sys.stderr)
        else:
            print("run `python scripts/gc_query.py --list` to see all commands", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(node, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(render(node))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
