"""Consistency test between the generated index and the *installed* CLI.

Skipped automatically when gitcode is not on PATH, so the suite stays green on
machines that only lint the docs.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "references", "command-index.md")
META = os.path.join(ROOT, "references", ".schema-meta.json")


def installed_commands(binary: str) -> list:
    proc = subprocess.run(
        [binary, "schema"], capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if proc.returncode != 0:
        raise unittest.SkipTest(f"`{binary} schema` failed: {proc.stderr[:200]}")
    schema = json.loads(proc.stdout)

    out = []

    def walk(node):
        if node.get("path") and len(node["path"].split()) > 1 and not node.get("subcommands"):
            out.append(node["path"])
        for child in node.get("subcommands") or []:
            walk(child)

    walk(schema)
    return sorted(out)


@unittest.skipUnless(shutil.which("gitcode") or shutil.which("gc"), "gitcode CLI not installed")
class LiveCoverageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.binary = shutil.which("gitcode") or shutil.which("gc")

    def test_documented_commands_match_installed_cli(self) -> None:
        with open(INDEX, "r", encoding="utf-8") as fh:
            documented = set(re.findall(r"^\| `(gitcode [^`]+)` \|", fh.read(), re.MULTILINE))
        installed = set(installed_commands(self.binary))
        self.assertEqual(
            installed - documented,
            set(),
            "installed CLI has commands missing from references; run gen_references.py",
        )

    def test_meta_version_matches_installed_version(self) -> None:
        proc = subprocess.run(
            [self.binary, "version"], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        m = re.search(r"^gitcode version (\S+)", proc.stdout, re.MULTILINE)
        self.assertIsNotNone(m)
        with open(META, "r", encoding="utf-8") as fh:
            meta = json.load(fh)
        self.assertEqual(
            meta["cli_version"],
            m.group(1),
            "bundled references were generated for a different CLI version",
        )


if __name__ == "__main__":
    unittest.main()
