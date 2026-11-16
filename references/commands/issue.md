# issue / label / milestone — 议题与元数据命令

> 自动生成：`scripts/gen_references.py` ← `gitcode schema`（CLI 0.17.0）。请勿手工编辑；需要现场真值时用 `python scripts/gc_query.py "<命令路径>"`。

## 命令清单

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode issue close` | Close an issue | ✓ |
| `gitcode issue comment edit` | Edit an issue comment | — |
| `gitcode issue comments` | List comments on an issue | ✓ |
| `gitcode issue create` | Create a new issue | ✓ |
| `gitcode issue edit` | Edit an issue | ✓ |
| `gitcode issue label` | Manage labels on an issue | ✓ |
| `gitcode issue list` | List issues in a repository | ✓ |
| `gitcode issue prs` | List Pull Requests associated with an issue | ✓ |
| `gitcode issue relations` | List issue and pull request relations in a repository | ✓ |
| `gitcode issue reopen` | Reopen a closed issue | ✓ |
| `gitcode issue view` | View an issue | ✓ |
| `gitcode label create` | Create a label | ✓ |
| `gitcode label delete` | Delete a label | ✓ |
| `gitcode label edit` | Edit a label | ✓ |
| `gitcode label list` | List labels | ✓ |
| `gitcode milestone create` | Create a milestone | ✓ |
| `gitcode milestone delete` | Delete a milestone | — |
| `gitcode milestone edit` | Edit a milestone | ✓ |
| `gitcode milestone list` | List milestones | ✓ |
| `gitcode milestone view` | View a milestone | ✓ |

## 命令组

### `gitcode issue`

Manage issues

子命令: `close`, `comment`, `comments`, `create`, `edit`, `label`, `list`, `prs`, `relations`, `reopen`, `view`

### `gitcode issue comment`

Add a comment to an issue

子命令: `edit`

### `gitcode label`

Manage labels

子命令: `create`, `delete`, `edit`, `list`

### `gitcode milestone`

Manage milestones

子命令: `create`, `delete`, `edit`, `list`, `view`

## 详细参数

### `gitcode issue close`

Close an issue

`用法: gitcode issue close <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--comment` | `c` | string | — | Add a comment before closing |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode issue close 123
gitcode issue close 123 --comment "Fixed in PR #456"
gitcode issue close 123 -R owner/repo --yes
```

### `gitcode issue comment edit`

Edit an issue comment

`用法: gitcode issue comment edit [id]`

参数: `id`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | New comment body |
| `--body-file` | `F` | string | — | Read comment body from file (use - for stdin) |
| `--id` | — | string | — | Issue comment ID |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode issue comment edit 12345 -R owner/repo --body "Updated comment"
gitcode issue comment edit --id 12345 -R owner/repo --body "Updated comment"
gitcode issue comment edit 12345 -R owner/repo --body-file comment.md
```

### `gitcode issue comments`

List comments on an issue

`用法: gitcode issue comments <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 0 | Maximum number of comments to list (0 = all) |
| `--order` | — | string | asc | Sort order (asc/desc)（可选: asc, desc） |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--since` | — | string | — | Filter comments updated after this time (ISO 8601 format) |

**示例**

```bash
gitcode issue comments 123 -R owner/repo
gitcode issue comments 123 -R owner/repo --limit 10
gitcode issue comments 123 -R owner/repo --order desc
```

### `gitcode issue create`

Create a new issue

`用法: gitcode issue create`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--assignee` | `a` | stringSlice | [] | Assignees |
| `--body` | `b` | string | — | Body for the issue |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--custom-fields-file` | — | string | — | Read custom fields JSON array from file |
| `--custom-fields-json` | — | string | — | Custom fields JSON array |
| `--dry-run` | — | bool | false | Preview the create request without creating the issue |
| `--issue-severity` | — | string | — | Issue severity (enterprise) |
| `--issue-type` | — | string | — | Issue type (enterprise) |
| `--json` | — | bool | false | Output as JSON |
| `--label` | `l` | stringSlice | [] | Labels to add |
| `--milestone` | `m` | int | 0 | Milestone number |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--security-hole` | — | bool | false | Mark as private issue |
| `--template-path` | — | string | — | Issue template path |
| `--title` | `t` | string | — | Title for the issue |

**示例**

```bash
gitcode issue create -R owner/repo --title "Bug" --body "Description"
gitcode issue create -R owner/repo --title "Feature" --label bug,enhancement
gitcode issue create -R owner/repo --title "Bug"
```

### `gitcode issue edit`

Edit an issue

`用法: gitcode issue edit <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--assignee` | `a` | stringSlice | [] | Assignees (comma-separated) |
| `--body` | `b` | string | — | New body/description |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--json` | — | bool | false | Output as JSON |
| `--label` | `l` | stringSlice | [] | Labels (comma-separated) |
| `--milestone` | `m` | int | 0 | Milestone number |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--security-hole` | — | bool | false | Mark as private issue |
| `--state` | `s` | string | — | State: open, closed, reopen, close（可选: open, closed, reopen, close） |
| `--title` | `t` | string | — | New title |
| `--yes` | `y` | bool | false | Skip confirmation for state changes |

**示例**

```bash
gitcode issue edit 123 --title "New title" -R owner/repo
gitcode issue edit 123 --body "New description" -R owner/repo
gitcode issue edit 123 --state close -R owner/repo
```

### `gitcode issue label`

Manage labels on an issue

`用法: gitcode issue label <number>`

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
gitcode issue label 123 --add bug,enhancement -R owner/repo
gitcode issue label 123 --remove bug -R owner/repo
gitcode issue label 123 --remove triage --add verified,in-progress -R owner/repo
```

### `gitcode issue list`

List issues in a repository

`用法: gitcode issue list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--assignee` | `a` | string | — | Filter by assignee username |
| `--created-after` | — | string | — | Filter issues created after this time |
| `--created-before` | — | string | — | Filter issues created before this time |
| `--creator` | — | string | — | Filter by creator username |
| `--direction` | — | string | desc | Sort direction (asc/desc)（可选: asc, desc） |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--json` | — | bool | false | Output as JSON |
| `--label` | `l` | string | — | Filter by labels (comma separated) |
| `--limit` | `L` | int | 30 | Maximum number of issues to list |
| `--milestone` | `m` | string | — | Filter by milestone title or number |
| `--page` | — | int | 0 | Page number for pagination |
| `--per-page` | — | int | 0 | API page size (default: --limit) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--search` | — | string | — | Search by keyword in title or body |
| `--since` | — | string | — | Filter by update time (ISO 8601 format) |
| `--sort` | — | string | created | Sort by (created/updated)（可选: created, updated） |
| `--state` | `s` | string | open | Filter by state (open/closed/all)（可选: open, closed, all） |
| `--template` | — | string | — | Format output using a Go template |
| `--time-format` | — | string | — | Time format (absolute/relative)（可选: absolute, relative） |
| `--updated-after` | — | string | — | Filter issues updated after this time |
| `--updated-before` | — | string | — | Filter issues updated before this time |

**示例**

```bash
gitcode issue list
gitcode issue list --state closed
gitcode issue list --label bug,enhancement
```

### `gitcode issue prs`

List Pull Requests associated with an issue

`用法: gitcode issue prs <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--mode` | — | int | 0 | Mode: 0 (default), 1 (enhanced with mergeable status) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode issue prs 123 -R owner/repo
gitcode issue prs 123 --mode 1 -R owner/repo
gitcode issue prs 123 -R owner/repo --json
```

### `gitcode issue relations`

List issue and pull request relations in a repository

`用法: gitcode issue relations`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 100 | Maximum number of issues to inspect |
| `--mode` | — | int | 1 | Issue PR lookup mode: 0 (default), 1 (enhanced with mergeable status) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--state` | `s` | string | all | Filter source issues by state (open/closed/all)（可选: open, closed, all） |

**示例**

```bash
gitcode issue relations -R owner/repo
gitcode issue relations -R owner/repo --json
gitcode issue relations -R owner/repo --state open --limit 50
```

### `gitcode issue reopen`

Reopen a closed issue

`用法: gitcode issue reopen <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--comment` | `c` | string | — | Add a comment before reopening |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode issue reopen 123
gitcode issue reopen 123 --comment "Still reproduces on latest version"
gitcode issue reopen 123 -R owner/repo --yes
```

### `gitcode issue view`

View an issue

`用法: gitcode issue view <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--comments` | `c` | bool | false | View issue comments |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--time-format` | — | string | absolute | Time format for dates (absolute/relative)（可选: absolute, relative） |
| `--web` | `w` | bool | false | Open in browser |

**示例**

```bash
gitcode issue view 123
gitcode issue view 123 --comments
gitcode issue view 123 --time-format relative
```

### `gitcode label create`

Create a label

`用法: gitcode label create <name>`

参数: `<name>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--color` | `c` | string | #ededed | Color in hex format |
| `--description` | `d` | string | — | Description |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode label create bug --color "#ff0000" -R owner/repo
gitcode label create enhancement --color "#00ff00" --description "New features" -R owner/repo
gitcode label create bug --color "#ff0000" --json -R owner/repo
```

### `gitcode label delete`

Delete a label

`用法: gitcode label delete <name>`

参数: `<name>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview the deletion without deleting the label |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode label delete old-label -R owner/repo
gitcode label delete old-label --yes -R owner/repo
gitcode label delete old-label --yes --json -R owner/repo
```

### `gitcode label edit`

Edit a label

`用法: gitcode label edit <name>`

参数: `<name>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--color` | `c` | string | — | New color in hex format (e.g., #ff0000) |
| `--json` | — | bool | false | Output as JSON |
| `--new-name` | — | string | — | New name for the label |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode label edit bug --new-name "bug-fix" -R owner/repo
gitcode label edit bug --color "#ff0000" -R owner/repo
gitcode label edit bug --color "#ff0000" --json -R owner/repo
```

### `gitcode label list`

List labels

`用法: gitcode label list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of labels to list |
| `--page` | — | int | 1 | Page number |
| `--per-page` | — | int | 0 | API page size (default: --limit) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode label list -R owner/repo
gitcode label list -R owner/repo --limit 50 --page 2
gitcode label list -R owner/repo --json
```

### `gitcode milestone create`

Create a milestone

`用法: gitcode milestone create <title>`

参数: `<title>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--description` | `d` | string | — | Description |
| `--due-date` | `D` | string | — | Due date (YYYY-MM-DD) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode milestone create "v1.0" -R owner/repo
gitcode milestone create "v1.0" --due-date "2024-12-31" -R owner/repo
gitcode milestone create "v2.0" --description "Next release" --due-date "2025-01-31" -R owner/repo
```

### `gitcode milestone delete`

Delete a milestone

`用法: gitcode milestone delete <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview the deletion without deleting the milestone |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode milestone delete 1 -R owner/repo
gitcode milestone delete 1 --yes -R owner/repo
```

### `gitcode milestone edit`

Edit a milestone

`用法: gitcode milestone edit <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--description` | `d` | string | — | New description |
| `--description-file` | `F` | string | — | Read description from file |
| `--due-date` | `D` | string | — | Due date (YYYY-MM-DD) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--state` | `s` | string | — | Milestone state (open/closed)（可选: open, closed） |
| `--title` | `t` | string | — | New milestone title |
| `--yes` | `y` | bool | false | Skip confirmation for state changes |

**示例**

```bash
gitcode milestone edit 5 --title "New Title" -R owner/repo
gitcode milestone edit 5 --description "Updated description" -R owner/repo
gitcode milestone edit 5 --description-file milestone-desc.md -R owner/repo
```

### `gitcode milestone list`

List milestones

`用法: gitcode milestone list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of milestones to list |
| `--page` | — | int | 1 | Page number |
| `--per-page` | — | int | 0 | API page size (default: --limit) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode milestone list -R owner/repo
gitcode milestone list -R owner/repo --limit 50 --page 2
gitcode milestone list -R owner/repo --json
```

### `gitcode milestone view`

View a milestone

`用法: gitcode milestone view <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--issues` | — | bool | true | Show associated issues |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--web` | `w` | bool | false | Open in browser |

**示例**

```bash
gitcode milestone view 1 -R owner/repo
gitcode milestone view 1 -R owner/repo --json
```
