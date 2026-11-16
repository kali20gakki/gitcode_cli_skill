# pr — Pull Request 命令

> 自动生成：`scripts/gen_references.py` ← `gitcode schema`（CLI 0.17.0）。请勿手工编辑；需要现场真值时用 `python scripts/gc_query.py "<命令路径>"`。

## 命令清单

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode pr checkout` | Check out a pull request locally | — |
| `gitcode pr close` | Close a pull request | ✓ |
| `gitcode pr comment delete` | Delete a PR comment | — |
| `gitcode pr comment edit` | Edit a PR comment | — |
| `gitcode pr comment resolve` | Mark a PR comment discussion as resolved | — |
| `gitcode pr comment unresolve` | Mark a PR comment discussion as unresolved | — |
| `gitcode pr comments` | List comments on a pull request | ✓ |
| `gitcode pr create` | Create a pull request | ✓ |
| `gitcode pr diff` | View changes in a pull request | ✓ |
| `gitcode pr edit` | Edit a pull request | ✓ |
| `gitcode pr issues` | List issues linked to a pull request | ✓ |
| `gitcode pr label` | Manage labels on a PR | ✓ |
| `gitcode pr list` | List pull requests | ✓ |
| `gitcode pr merge` | Merge a pull request | ✓ |
| `gitcode pr ready` | Toggle PR ready/wip status | ✓ |
| `gitcode pr reopen` | Reopen a closed pull request | ✓ |
| `gitcode pr reply` | Reply to a PR comment discussion | ✓ |
| `gitcode pr review` | Review a pull request | ✓ |
| `gitcode pr reviews` | View review states on a pull request | ✓ |
| `gitcode pr sync` | Sync a PR from one repository to another | ✓ |
| `gitcode pr test` | Trigger or manage PR tests | — |
| `gitcode pr view` | View a pull request | ✓ |

## 命令组

### `gitcode pr`

Manage pull requests

子命令: `checkout`, `close`, `comment`, `comments`, `create`, `diff`, `edit`, `issues`, `label`, `list`, `merge`, `ready`, `reopen`, `reply`, `review`, `reviews`, `sync`, `test`, `view`

### `gitcode pr comment`

Add a comment to a pull request

子命令: `delete`, `edit`, `resolve`, `unresolve`

## 详细参数

### `gitcode pr checkout`

Check out a pull request locally

`用法: gitcode pr checkout <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--branch` | `b` | string | — | Custom branch name |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr checkout 123 -R owner/repo
gitcode pr checkout 123 -R owner/repo --branch my-feature
```

### `gitcode pr close`

Close a pull request

`用法: gitcode pr close <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--comment` | `c` | string | — | Add a comment before closing |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode pr close 123 -R owner/repo
gitcode pr close 123 -R owner/repo --comment "Not needed anymore" --yes
gitcode pr close 123 -R owner/repo --json
```

### `gitcode pr comment delete`

Delete a PR comment

`用法: gitcode pr comment delete <comment-id>`

参数: `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode pr comment delete 123 -R owner/repo
gitcode pr comment delete 123 -R owner/repo --yes
```

### `gitcode pr comment edit`

Edit a PR comment

`用法: gitcode pr comment edit <comment-id>`

参数: `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | New comment body |
| `--body-file` | `F` | string | — | Read comment body from file (use - for stdin) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr comment edit 123 --body "Updated text" -R owner/repo
gitcode pr comment edit 123 --body-file comment.md -R owner/repo
echo "Updated text" | gitcode pr comment edit 123 --body-file - -R owner/repo
```

### `gitcode pr comment resolve`

Mark a PR comment discussion as resolved

`用法: gitcode pr comment resolve <pr-number> <discussion-id>`

参数: `<pr-number>`（必填）, `<discussion-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr comment resolve 123 d1 -R owner/repo
```

### `gitcode pr comment unresolve`

Mark a PR comment discussion as unresolved

`用法: gitcode pr comment unresolve <pr-number> <discussion-id>`

参数: `<pr-number>`（必填）, `<discussion-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr comment unresolve 123 d1 -R owner/repo
```

### `gitcode pr comments`

List comments on a pull request

`用法: gitcode pr comments <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 0 | Maximum number of comments to list (0 = all) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr comments 123 -R owner/repo
gitcode pr comments 123 --limit 5 -R owner/repo
gitcode pr comments 123 -R owner/repo --json
```

### `gitcode pr create`

Create a pull request

`用法: gitcode pr create`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--base` | `B` | string | main | Base branch |
| `--body` | `b` | string | — | Body for the PR |
| `--body-file` | — | string | — | Read body from file (use - for stdin) |
| `--draft` | `d` | bool | false | Create as draft |
| `--fill` | `f` | bool | false | Fill from last commit |
| `--fork` | `F` | string | — | Fork repository path for cross-repo PR (owner/repo) |
| `--head` | `H` | string | — | Head branch (default: current branch) |
| `--json` | — | bool | false | Output as JSON |
| `--labels` | `l` | stringSlice | [] | Add labels (comma-separated) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--title` | `t` | string | — | Title for the PR |
| `--web` | `w` | bool | false | Open in browser |

**示例**

```bash
gitcode pr create -R owner/repo --title "Feature" --body "Description"
gitcode pr create -R owner/repo --title "Feature" --body-file description.md
cat description.md | gitcode pr create -R owner/repo --title "Feature" --body-file -
```

### `gitcode pr diff`

View changes in a pull request

`用法: gitcode pr diff <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr diff 123 -R owner/repo
gitcode pr diff 123 --json -R owner/repo
```

### `gitcode pr edit`

Edit a pull request

`用法: gitcode pr edit <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--add-assignee` | — | stringSlice | [] | Add assignees (comma-separated usernames) |
| `--add-label` | — | stringSlice | [] | Add labels while preserving existing labels (comma-separated) |
| `--add-reviewer` | — | stringSlice | [] | Add reviewers (comma-separated usernames) |
| `--add-tester` | — | stringSlice | [] | Add testers (comma-separated usernames) |
| `--base` | — | string | — | New base branch |
| `--body` | `b` | string | — | New body |
| `--body-file` | `F` | string | — | Read body from file |
| `--close-related-issue` | — | string | — | Close related issues when merged (true/false)（可选: true, false） |
| `--draft` | — | string | — | Mark as draft (true/false)（可选: true, false） |
| `--json` | — | bool | false | Output as JSON |
| `--labels` | `l` | stringSlice | [] | Add labels (comma-separated; compatibility alias) |
| `--mergers` | — | stringSlice | [] | Set PR mergers, replacing any previous set (comma-separated usernames) |
| `--milestone` | `m` | int | 0 | Set milestone by number |
| `--remove-assignee` | — | stringSlice | [] | Remove assignees (comma-separated usernames) |
| `--remove-label` | — | stringSlice | [] | Remove labels while preserving other labels (comma-separated) |
| `--remove-reviewer` | — | stringSlice | [] | Remove reviewers (comma-separated usernames) |
| `--remove-tester` | — | stringSlice | [] | Remove testers (comma-separated usernames) |
| `--replace-labels` | — | stringSlice | [] | Replace all labels (comma-separated; use an empty value to clear) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--title` | `t` | string | — | New title |
| `--yes` | `y` | bool | false | Skip confirmation for replacing all labels |

**示例**

```bash
gitcode pr edit 123 -R owner/repo --title "New title"
gitcode pr edit 123 -R owner/repo --body "New description"
gitcode pr edit 123 -R owner/repo --body-file description.md
```

### `gitcode pr issues`

List issues linked to a pull request

`用法: gitcode pr issues <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr issues 123 -R owner/repo
gitcode pr issues 123
gitcode pr issues 123 -R owner/repo --json
```

### `gitcode pr label`

Manage labels on a PR

`用法: gitcode pr label <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--add` | `a` | stringSlice | [] | Add labels (comma-separated) |
| `--json` | — | bool | false | Output as JSON |
| `--list` | `l` | bool | false | List labels |
| `--remove` | `r` | string | — | Remove a label |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr label 123 --add bug,enhancement -R owner/repo
gitcode pr label 123 --remove bug -R owner/repo
gitcode pr label 123 --list -R owner/repo
```

### `gitcode pr list`

List pull requests

`用法: gitcode pr list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--base` | `B` | string | — | Filter by base branch |
| `--commit-message` | — | string | — | Filter PRs whose commit messages contain text |
| `--direction` | — | string | — | Sort direction (asc/desc)（可选: asc, desc） |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--head` | `H` | string | — | Filter by head branch |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of PRs to list |
| `--milestone` | `m` | string | — | Filter by milestone title |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--sort` | — | string | — | Sort by created/updated/popularity/long-running（可选: created, updated, popularity, long-running） |
| `--state` | `s` | string | open | Filter by state (open/closed/merged/all)（可选: open, closed, merged, all） |

**示例**

```bash
gitcode pr list -R owner/repo
gitcode pr list -R owner/repo --state closed
gitcode pr list -R owner/repo --head feature/login --base main
```

### `gitcode pr merge`

Merge a pull request

`用法: gitcode pr merge <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--delete-branch` | `d` | bool | false | Delete branch after merge |
| `--json` | — | bool | false | Output as JSON |
| `--method` | `m` | string | merge | Merge method (merge/squash/rebase)（可选: merge, squash, rebase） |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode pr merge 123 -R owner/repo
gitcode pr merge 123 -R owner/repo --method squash
gitcode pr merge 123 -R owner/repo --delete-branch
```

### `gitcode pr ready`

Toggle PR ready/wip status

`用法: gitcode pr ready <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--ready` | `r` | bool | false | Mark as ready for review |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--wip` | `w` | bool | false | Mark as work-in-progress |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode pr ready 123 -R owner/repo
gitcode pr ready 123 -R owner/repo --wip
gitcode pr ready 123 -R owner/repo --yes
```

### `gitcode pr reopen`

Reopen a closed pull request

`用法: gitcode pr reopen <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--comment` | `c` | string | — | Add a comment after reopening |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode pr reopen 123 -R owner/repo
gitcode pr reopen 123 -R owner/repo --comment "Reopening for further changes"
gitcode pr reopen 123 -R owner/repo --yes
```

### `gitcode pr reply`

Reply to a PR comment discussion

`用法: gitcode pr reply <pr-number> --discussion <id> --body <text>`

参数: `<pr-number>`（必填）, `<id>`（必填）, `<text>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | **必填** Reply body text |
| `--discussion` | `d` | string | — | **必填** Discussion ID to reply to |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr reply 123 --discussion abc123 --body "Thanks for the feedback!" -R owner/repo
gitcode pr reply 123 --discussion abc123 --body "Line 1
Line 2" -R owner/repo
gitcode pr reply 123 --discussion abc123 --body "ack" --json -R owner/repo
```

### `gitcode pr review`

Review a pull request

`用法: gitcode pr review <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--approve` | `a` | bool | false | Approve the PR |
| `--comment` | `c` | string | — | Comment body |
| `--comment-file` | `F` | string | — | Read comment from file (use - for stdin) |
| `--force` | — | bool | false | Force approval (admin only) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--request` | `r` | bool | false | Request changes on the PR (posts a [REQUEST CHANGES] comment) |
| `--yes` | — | bool | false | Skip force approval confirmation |

**示例**

```bash
gitcode pr review 123 -R owner/repo --approve
gitcode pr review 123 -R owner/repo --comment "Looks good to me"
gitcode pr review 123 -R owner/repo --comment-file review-notes.md
```

### `gitcode pr reviews`

View review states on a pull request

`用法: gitcode pr reviews <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode pr reviews 123 -R owner/repo
gitcode pr reviews 123 -R owner/repo --json
```

### `gitcode pr sync`

Sync a PR from one repository to another

`用法: gitcode pr sync`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--base` | — | string | — | Base branch in target repository (default: target default branch) |
| `--body` | — | string | — | Pull request body (default: inherit from source PR with sync info) |
| `--draft` | — | bool | false | Create the pull request as draft |
| `--json` | — | bool | false | Output as JSON |
| `--source-pr` | — | string | — | **必填** Source PR (owner/repo#number or URL) |
| `--target-repo` | — | string | — | **必填** Target repository (owner/repo) |
| `--title` | — | string | — | Pull request title (default: [sync] <source title>) |
| `--yes` | — | bool | false | Skip confirmation prompt before pushing and creating the target PR |

**示例**

```bash
gitcode pr sync --source-pr owner/source-repo#123 --target-repo owner/target-repo
gitcode pr sync --source-pr owner/source-repo#123 \
--target-repo owner/target-repo \
--base release/v1.0
gitcode pr sync --source-pr owner/source-repo#123 \
--target-repo owner/target-repo \
--title "[sync] Fix login bug" \
--body "Synced from owner/source-repo#123"
```

### `gitcode pr test`

Trigger or manage PR tests

`用法: gitcode pr test <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--force` | — | bool | false | Force test pass (admin only) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip force test pass confirmation |

**示例**

```bash
gitcode pr test 123 -R owner/repo
gitcode pr test 123 -R owner/repo --force
```

### `gitcode pr view`

View a pull request

`用法: gitcode pr view <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--comments` | `c` | bool | false | View comments |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--time-format` | — | string | absolute | Time format for dates (absolute/relative)（可选: absolute, relative） |
| `--web` | `w` | bool | false | Open in browser |

**示例**

```bash
gitcode pr view 123 -R owner/repo
gitcode pr view 123 -R owner/repo --web
gitcode pr view 123 -R owner/repo --time-format relative
```
