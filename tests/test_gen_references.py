"""Unit tests for the reference generator (offline, fixture-driven)."""

from __future__ import annotations

import json
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import gen_references as gen  # noqa: E402

FIXTURE = os.path.join(ROOT, "tests", "fixtures", "schema-0.17.0.json")


def load_fixture() -> dict:
    with open(FIXTURE, "r", encoding="utf-8-sig") as fh:
        return json.load(fh)


def leaf_paths(schema: dict) -> list:
    return sorted(
        n["path"]
        for n in gen.walk(schema)
        if len(n["path"].split()) > 1 and not (n.get("subcommands") or [])
    )


class GeneratorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_fixture()
        cls.files = gen.build(cls.schema, "0.17.0", "deadbeef")

    def test_every_leaf_command_is_documented_exactly_once(self) -> None:
        leaves = leaf_paths(self.schema)
        self.assertGreaterEqual(len(leaves), 150, "fixture looks truncated")

        index = self.files["references/command-index.md"]
        for path in leaves:
            self.assertEqual(
                index.count(f"| `{path}` |"), 1, f"{path} missing or duplicated in command-index"
            )

        family_docs = "".join(
            self.files[f"references/{rel}"] for rel in gen.FILE_ORDER
        )
        for path in leaves:
            self.assertEqual(
                family_docs.count(f"### `{path}`"), 1, f"{path} missing or duplicated in family docs"
            )

    def test_every_top_level_command_is_mapped(self) -> None:
        tops = {gen.top_level_of(p) for p in leaf_paths(self.schema)}
        unmapped = tops - set(gen.FAMILIES)
        self.assertEqual(unmapped, set(), f"unmapped top-level commands: {sorted(unmapped)}")

    def test_generation_is_deterministic(self) -> None:
        again = gen.build(self.schema, "0.17.0", "deadbeef")
        self.assertEqual(self.files, again)

    def test_capabilities_matrix_matches_schema(self) -> None:
        doc = self.files["references/capabilities.md"]
        self.assertIn("| `gitcode pr merge` | ✓ | ✓ | ✓ |", doc)
        # pr checkout has no --json: the JSON cell must stay empty
        self.assertIn("| `gitcode pr checkout` |  |", doc)

    def test_flag_details_are_preserved(self) -> None:
        pr = self.files["references/commands/pr.md"]
        self.assertIn("`--approve`", pr)
        self.assertIn("`--comment-file`", pr)
        # enum values and defaults must survive the round-trip
        self.assertIn("可选: merge, squash, rebase", pr)
        self.assertIn("| `--base` | `B` | string | main |", pr)

    def test_multiline_examples_keep_continuations(self) -> None:
        pr = self.files["references/commands/pr.md"]
        self.assertIn("--target-repo", pr)

    def test_meta_records_version_and_hash(self) -> None:
        meta = json.loads(self.files["references/.schema-meta.json"])
        self.assertEqual(meta["cli_version"], "0.17.0")
        self.assertEqual(meta["schema_sha256"], "deadbeef")
        self.assertEqual(meta["leaf_commands"], len(leaf_paths(self.schema)))

    def test_root_node_is_not_rendered_as_a_group(self) -> None:
        ops = self.files["references/commands/ops.md"]
        self.assertNotIn("### `gitcode`\n", ops)


if __name__ == "__main__":
    unittest.main()
