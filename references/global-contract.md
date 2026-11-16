# 全局契约

> 本文件只写"对每条命令都成立"的规则。具体 flag 见 `command-index.md` / `capabilities.md` / `commands/*.md`。
> 依据：`gitcode schema`（CLI 0.17.0 实测）+ 官方 `docs/AI-GUIDE.md`、`AGENTS.md`。

## 1. 命令发现：不确定就查，不要猜

| 需求 | 做法 |
| --- | --- |
| 有哪些命令 | `gitcode schema`（JSON 全树）、`gitcode help --json`、`gitcode help --topics` |
| 某条命令的完整参数 | `python scripts/gc_query.py "pr list"`（读本地 CLI，最准）或 `gitcode schema "pr list"` |
| 按关键字找命令 | `gitcode help --search <keyword>`、`python scripts/gc_query.py --search <keyword>` |
| 环境是否就绪 | `python scripts/gc_preflight.py`（CLI/版本/认证/仓库解析/文档漂移） |
| 文档是否过期 | `python scripts/gc_query.py --check` |

`completion` 与 `help` 是 cobra 内建命令，不出现在 `schema` 中：`gitcode completion <shell>`、`gitcode help <command>`。

## 2. 认证与凭据

- 认证优先级：`GC_TOKEN` > `GITCODE_TOKEN` > 本地登录配置（`gitcode auth login`，落在 `~/.config/gc/`）。
- 查状态用 `gitcode auth status` / `gitcode auth status --json`（只含 `logged_in`、`username`、`token_source`，不含 token 值）。
- **禁止**调用 `gitcode auth token`、`gitcode auth status --show-token`、读取 `~/.config/gc/auth.json`，或打印 `GC_TOKEN` / `GITCODE_TOKEN`。需要登录时让用户**本人**在私有交互终端执行 `gitcode auth login`，agent 不代输 token。
- 凭据只从环境变量或用户已有登录态来；CI 用平台 Secret 注入。

## 3. 输出与解析

| 场景 | 用法 |
| --- | --- |
| 程序解析 | `--json`（stdout 只有 JSON；warning 走 stderr；失败时不要从 stdout 解析半成品） |
| 表格/简化 | `--format table` / `--format simple`（`--format json` 等价 `--json`） |
| 自定义裁剪 | `--template '{{range .}}#{{.Number}} {{.Title}}{{"\n"}}{{end}}'`（目前仅 `issue list` 支持，见 `capabilities.md`） |
| 时间显示 | `--time-format absolute\|relative` |
| 原始 API 裁剪 | `gitcode api <endpoint> --jq '.field'`（0.17+；`--jq` **只存在于 `api` 命令**，其它命令请 `--json` 后交给本地 jq/Python 处理） |
| 结果量 | `--limit`、`--per-page`、`--page`、`--paginate`（`--paginate` 时 `--per-page` 默认 100） |

支持度因命令而异，先看 `capabilities.md` 的矩阵，不要假设所有命令都有 `--json`。

## 4. 非交互与确认

- agent 场景建议显式加 `--no-interactive`：无法继续时立即失败并提示 `--yes`，而不是挂起等输入。
- 破坏性/状态变更命令在非 TTY 下**未传 `--yes` 会直接失败**（`pr merge`、`issue close`、`pr edit`、`release delete`、`repo delete`、`actions setting` 等 33 条，见 `capabilities.md` 的 `--yes` 列）。
- 关闭更新检查，避免提示污染 stdout 与退出码：`GC_NO_UPDATE_CHECK=1` 或每条命令加 `--no-update-check`；`CI=true` 也会禁用。

## 5. 退出码

| 码 | 含义 | agent 处置 |
| --- | --- | --- |
| 0 | 成功 | — |
| 1 | 通用错误 | 读 stderr，重试一次；仍失败则报告 |
| 2 | 参数/用法错误 | 用 `gc_query.py` 校正 flag，不要盲目重试 |
| 3 | 资源不存在 | 确认 owner/repo/number 拼写 |
| 4 | 认证/权限错误 | 让用户登录或确认权限，不要绕过 |
| 5 | 资源冲突 | 状态已变化，重新读取后再决定 |

## 6. 仓库解析顺序

1. 显式 `-R owner/repo`（161 个叶命令中 104 条支持）。
2. 当前目录所属 git 仓库的 `origin`。
3. `gitcode repo set-default` 设置的默认仓库（`--view` 查看，`--unset` 清除）。

三者都没有时报错。非 git 目录下务必带 `-R`，或先 `gitcode repo set-default owner/repo`。

## 7. 正文、编码与安全扫描

- 正文参数：`--body/-b`（issue/pr/comment）、`--body-file/-F`、`--comment/-c`、`--comment-file/-F`、`--notes/-n`、`--notes-file/-F`、`--description/-d` / `--description-file`。
- `-` 表示从 stdin 读：`gitcode pr comment 10 --body-file - < body.md`。
- **中文/非 ASCII 一律写 UTF-8 无 BOM 文件再传 `*-file`**。Windows PowerShell 管道会按本地代码页编码，CLI 会拦截疑似损坏成 `???` 的内容。
- CLI 提交前会扫描当前 `GC_TOKEN`/`GITCODE_TOKEN` 值并拒绝泄漏；agent 自己也不得把 token、私钥、漏洞细节、PoC 写进任何 issue/PR/comment/discussion/release 正文。

## 8. `gitcode api` 兜底

- `gitcode api <endpoint>`：未以 `/api/` 开头时自动补 `/api/v5`。
- `--method`（GET/POST/PATCH/DELETE…）、`--input <file|->`（请求体）、`--header "Name: value"`。
- 0.17+：`--jq <expr>` 过滤响应、`--paginate`（跟随 page 参数）、`--slurp`（合并为单数组）、`--include`（输出响应头）。HTTP 304 以非零码结束，可用于"无变化"判断。
- 含 `&` 的查询串整体加引号：`gitcode api 'repos/o/r/commits?path=a&sha=main'`。
- 已知端点见 GitCode API 文档；不要凭 GitHub API 语义类比猜测。

## 9. 破坏性操作阶梯

1. 先 `--dry-run`（issue create、release delete、repo delete、label/milestone delete、actions artifact delete 等支持）或先 `view` 打印现状。
2. 向用户说明"将改变什么、影响哪些对象"。
3. 拿到**本轮**明确授权后，才加 `--yes` 执行。
4. 执行后回读校验（`view`/`--json`），不要只看退出码。

## 10. 平台语义注意

- **PR 正文里的裸 `#NNN`（无 `Closes`/`Fixes`/`Resolves`/`Refs` 前缀）会触发关联 Issue 自动关闭**。引用其他 issue 要用文字描述；修复型 PR 写 `Closes #N`。
- commit message 里的 `Closes` 不被 GitCode 识别，只有 PR body 生效。
- PR JSON 的 `merged` 已按 `state`/`merged_at` 归一为布尔，直接用。
- `pr diff --json` 的 `files[].path` 可能为空、文本 diff 可能缺 `diff --git` 文件头；要文件清单用 `gitcode api repos/<owner>/<repo>/pulls/<n>/files --jq '.[].filename'`，可与 `pr view --json` 的 `changed_files` 计数互相印证。
- `actions job log --output <file>` 写出的是 **ZIP 归档**（内含按步骤拆分的 `*.log`），不是单个文本日志。用 `.zip` 命名再解包，直接读失败步骤那一份；不要整份灌进上下文。
- `issue prs <n>` 返回 `[]` 通常是"确实没有关联 PR"，可再用 `pr list --json` 按 `head.ref`/`body` 交叉验证，避免误判为命令用法错误。
- `pr review --approve` 需要独立的"审批权限"，与合并权限不同；403 时降级为 `--comment`。GitCode 无原生 request-changes，`--request` 实际是发一条 `[REQUEST CHANGES]` 前缀评论。

## 11. Windows / PowerShell

- PowerShell 预置 `gc` 为 `Get-Content` 别名 → 统一用 `gitcode`（或 `gc.exe`）。
- 执行策略可能禁止 `npx.ps1`：用 `npx.cmd`，或 `node "<nodejs>\node_modules\npm\bin\npx-cli.js"`。
- 含 `&` 的 URL、含空格的路径加引号；中文正文用文件传入（见 §7）。
