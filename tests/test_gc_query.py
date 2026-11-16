"""Unit tests for scripts/gc_query.py against the saved schema fixture."""

from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import gc_query  # noqa: E402

FIXTURE = os.path.join(ROOT, "tests", "fixtures", "schema-0.17.0.json")


class QueryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.environ["GC_SCHEMA_JSON"] = FIXTURE
        with open(FIXTURE, "r", encoding="utf-8-sig") as fh:
            cls.schema = json.load(fh)

    @classmethod
    def tearDownClass(cls) -> None:
        os.environ.pop("GC_SCHEMA_JSON", None)

    def run_query(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = gc_query.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_find_node_accepts_path_with_or_without_prefix(self) -> None:
        self.assertEqual(gc_query.find_node(self.schema, "pr list")["path"], "gitcode pr list")
        self.assertEqual(gc_query.find_node(self.schema, "gitcode pr list")["path"], "gitcode pr list")
        self.assertEqual(gc_query.find_node(self.schema, "  PR   LIST ")["path"], "gitcode pr list")

    def test_unknown_command_exits_1_with_suggestion(self) -> None:
        code, _, err = self.run_query(["pr lst"])
        self.assertEqual(code, 1)
        self.assertIn("unknown command path", err)
        self.assertIn("gitcode pr list", err)

    def test_render_contains_usage_flags_and_examples(self) -> None:
        code, out, _ = self.run_query(["pr review"])
        self.assertEqual(code, 0)
        self.assertIn("用法: gitcode pr review <number>", out)
        self.assertIn("--approve", out)
        self.assertIn("示例:", out)
        # global flags are documented once in the footer, not per command
        self.assertEqual(out.count("--no-interactive"), 1)

    def test_search_matches_flag_names_too(self) -> None:
        code, out, _ = self.run_query(["--search", "dry-run"])
        self.assertEqual(code, 0)
        self.assertIn("gitcode issue create", out)
        self.assertIn("gitcode release delete", out)

    def test_list_filters_by_prefix(self) -> None:
        code, out, _ = self.run_query(["--list", "--prefix", "release"])
        self.assertEqual(code, 0)
        lines = [line for line in out.splitlines() if line.strip()]
        self.assertTrue(lines)
        self.assertTrue(all(line.startswith("gitcode release") for line in lines), lines[:3])

    def test_capabilities_marks_known_support(self) -> None:
        code, out, _ = self.run_query(["--capabilities"])
        self.assertEqual(code, 0)
        self.assertIn("| `gitcode pr merge` | ✓ | ✓ | ✓ |", out)
        self.assertIn("`gitcode pr checkout`", out)

    def test_json_mode_returns_raw_node(self) -> None:
        code, out, _ = self.run_query(["issue create", "--json"])
        self.assertEqual(code, 0)
        node = json.loads(out)
        self.assertEqual(node["path"], "gitcode issue create")
        self.assertTrue(any(f["name"] == "body-file" for f in node["flags"]))


if __name__ == "__main__":
    unittest.main()
