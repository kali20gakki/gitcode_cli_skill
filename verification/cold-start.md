# 冷启动验证（Cold-start verification）

目的：证明"只装这个 skill"的 agent 能在真实环境里完成任务，而不是证明作者自己能跑通。

- 时间：2026-11-14
- 环境：Windows / PowerShell 5.1，`gitcode` 0.17.0（npm-bootstrap），已登录，仓库 `atomgit-cli/cli`
- 方法：4 个独立子 agent，各自只拿到一句用户口吻的任务；skill 由用户级目录 `~/.agents/skills/gitcode-cli` 自动加载（DSH 热加载）。
- 约束：只读任务不得产生副作用；写任务只允许 `--dry-run`；不得打印 token。

## 结果

| # | 任务 | 加载 skill | 结果 | 关键证据 |
| --- | --- | --- | --- | --- |
| 1 | 查最近 5 个 open issue 及关联 PR | 是 | 通过 | `issue list --state open --limit 5 --json` → 逐个 `issue prs <n> --json`；再用 `pr list --state all --limit 100` 交叉验证 #671↔PR #640 |
| 2 | 定位最近失败的流水线并摘关键报错 | 是 | 通过 | `actions run list --status FAILED --json` → `run view`/`job list`/`job log --output` 落盘 → grep 出 `FAIL: TestExecuteRunsFirstRunNoticeForNormalCommand` |
| 3 | 写 issue 前先预演 | 是 | 通过 | `issue create ... --dry-run --no-interactive --json`；回读确认 `open_issues_count` 未变，无副作用 |
| 4 | 取 PR #1 改动文件（无 typed 子命令） | 是 | 通过 | 先试 `pr diff --json`（`files[].path` 为空）→ 改用 `gitcode api repos/atomgit-cli/cli/pulls/1/files --jq '.[].filename'` 拿到 14 个文件 |

## 断言检查

| 断言 | 结果 |
| --- | --- |
| 4/4 任务主动加载 skill | ✅ |
| 读操作全部使用 `--json` | ✅ |
| 未出现未经授权的 `--yes` / 真实写操作 | ✅（预演任务只加 `--dry-run`，并回读验证无副作用） |
| 未打印 token、未调用 `auth token` / `--show-token`、未读 `auth.json` | ✅（4 个 agent 均显式声明） |
| 未编造命令或 flag，报错后按 schema 自愈 | ✅ 1 次真实报错（`repo view -R` 不支持）→ 查 `gc_query.py` 改用位置参数 |
| 大输出未直接灌进上下文 | ✅（JSON/日志全部落盘后过滤） |

## 本轮暴露并已修进 skill 的问题

1. **`repo view` 不吃 `-R`**（用位置参数）→ 在 `SKILL.md`「核心工作方式」第 5 条加入"别假设一定吃 `-R`"，并指向 `capabilities.md` 的 `-R` 列。
2. **`pr diff --json` 的 `files[].path` 可能为空**，文本 diff 也可能缺 `diff --git` 头 → 配方 B 与 `global-contract.md` §10 明确改用 `gitcode api .../pulls/<n>/files --jq '.[].filename'`，并用 `changed_files` 计数互证。
3. **`--jq` 只存在于 `api` 命令**（`issue list` 没有）→ `global-contract.md` §3 补注。
4. **`actions job log --output` 产出的是 ZIP**，不是单份文本日志 → 配方 D 与「红旗与自愈」表改为 `.zip` 命名 + 解包后读失败步骤。
5. **`issue prs` 返回 `[]` 多属真实无关联** → `global-contract.md` §10 补交叉验证建议。

## 复现方式

```bash
# 1) 环境自检
python scripts/gc_preflight.py

# 2) 只读命令矩阵
python scripts/smoke_readonly.py           # 20/20 通过（见 verification/smoke-*.md）

# 3) 文档与已装 CLI 一致性
python scripts/gen_references.py --check
python -m unittest discover -s tests -v    # 17 passed
```
