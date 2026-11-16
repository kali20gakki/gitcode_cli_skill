#!/usr/bin/env python3
"""Generate the reference docs bundled with the gitcode-cli skill.

The single source of truth is the installed CLI itself:

    gitcode schema            # machine-readable command tree (JSON)

Everything under ``references/`` is derived from that tree, so the docs can
never drift far from the binary an agent will actually call.

Usage
-----
    python scripts/gen_references.py                     # regenerate in place
    python scripts/gen_references.py --check             # diff only, exit 1 on drift
    python scripts/gen_references.py --schema-json FILE  # offline / tests
    python scripts/gen_references.py --out DIR           # write somewhere else

Design notes
------------
* Deterministic output: commands are sorted by path, no timestamps, no
  absolute paths.  Generating twice from the same schema yields identical
  bytes, which is what makes ``--check`` useful in CI.
* One file per command family keeps each reference small enough to read on
  demand (progressive disclosure) instead of dumping a 300 KB schema.
* Any top-level command that is not mapped below is a bug, not a silent
  omission: it lands in ``commands/ops.md`` and ``--check``/tests complain.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import subprocess
import sys
from typing import Dict, Iterable, List, Optional, Tuple

GENERATOR_VERSION = "1.0.0"

# Top-level command -> reference file.  Keeping several related families in one
# file avoids a dozen tiny files while still separating the big workflows.
FAMILIES: Dict[str, Tuple[str, str]] = {
    "pr": ("commands/pr.md", "pr — Pull Request 命令"),
    "issue": ("commands/issue.md", "issue / label / milestone — 议题与元数据命令"),
    "label": ("commands/issue.md", "issue / label / milestone — 议题与元数据命令"),
    "milestone": ("commands/issue.md", "issue / label / milestone — 议题与元数据命令"),
    "repo": ("commands/repo.md", "repo — 仓库、分支与保护规则命令"),
    "release": ("commands/release-commit.md", "release / commit — 发布与提交命令"),
    "commit": ("commands/release-commit.md", "release / commit — 发布与提交命令"),
    "actions": ("commands/actions.md", "actions — 流水线、Job、Artifact 与 Runner 命令"),
    "search": ("commands/search-user.md", "search / user / discussions — 发现与协作命令"),
    "user": ("commands/search-user.md", "search / user / discussions — 发现与协作命令"),
    "discussions": ("commands/search-user.md", "search / user / discussions — 发现与协作命令"),
    "api": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "auth": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "config": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "doctor": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "update": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "schema": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "version": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "browse": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "precommit": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "lark": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
    "ssh-key": ("commands/ops.md", "api / auth / config / doctor 等通用命令"),
}

# Flags that every command inherits; documenting them per command is noise.
GLOBAL_FLAGS = {"no-interactive", "no-update-check", "help"}

TITLES: Dict[str, str] = {rel: title for rel, title in FAMILIES.values()}

FILE_ORDER = [
    "commands/pr.md",
    "commands/issue.md",
    "commands/repo.md",
    "commands/release-commit.md",
    "commands/actions.md",
    "commands/search-user.md",
    "commands/ops.md",
]


# --------------------------------------------------------------------------- #
# schema loading
# --------------------------------------------------------------------------- #
def load_schema(args: argparse.Namespace) -> Tuple[dict, str, str]:
    """Return (schema, cli_version, schema_sha256)."""
    if args.schema_json:
        with open(args.schema_json, "r", encoding="utf-8-sig") as fh:
            schema = json.load(fh)
        version = _version_from_meta(args.out) or "unknown"
    else:
        proc = subprocess.run(
            [args.gitcode, "schema"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if proc.returncode != 0:
            sys.exit(f"error: `{args.gitcode} schema` failed: {proc.stderr.strip()}")
        schema = json.loads(proc.stdout)
        version = _cli_version(args.gitcode)

    canonical = json.dumps(schema, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return schema, version, digest


def _cli_version(binary: str) -> str:
    try:
        out = subprocess.run(
            [binary, "version"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        ).stdout
    except OSError:
        return "unknown"
    for line in out.splitlines():
        parts = line.strip().split()
        if len(parts) >= 3 and parts[0] == "gitcode" and parts[1] == "version":
            return parts[2]
    return "unknown"


def _version_from_meta(out_dir: str) -> Optional[str]:
    path = os.path.join(out_dir, "references", ".schema-meta.json")
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh).get("cli_version")
    except (OSError, ValueError):
        return None


# --------------------------------------------------------------------------- #
# tree walking
# --------------------------------------------------------------------------- #
def top_level_of(path: str) -> str:
    parts = path.split()
    return parts[1] if len(parts) > 1 else ""


def walk(node: dict) -> Iterable[dict]:
    """Depth-first over every node that has a path (root included)."""
    if node.get("path"):
        yield node
    for child in node.get("subcommands") or []:
        yield from walk(child)


def family_file(path: str) -> str:
    top = top_level_of(path)
    if top in FAMILIES:
        return FAMILIES[top][0]
    return "commands/ops.md"


def family_title(path: str) -> str:
    return TITLES[family_file(path)]


def is_leaf(node: dict) -> bool:
    return not (node.get("subcommands") or [])


# --------------------------------------------------------------------------- #
# rendering helpers
# --------------------------------------------------------------------------- #
def cell(text: object) -> str:
    """Make a value safe for a single markdown table cell."""
    s = "" if text is None else str(text)
    s = s.replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    s = " ".join(s.split())
    return s or "—"


def code_span(text: str) -> str:
    return f"`{text}`" if text else "—"


def usage_line(node: dict) -> str:
    path = node["path"]
    use = (node.get("use") or "").strip()
    rest = " ".join(use.split()[1:]) if use else ""
    return f"{path} {rest}".strip()


def flag_rows(node: dict) -> List[str]:
    rows: List[str] = []
    for flag in node.get("flags") or []:
        name = flag.get("name", "")
        if name in GLOBAL_FLAGS:
            continue
        desc = flag.get("usage", "")
        enum = flag.get("enum")
        if enum:
            desc = f"{desc}（可选: {', '.join(enum)}）"
        if flag.get("required"):
            desc = f"**必填** {desc}"
        rows.append(
            "| {flag} | {short} | {type} | {default} | {desc} |".format(
                flag=code_span(f"--{name}"),
                short=code_span(flag.get("shorthand", "")),
                type=cell(flag.get("type", "")),
                default=cell(flag.get("default", "")),
                desc=cell(desc),
            )
        )
    return rows


def example_commands(example: str) -> List[str]:
    """Split a schema ``example`` blob into commands, keeping continuations.

    Cobra examples mix comments (``# ...``) and shell commands (``$ ...``) and
    long commands wrap onto following lines without a prompt.  Keeping the
    continuation lines matters: ``pr sync`` is only usable when its
    ``--target-repo`` line is not dropped.
    """
    commands: List[str] = []
    current: List[str] = []
    for raw in example.splitlines():
        text = raw.strip()
        if not text or text.startswith("#"):
            continue
        if text.startswith("$ "):
            if current:
                commands.append("\n".join(current))
            current = [text[2:].strip()]
        elif current:
            current.append(text)
    if current:
        commands.append("\n".join(current))
    return commands


def example_block(node: dict, limit: int = 3) -> List[str]:
    commands = example_commands(node.get("example") or "")
    if not commands:
        return []
    return ["**示例**", "", "```bash", "\n".join(commands[:limit]), "```"]


def leaf_block(node: dict) -> List[str]:
    out = [f"### `{node['path']}`", ""]
    out.append(node.get("short", "").strip() or "—")
    out.append("")
    out.append(f"`用法: {usage_line(node)}`")
    out.append("")

    args = node.get("arguments") or []
    # Cobra sometimes folds flag names into `use`; those are already in the
    # flag table, so keep only real positional arguments here.
    args = [a for a in args if not str(a.get("name", "")).startswith("-")]
    if args:
        rendered = []
        for arg in args:
            name = arg.get("name", "")
            rendered.append(f"{code_span(name)}（必填）" if arg.get("required") else code_span(name))
        out.append(f"参数: {', '.join(rendered)}")
        out.append("")

    rows = flag_rows(node)
    if rows:
        out.append("| Flag | 简写 | 类型 | 默认 | 说明 |")
        out.append("| --- | --- | --- | --- | --- |")
        out.extend(rows)
        out.append("")

    examples = example_block(node)
    if examples:
        out.extend(examples)
        out.append("")
    return out


def group_block(node: dict) -> List[str]:
    children = [c for c in node.get("subcommands") or [] if not c.get("hidden")]
    out = [f"### `{node['path']}`", ""]
    out.append(node.get("short", "").strip() or "—")
    out.append("")
    out.append("子命令: " + ", ".join(f"`{c['name']}`" for c in children))
    out.append("")
    return out


def family_doc(title: str, nodes: List[dict], version: str) -> str:
    groups = [n for n in nodes if not is_leaf(n)]
    leaves = [n for n in nodes if is_leaf(n)]
    out = [
        f"# {title}",
        "",
        f"> 自动生成：`scripts/gen_references.py` ← `gitcode schema`（CLI {version}）。"
        "请勿手工编辑；需要现场真值时用 `python scripts/gc_query.py \"<命令路径>\"`。",
        "",
        "## 命令清单",
        "",
        "| 命令 | 摘要 | JSON |",
        "| --- | --- | --- |",
    ]
    for node in sorted(leaves, key=lambda n: n["path"]):
        has_json = any(f.get("name") == "json" for f in node.get("flags") or [])
        out.append(f"| `{node['path']}` | {cell(node.get('short'))} | {'✓' if has_json else '—'} |")
    out.append("")

    if groups:
        out.extend(["## 命令组", ""])
        for node in sorted(groups, key=lambda n: n["path"]):
            out.extend(group_block(node))

    if leaves:
        out.extend(["## 详细参数", ""])
        for node in sorted(leaves, key=lambda n: n["path"]):
            out.extend(leaf_block(node))
    return "\n".join(out).rstrip() + "\n"


def index_doc(nodes: List[dict], version: str) -> str:
    leaves = sorted((n for n in nodes if is_leaf(n)), key=lambda n: n["path"])
    by_top: Dict[str, List[dict]] = {}
    for node in leaves:
        by_top.setdefault(top_level_of(node["path"]), []).append(node)

    out = [
        "# 命令总索引",
        "",
        f"> 自动生成（CLI {version}），共 **{len(leaves)}** 个叶命令 + 命令组。",
        "> `completion` / `help` 为 cobra 内建命令，不出现在 `gitcode schema` 中，用法见 `global-contract.md`。",
        ">",
        "> 需要完整参数：读对应 `commands/<家族>.md`；需要现场真值：`python scripts/gc_query.py \"<命令路径>\"`。",
        "",
        "| 家族 | 参考文件 |",
        "| --- | --- |",
    ]
    for top in sorted(by_top):
        out.append(f"| `{top}` | `{family_file(top)}` |")
    out.append("")

    for top in sorted(by_top):
        out.extend([f"## {top}", "", "| 命令 | 摘要 | JSON |", "| --- | --- | --- |"])
        for node in by_top[top]:
            has_json = any(f.get("name") == "json" for f in node.get("flags") or [])
            out.append(f"| `{node['path']}` | {cell(node.get('short'))} | {'✓' if has_json else '—'} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


CAP_COLUMNS = [
    ("json", "--json"),
    ("repo", "-R"),
    ("yes", "--yes"),
    ("dry-run", "--dry-run"),
    ("paginate", "--paginate"),
    ("template", "--template"),
]


def capabilities_doc(nodes: List[dict], version: str) -> str:
    leaves = sorted((n for n in nodes if is_leaf(n)), key=lambda n: n["path"])
    out = [
        "# 能力矩阵",
        "",
        f"> 自动生成（CLI {version}）。✓ = 该命令支持此 flag；空白 = 不支持。",
        "> 用途：先看这里判断能否 `--json` 解析、能否 `--dry-run` 预演、是否需要 `--yes`，再决定读哪个家族文档。",
        "",
        "| 命令 | " + " | ".join(label for _, label in CAP_COLUMNS) + " |",
        "| --- | " + " | ".join("---" for _ in CAP_COLUMNS) + " |",
    ]
    for node in leaves:
        names = {f.get("name") for f in node.get("flags") or []}
        cells = ["✓" if key in names else "" for key, _ in CAP_COLUMNS]
        out.append(f"| `{node['path']}` | " + " | ".join(cells) + " |")
    out.append("")
    out.extend(
        [
            "## 统计",
            "",
            "| 能力 | 命令数 |",
            "| --- | --- |",
        ]
    )
    for key, label in CAP_COLUMNS:
        count = sum(1 for n in leaves if key in {f.get("name") for f in n.get("flags") or []})
        out.append(f"| {label} | {count} / {len(leaves)} |")
    out.append("")
    return "\n".join(out).rstrip() + "\n"


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def build(schema: dict, version: str, digest: str) -> Dict[str, str]:
    # The root node only carries the global flags; every global rule lives in
    # global-contract.md instead of being repeated per family.
    nodes = [n for n in walk(schema) if len(n["path"].split()) > 1]
    leaves = [n for n in nodes if is_leaf(n)]

    unmapped = sorted({top_level_of(n["path"]) for n in leaves} - set(FAMILIES))
    if unmapped:
        print(
            "warning: unmapped top-level command(s) fell back to commands/ops.md: "
            + ", ".join(unmapped),
            file=sys.stderr,
        )

    files: Dict[str, str] = {}
    for rel in FILE_ORDER:
        members = [n for n in nodes if family_file(n["path"]) == rel]
        files[f"references/{rel}"] = family_doc(TITLES[rel], members, version)

    files["references/command-index.md"] = index_doc(nodes, version)
    files["references/capabilities.md"] = capabilities_doc(nodes, version)
    files["references/.schema-meta.json"] = (
        json.dumps(
            {
                "cli_version": version,
                "schema_sha256": digest,
                "generator_version": GENERATOR_VERSION,
                "leaf_commands": len(leaves),
                "files": sorted(files) + ["references/.schema-meta.json"],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    return files


def write_files(root: str, files: Dict[str, str], check: bool) -> int:
    drift = []
    for rel, content in sorted(files.items()):
        target = os.path.join(root, rel)
        if check:
            try:
                with open(target, "r", encoding="utf-8") as fh:
                    current = fh.read()
            except OSError:
                current = None
            if current != content:
                drift.append(rel)
                if current is not None:
                    diff = list(
                        difflib.unified_diff(
                            current.splitlines()[:40],
                            content.splitlines()[:40],
                            fromfile=f"{rel} (on disk)",
                            tofile=f"{rel} (generated)",
                            lineterm="",
                        )
                    )
                    print("\n".join(diff[:20]))
            continue

        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        print(f"wrote {rel} ({len(content)} bytes)")

    if check:
        if drift:
            print("drift detected in: " + ", ".join(drift), file=sys.stderr)
            print("run `python scripts/gen_references.py` to regenerate", file=sys.stderr)
            return 1
        print(f"references are up to date ({len(files)} files)")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    default_out = os.path.dirname(here)

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--gitcode", default="gitcode", help="gitcode 可执行文件（默认 PATH 中的 gitcode）")
    parser.add_argument("--schema-json", help="使用已保存的 schema JSON，而不是调用 CLI")
    parser.add_argument("--out", default=default_out, help="skill 根目录（默认脚本上一级）")
    parser.add_argument("--check", action="store_true", help="只比对，不写入；有差异退出码 1")
    args = parser.parse_args(argv)

    schema, version, digest = load_schema(args)
    files = build(schema, version, digest)
    return write_files(os.path.abspath(args.out), files, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
