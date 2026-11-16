---
name: gitcode-cli
description: 用 gitcode CLI 在 GitCode 平台完成端到端研发操作——仓库与分支、Issue、PR（创建/评审/合并/评论/diff/行级评论）、Release 与资产、Commit、Actions 流水线排障、标签与里程碑、搜索、用户与讨论、SSH Key，以及用 `gitcode api` 兜底任意 REST 接口。当用户提到 GitCode、gitcode、gc 命令、GitCode 仓库/Issue/PR/MR/流水线/Release、`owner/repo` 形式的 GitCode 路径、gitcode.com 链接，或说"提个 PR""看看 CI 挂了没""发个 release""查下这个 issue""把评论发到 PR""列一下仓库分支/标签/里程碑"时，务必使用本 skill，即使用户没有点名要用 CLI。做任何 GitCode 写操作前，先用本 skill 的契约做安全检查与 `--dry-run`。深度 PR 代码审查工作流请改用 gitcode-code-reviewer skill。
license: MIT
metadata:
  version: "1.0.0"
  compatible_cli: ">=0.17.0"
  upstream: https://gitcode.com/atomgit-cli/cli
---

# GitCode CLI

`gitcode` 是 GitCode 官方命令行工具，把仓库、Issue、PR、Release、Actions 带回终端，并为 agent/脚本提供结构化、带安全边界的执行入口。本 skill 的价值不在"记住命令"，而在：**用对命令、用对 flag、用 `--json` 解析、用文件传正文、破坏性操作先预演再授权、永不碰 token**。

## 何时使用

- 用户要在 GitCode 上读或写任何东西（仓库、Issue、PR、Release、流水线、标签、里程碑、讨论、SSH Key）。
- 用户给了 `https://gitcode.com/<owner>/<repo>/...` 链接，或 `owner/repo` 形式的路径。
- 需要判断"某个改动是否已合入""CI 为什么挂""某个版本发了什么"。
- 需要调 GitCode REST 接口，但 CLI 没有对应 typed 命令。

不适用：纯本地 git 操作（用 git 本身）、GitHub 上的操作（用 `gh`）、GitCode 网页端交互。

## 第一步：30 秒前置检查

```bash
python scripts/gc_preflight.py          # 或 --json
```

它回答：CLI 在不在、版本多少、渠道是什么、**是否已认证**、默认仓库/当前仓库是哪个、随包文档是否与已装版本一致。判定规则：

- CLI 缺失 → 停下来给用户官方安装命令（`npx -y atomgit-cli@latest install`），不要猜路径。
- 未认证（`auth` 非 ok）→ 让用户**本人在自己的交互终端**执行 `gitcode auth login`；agent 不代输 token、不读配置文件。
- `schema_drift: yes` → 随包文档与已装版本不一致：以 `python scripts/gc_query.py "<命令>"` 的现场结果为准，并建议用户 `python scripts/gen_references.py` 重建文档。

## 动手前必读

`references/global-contract.md`（约 100 行）定义了每条命令都成立的规则：命令发现、认证、输出、非交互、退出码、仓库解析、正文编码、`api` 兜底、破坏性操作阶梯、平台语义与 Windows 注意事项。**任何写操作前必须读它**。

## 核心工作方式

1. **不要背参数。** 先用 `references/command-index.md` 找到命令，再看 `references/capabilities.md` 判断能否 `--json`/`--dry-run`/是否需要 `--yes`，最后读 `references/commands/<家族>.md` 拿完整 flag。
2. **不确定就读 CLI 自己。** `python scripts/gc_query.py "pr list"` 打印已装版本的参数与示例；`gitcode schema "<path>"` 是同一份真值的原始 JSON。
3. **读用 `--json`，写用文件。** 解析类调用一律 `--json`；中文/长正文先写 UTF-8 文件再传 `--body-file` / `--notes-file` / `--comment-file`。
4. **写前预演，写后回读。** 支持 `--dry-run` 的先预演；执行后用 `view --json` 校验结果，而不是只看退出码。
5. **别假设一定吃 `-R`。** 多数命令有 `-R/--repo`，但少数用位置参数（如 `repo view <owner>/<repo>`、`repo stats --branch`）；以 `capabilities.md` 的 `-R` 列为准，报 `unknown shorthand flag: 'R'` 就换位置参数。

## 安全红线（不可协商）

- 禁止 `gitcode auth token`、`gitcode auth status --show-token`、读取 `~/.config/gc/auth.json`，或打印 `GC_TOKEN` / `GITCODE_TOKEN`。
- 禁止把 token、私钥、漏洞细节、PoC、攻击步骤写进 issue/PR/comment/discussion/commit/release 正文（CLI 会扫描当前 token 值，但 agent 必须自觉）。
- 破坏性/状态变更操作：先 `--dry-run` 或 `view` → 向用户说明影响 → 拿到**本轮**明确授权 → 才加 `--yes`。没有授权就用普通失败结束，不要"为了跑通"擅自加 `--yes`。
- 写操作只对用户指定的仓库执行；先用 `gitcode repo view <repo> --json` 确认存在与权限，不要拿陌生仓库试写。
- PR 正文里的裸 `#NNN` 会自动关闭关联 Issue：修复型写 `Closes #N`，引用其他 Issue 用文字描述。

## 任务路由

| 我想… | 命令起点 | 参考文件 |
| --- | --- | --- |
| 看仓库/分支/保护规则/贡献统计 | `repo view`、`repo branch list`、`repo branch-protection list`、`repo stats` | `commands/repo.md` |
| 读 Issue 及其评论、关联 PR | `issue list/view --comments`、`issue comments`、`issue prs` | `commands/issue.md` |
| 建/改 Issue，打标签，指派 | `issue create`（`--body-file`、`--dry-run`）、`issue edit`、`issue label` | `commands/issue.md` |
| 建 PR、改 PR、合并、关闭 | `pr create`、`pr edit`、`pr merge --method`、`pr close` | `commands/pr.md` |
| 评审 PR（整体/行级/回复/解决） | `pr diff`、`pr review`、`pr comment --path --position`、`pr reply`、`pr comment resolve` | `commands/pr.md` |
| 看 PR 的评论、审阅状态、关联 Issue | `pr comments`、`pr reviews`、`pr issues` | `commands/pr.md` |
| 发版、传资产、下载产物 | `release create/upload/download/view` | `commands/release-commit.md` |
| 查提交历史、diff、patch、提交评论 | `repo log`、`commit view --show-diff`、`commit diff`、`commit comments` | `commands/release-commit.md` |
| CI 挂了要定位 | `actions run list --status FAILED` → `job list` → `job log --output` | `commands/actions.md` |
| 启用/停用流水线、校验 workflow YAML | `actions setting enable/disable`、`actions yaml validate` | `commands/actions.md` |
| 管标签、里程碑 | `label create/list/delete`、`milestone create/edit/list/view` | `commands/issue.md` |
| 搜仓库/Issue/用户 | `search repos`、`search issues`、`search users` | `commands/search-user.md` |
| 看/改个人资料、SSH Key、讨论 | `user view/edit`、`ssh-key list/add/delete`、`discussions ...` | `commands/search-user.md`、`commands/ops.md` |
| CLI 没有的接口 | `gitcode api <endpoint> --jq` | `global-contract.md` §8 |
| 认证/配置/升级/环境诊断 | `auth status`、`config list/set`、`doctor install`、`update --check` | `commands/ops.md` |

## 高频配方

### A. Issue → PR 闭环

```bash
gitcode issue view 42 -R owner/repo --json           # 需求与状态
git checkout -b fix/42-timeout main                   # 分支用 git 建
# …改代码、提交、推送…
cat > pr-body.md <<'EOF'
修复超时未重试的问题。

Closes #42
EOF
gitcode pr create -R owner/repo --base main --head fix/42-timeout \
  --title "fix: retry on timeout" --body-file pr-body.md --json
gitcode pr view <new-number> -R owner/repo --json     # 用返回的 number 回读
```

### B. 评审 PR

```bash
gitcode pr diff 123 -R owner/repo --json
gitcode pr comments 123 -R owner/repo --json
gitcode pr reviews 123 -R owner/repo --json
gitcode pr review 123 -R owner/repo --comment-file review.md --json      # 整体意见
gitcode pr comment 123 -R owner/repo --path src/a.go --position 42 \
  --body-file line-note.md --json                                        # 行级评论
gitcode pr comment resolve 123 <discussion-id> -R owner/repo             # 标记已解决
```

`--approve` 需要独立的审批权限；403 时降级为 `--comment`，不要反复重试。

需要**具体文件清单**时注意：`pr diff --json` 的 `files[].path` 可能为空（文本 diff 也可能缺 `diff --git` 头），此时用 REST 兜底 `gitcode api repos/owner/repo/pulls/123/files --jq '.[].filename'`。

### C. 发布

```bash
gitcode release create v1.0.0 -R owner/repo --title "v1.0.0" \
  --notes-file notes.md --json
gitcode release upload v1.0.0 dist/app.zip -R owner/repo --json
gitcode release view v1.0.0 -R owner/repo --json
gitcode release download v1.0.0 -R owner/repo --output ./dist --clobber
```

### D. 流水线排障

```bash
gitcode actions run list -R owner/repo --status FAILED --limit 10 --json
gitcode actions run view <run-id> -R owner/repo --json
gitcode actions job list <run-id> -R owner/repo --json
gitcode actions job view <run-id> <job-id> -R owner/repo --json
gitcode actions job log <run-id> <job-id> -R owner/repo --output job.zip    # 产出 ZIP，解包后读失败步骤的 .log
```

### E. typed 命令未覆盖时用 API 兜底

```bash
gitcode api repos/owner/repo/pulls/123/files --jq '.[].filename'
gitcode api 'repos/owner/repo/commits?path=README.md&sha=main' --paginate --slurp
gitcode api repos/owner/repo/pulls/123 --method PATCH --input body.json
```

## 红旗与自愈

| 症状 | 含义 | 处置 |
| --- | --- | --- |
| `unknown flag` / `unknown command` | 已装版本与文档不一致（多为旧版） | `gc_query.py` 查真值；提示升级 `gitcode update` |
| 退出码 2 | 参数/用法错误 | 读 stderr 指出缺哪个必填 flag，如 `repo stats` 需要 `--branch` |
| 退出码 3 | 资源不存在 | 核对 owner/repo/number |
| 退出码 4 | 认证/权限 | 让用户登录或确认权限；不要用 curl+token 绕过 |
| 输出巨大 | JSON 全量回显 | `--limit` / `--per-page` / `--output` 落盘，或改用 `gitcode api --jq` 裁剪 |
| 中文变 `???` | PowerShell 管道编码 | 写 UTF-8 文件后 `--body-file` |
| 解包/后缀报错 | `actions job log --output` 写出的是 ZIP | 用 `.zip` 命名，解包后读失败步骤的 `.log` |
| 命令挂起 | 交互式确认 | 加 `--no-interactive`，授权后加 `--yes` |

## 与其它 skill 的分工

- `gitcode-code-reviewer`：深度代码审查工作流（逐行评论、上下文分析）。需要"像人一样审查"时用它；只是"把评论发上去""看 diff"用本 skill。
- `gitcode-release-note-generator`：基于真实数据生成正式 Release Note 文档。本 skill 只负责把生成好的 notes 发到 Release。
- 纯 git 操作（clone/branch/commit/push）：用 git；本 skill 只在需要 GitCode 平台能力时介入。

## 参考文件

| 文件 | 何时读 |
| --- | --- |
| `global-contract.md` | 动手前；写操作与安全规则 |
| `command-index.md` | 不知道用哪条命令 |
| `capabilities.md` | 判断 `--json` / `--dry-run` / `--yes` / 分页支持 |
| `commands/pr.md` | PR 及评审、评论、合并 |
| `commands/issue.md` | Issue、标签、里程碑 |
| `commands/repo.md` | 仓库、分支、保护规则、可见性 |
| `commands/release-commit.md` | Release、Commit |
| `commands/actions.md` | 流水线、Job、Artifact、Runner、YAML |
| `commands/search-user.md` | 搜索、用户、讨论 |
| `commands/ops.md` | `api`、认证、配置、升级、诊断、SSH Key |

## 维护

- 升级 CLI 后：`python scripts/gen_references.py` 重建文档，`--check` 验证一致。
- 怀疑文档过期：`python scripts/gc_query.py --check`。
- 端到端自检：`python scripts/smoke_readonly.py`（只读矩阵，结果写入 `verification/`）。
