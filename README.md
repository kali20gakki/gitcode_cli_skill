# GitCode CLI Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-kali20gakki%2Fgitcode__cli__skill-181717?logo=github)](https://github.com/kali20gakki/gitcode_cli_skill)
[![Works with](https://img.shields.io/badge/Works%20with-Codex%20%7C%20Claude%20Code%20%7C%20OpenCode%20%7C%20DSH-0A7B83)](#快速上手)

一个面向 Codex、Claude Code、OpenCode、DeepSeek Harness（DSH）的 **GitCode CLI 操作 Skill**。

装上它之后，你只要说"看看这个 PR 的评论""CI 为什么挂了""发个 v1.0.0 release""把这个 issue 关掉"，Agent 就会自己调用 `gitcode` 命令完成：用 `--json` 解析结果、用文件传中文正文、破坏性操作先 `--dry-run` 再找你确认，并且**永远不会去读你的 token**。

覆盖 `gitcode` 0.17.0 的 **161 个叶命令**（仓库、分支与保护规则、Issue、PR 与评审、Release、Commit、Actions 流水线、标签、里程碑、搜索、用户、讨论、SSH Key），以及 `gitcode api` 任意 REST 接口兜底。

---

## 快速上手

### 1. 安装 Skill

#### Codex

```bash
npx skills add kali20gakki/gitcode_cli_skill --skill gitcode-cli -a codex -g -y
```

#### Claude Code

```bash
npx skills add kali20gakki/gitcode_cli_skill --skill gitcode-cli -a claude-code -g -y
```

#### OpenCode

```bash
npx skills add kali20gakki/gitcode_cli_skill --skill gitcode-cli -a opencode -g -y
```

#### DSH（DeepSeek Harness）

DSH 通过扫描本地 skills 目录加载，**放进去就热加载，不用重启**。`npx skills` 目前还没有 DSH 目标，所以用目录方式安装：

Windows PowerShell（用户级，推荐）：

```powershell
git clone https://github.com/kali20gakki/gitcode_cli_skill.git "$HOME\.agents\skills\gitcode-cli"
```

已经克隆到本地、只想装过去：

```powershell
Copy-Item -Recurse .\gitcode-cli "$HOME\.agents\skills\gitcode-cli"
```

Linux / macOS（用户级，推荐）：

```bash
git clone https://github.com/kali20gakki/gitcode_cli_skill.git ~/.agents/skills/gitcode-cli
# 或
cp -r ./gitcode-cli ~/.agents/skills/gitcode-cli
```

只对某个项目生效（项目级）：

```powershell
# projectRoot = 最近包含 .git 的祖先目录
Copy-Item -Recurse .\gitcode-cli "<your-repo>\.dsh\skills\gitcode-cli"
```

```bash
cp -r ./gitcode-cli <your-repo>/.dsh/skills/gitcode-cli
```

DSH 的 skill 扫描根（按要求从高到低）：

| 作用域 | 路径 |
| --- | --- |
| 项目级 | `<projectRoot>/.dsh/skills`、`<projectRoot>/.agents/skills` |
| 用户级 | `~/.dsh/skills`、`~/.agents/skills`（本文默认用这个） |

验证：在 DSH 里直接说「用 gitcode-cli skill 查看 atomgit-cli/cli 最近的 issue」，或看 skill 列表里是否出现 `gitcode-cli`。卸载就是删掉这个目录。

### 2. 安装 GitCode CLI（前置依赖）

```bash
npx -y atomgit-cli@latest install
gitcode version
gitcode doctor install --json
```

Windows PowerShell 如果报"禁止运行脚本"，改用 `.cmd` 入口：

```powershell
npx.cmd -y atomgit-cli@latest install
```

### 3. 认证

```bash
gitcode auth login     # 必须在你自己可交互的终端里执行，Agent 不应代输 token
gitcode auth status    # 只看登录状态，不会输出 token 值
```

CI 场景用 Secret 注入 `GC_TOKEN`，不要把 token 写进命令或脚本。

### 4. 直接开始用

```text
看看 atomgit-cli/cli 最近的 open issue，以及它们关联的 PR
```

```text
在 owner/repo 提一个 bug issue，标题是"登录超时"，正文用我给的 bug.md
```

```text
owner/repo 的 CI 挂了，帮我定位失败的 job 并把日志抓下来
```

```text
给 owner/repo 发 v1.2.0 release，说明在 notes.md，并把 dist/app.zip 传上去
```

```text
把这个 PR 的改动看一遍，先把审查意见给我看，确认后再发到 PR：
https://gitcode.com/owner/repo/pull/123
```

---

## 这个 Skill 能做什么

- **全命令覆盖**：`references/command-index.md` 列出 161 个叶命令；每个家族的完整 flag、类型、默认值、枚举、官方示例都在 `references/commands/*.md`。
- **先判断再执行**：`references/capabilities.md` 标出每条命令是否支持 `--json`、`-R`、`--yes`、`--dry-run`、`--paginate`、`--template`。
- **读用 JSON、写用文件**：解析类调用统一 `--json`；中文正文写 UTF-8 无 BOM 文件再传 `--body-file` / `--notes-file` / `--comment-file`。
- **破坏性操作有阶梯**：`--dry-run` → 说明影响 → 拿到本轮授权 → 才 `--yes`；绝不"为了跑通"擅自跳过确认。
- **凭据零接触**：明确禁止 `auth token`、`--show-token`、读取 `~/.config/gc/auth.json`、打印 `GC_TOKEN`。
- **自带自愈与体检**：`gc_preflight.py` 检查环境，`gc_query.py` 现场查真值，`gen_references.py` 在 CLI 升级后重建文档。

---

## 安装说明

### 推荐：skills CLI

先确认仓库能被识别：

```bash
npx skills add kali20gakki/gitcode_cli_skill --list
```

输出里能看到 `gitcode-cli` 就可以安装（见上文按 Agent 区分的命令）。

### 手动安装

拉取仓库：

```bash
git clone https://github.com/kali20gakki/gitcode_cli_skill.git gitcode-cli
cd gitcode-cli
```

**Codex**

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)" ~/.codex/skills/gitcode-cli
```

**Claude Code**

```bash
mkdir -p ~/.claude/skills
ln -s "$(pwd)" ~/.claude/skills/gitcode-cli
```

**OpenCode**

```bash
mkdir -p ~/.config/opencode/skills
ln -s "$(pwd)" ~/.config/opencode/skills/gitcode-cli
```

**DSH（Windows）**

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
if (Test-Path "$HOME\.agents\skills\gitcode-cli") { throw "target exists" }
Copy-Item -Recurse "$(Get-Location)" "$HOME\.agents\skills\gitcode-cli"
```

**DSH（Linux / macOS）**

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)" ~/.agents/skills/gitcode-cli
```

---

## 更新

### 使用 skills CLI

```bash
npx skills check
npx skills update
```

或重新安装一次最新版：

```bash
npx skills add kali20gakki/gitcode_cli_skill --skill gitcode-cli -a codex -g -y
```

把 `-a codex` 换成你实际用的 Agent（`claude-code` / `opencode`）。

### DSH / 手动安装

```powershell
git -C "$HOME\.agents\skills\gitcode-cli" pull
```

```bash
git -C ~/.agents/skills/gitcode-cli pull
```

如果是直接复制文件而不是软链接/克隆，重新复制一次即可。

### 升级了 gitcode CLI 之后

随包文档是按生成时的 CLI 版本产出的。升级后重建一次：

```bash
python scripts/gen_references.py          # 重建 references/
python scripts/gen_references.py --check  # 只比对，有差异退出码 1
python scripts/gc_query.py --check        # 检查版本与文档是否一致
```

---

## 令牌与认证

`gitcode` 的认证优先级：

| 来源 | 用途 | 是否必需 | 说明 |
| --- | --- | --- | --- |
| `GC_TOKEN` | 环境变量令牌 | 可选（优先于其余两者） | CI 推荐；不要写进命令历史 |
| `GITCODE_TOKEN` | 环境变量令牌 | 可选 | 兼容旧变量名 |
| `gitcode auth login` | 本地登录配置 | 本地开发推荐 | 落盘在 `~/.config/gc/`，由你本人执行 |

Agent 侧的硬规则：

- 不调用 `gitcode auth token`、不调用 `auth status --show-token`、不读 `~/.config/gc/auth.json`、不打印任何 token。
- 需要登录时，Agent 只能提示你自己去终端跑 `gitcode auth login`。
- 不要把 token、私钥、漏洞细节写进 issue/PR/comment/release 正文。

---

## 命令行脚本

```bash
python scripts/gc_preflight.py --json      # 环境体检：CLI/版本/认证/仓库解析/文档漂移
python scripts/gc_query.py "pr create"     # 查已装版本的真实参数与示例
python scripts/gc_query.py --search dry-run
python scripts/gc_query.py --capabilities  # 能力矩阵
python scripts/gen_references.py --check   # 文档是否落后于已装 CLI
python scripts/smoke_readonly.py           # 只读命令回归，结果写入 verification/
python -m unittest discover -s tests -v    # 离线单测 + 实测一致性
```

---

## 常见用法

```text
把 owner/repo 的 v1.0.0 到 v1.1.0 之间的合并 PR 列出来，按标签分组
```

```text
review PR owner/repo#123：先给我摘要和风险点，不要直接发评论
```

```text
确认 owner/repo#123 是否已合入 main，给出 merged 字段和合并时间
```

```text
流水线 run 456 失败了，把失败的 job 和日志关键片段摘出来
```

```text
GitCode 没有对应子命令，帮我取 owner/repo#123 改了哪些文件（用 gitcode api）
```

---

## 目录结构

```text
gitcode-cli/
├── SKILL.md                    # Agent 入口：路由、配方、安全红线
├── references/
│   ├── global-contract.md      # 全局契约（认证/输出/非交互/退出码/安全）
│   ├── command-index.md        # 全量命令索引（161 条）
│   ├── capabilities.md         # 能力矩阵
│   └── commands/               # 按家族拆分的完整参数与示例
├── scripts/                    # 查询 / 体检 / 生成 / 回归
├── tests/                      # 离线单测 + 与已装 CLI 的一致性测试
├── verification/               # smoke 与冷启动验证记录
└── evals/evals.json            # 冷启动评测提示词
```

---

## 注意事项

- 破坏性操作（合并、关闭、删除、改可见性、启停流水线）在非交互环境**必须显式 `--yes`**；没有用户授权就不要加。
- PR 正文里的裸 `#NNN` 会触发关联 Issue 自动关闭；修复型 PR 写 `Closes #N`，引用其他 Issue 用文字。
- `pr review --approve` 需要独立的审批权限，与合并权限不同；403 时降级为 `--comment`。
- Windows PowerShell 里 `gc` 是 `Get-Content` 的别名，请统一使用 `gitcode`。
- 中文正文走 UTF-8 文件，不要用 PowerShell 管道直接传，否则可能被编码损坏成 `???`。

---

## 版本与兼容

- 本 skill 以 **gitcode 0.17.0** 生成，`metadata.compatible_cli: ">=0.17.0"`。
- 0.12.0 → 0.17.0 的主要变化（由两份 schema 实测 diff 得出）：
  - 新增命令族：`actions setting`、`actions plugin`、`actions run rerun/retry/stop`、`ssh-key`、`repo archive/unarchive`、`release delete-asset`、`pr reviews`、`label edit`、`auth git-credential/setup-git`、discussions 的创建/编辑/删除与评论回复。
  - 新增能力：`api --jq/--paginate/--slurp/--include/--field`、`release download --clobber/--skip-existing`、`pr edit --mergers`、`actions run list --commit/--created`、`actions run watch --wait`。
- 低于 0.17.0 时这些命令/参数不存在：用 `python scripts/gc_query.py "<命令>"` 查真值，或先 `gitcode update`。

---

## 仓库与命名

- GitHub 仓库：`kali20gakki/gitcode_cli_skill`（仓库名带下划线）
- Skill 名称与目录名：`gitcode-cli`（见 `SKILL.md` 的 `name` 字段）

两者刻意不同：仓库名用了下划线，而 skill 目录/名称是 `gitcode-cli`。克隆到 skills 目录时请显式指定目标目录，避免生成 `gitcode_cli_skill` 这个目录名：

```bash
git clone https://github.com/kali20gakki/gitcode_cli_skill.git gitcode-cli
```

## License

[MIT](LICENSE)
