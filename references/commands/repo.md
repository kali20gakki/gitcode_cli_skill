# repo — 仓库、分支与保护规则命令

> 自动生成：`scripts/gen_references.py` ← `gitcode schema`（CLI 0.17.0）。请勿手工编辑；需要现场真值时用 `python scripts/gc_query.py "<命令路径>"`。

## 命令清单

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode repo archive` | Archive a repository | ✓ |
| `gitcode repo branch create` | Create a branch in a repository | ✓ |
| `gitcode repo branch list` | List branches in a repository | ✓ |
| `gitcode repo branch view` | View a branch in a repository | ✓ |
| `gitcode repo branch-protection create` | Create a branch protection rule | — |
| `gitcode repo branch-protection delete` | Delete a branch protection rule | — |
| `gitcode repo branch-protection list` | List branch protection rules | ✓ |
| `gitcode repo branch-protection update` | Update a branch protection rule | — |
| `gitcode repo clone` | Clone a repository locally | — |
| `gitcode repo create` | Create a new repository | ✓ |
| `gitcode repo delete` | Delete a repository | ✓ |
| `gitcode repo edit` | Edit repository settings | ✓ |
| `gitcode repo fork` | Fork a repository | ✓ |
| `gitcode repo list` | List repositories | ✓ |
| `gitcode repo log` | List repository commits | ✓ |
| `gitcode repo pr-settings update` | Update pull request settings | ✓ |
| `gitcode repo pr-settings view` | View pull request settings | ✓ |
| `gitcode repo set-default` | Set or view the default repository | ✓ |
| `gitcode repo stats` | Get code contribution statistics | ✓ |
| `gitcode repo sync` | Sync a local directory into another repository and create a PR | ✓ |
| `gitcode repo unarchive` | Unarchive a repository | ✓ |
| `gitcode repo view` | View a repository | ✓ |

## 命令组

### `gitcode repo`

Manage GitCode repositories

子命令: `archive`, `branch`, `branch-protection`, `clone`, `create`, `delete`, `edit`, `fork`, `list`, `log`, `pr-settings`, `set-default`, `stats`, `sync`, `unarchive`, `view`

### `gitcode repo branch`

Manage branches

子命令: `create`, `list`, `view`

### `gitcode repo branch-protection`

Manage branch protection rules

子命令: `create`, `delete`, `list`, `update`

### `gitcode repo pr-settings`

Manage pull request merge gate settings

子命令: `update`, `view`

## 详细参数

### `gitcode repo archive`

Archive a repository

`用法: gitcode repo archive <repository>`

参数: `<repository>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview without archiveing the repository |
| `--json` | — | bool | false | Output as JSON |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode repo archive owner/repo --yes
```

### `gitcode repo branch create`

Create a branch in a repository

`用法: gitcode repo branch create <branch-name>`

参数: `<branch-name>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--description` | — | string | — | Branch description |
| `--json` | — | bool | false | Output as JSON |
| `--ref` | — | string | — | Source branch or tag name (default: repository default branch) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode repo branch create feature -R owner/repo
gitcode repo branch create feature --ref develop -R owner/repo
gitcode repo branch create feature --description "feature branch" -R owner/repo
```

### `gitcode repo branch list`

List branches in a repository

`用法: gitcode repo branch list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of branches to list |
| `--page` | — | int | 0 | Page number |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode repo branch list -R owner/repo
gitcode repo branch list -R owner/repo --json
```

### `gitcode repo branch view`

View a branch in a repository

`用法: gitcode repo branch view <branch>`

参数: `<branch>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode repo branch view main -R owner/repo
gitcode repo branch view main
gitcode repo branch view main -R owner/repo --json
```

### `gitcode repo branch-protection create`

Create a branch protection rule

`用法: gitcode repo branch-protection create`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--merger` | — | string | — | Who can merge (roles/usernames, semicolon-separated) |
| `--pusher` | — | string | — | Who can push (roles/usernames, semicolon-separated) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--wildcard` | — | string | — | Branch name or wildcard pattern (e.g. main, release/*) |

**示例**

```bash
gitcode repo branch-protection create --wildcard "main" --pusher admin --merger admin -R owner/repo
gitcode repo branch-protection create --wildcard "release/*" --pusher "admin;user1" -R owner/repo
```

### `gitcode repo branch-protection delete`

Delete a branch protection rule

`用法: gitcode repo branch-protection delete <wildcard>`

参数: `<wildcard>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode repo branch-protection delete "main" -R owner/repo
```

### `gitcode repo branch-protection list`

List branch protection rules

`用法: gitcode repo branch-protection list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode repo branch-protection list -R owner/repo
```

### `gitcode repo branch-protection update`

Update a branch protection rule

`用法: gitcode repo branch-protection update <wildcard>`

参数: `<wildcard>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--merger` | — | string | — | Who can merge (roles/usernames) |
| `--pusher` | — | string | — | Who can push (roles/usernames) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode repo branch-protection update "main" --pusher develop -R owner/repo
```

### `gitcode repo clone`

Clone a repository locally

`用法: gitcode repo clone <repository> [<directory>]`

参数: `<repository>`（必填）, `<directory>`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--branch` | `b` | string | — | Branch to checkout |
| `--depth` | `d` | int | 0 | Create a shallow clone |
| `--git-protocol` | `p` | string | — | Git protocol to use (https/ssh, default: auth config)（可选: https, ssh） |
| `--recursive` | `r` | bool | false | Clone submodules |

**示例**

```bash
gitcode repo clone owner/repo
gitcode repo clone owner/repo my-project
gitcode repo clone owner/repo --git-protocol ssh
```

### `gitcode repo create`

Create a new repository

`用法: gitcode repo create <name>`

参数: `<name>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--description` | `d` | string | — | Description of the repository |
| `--json` | — | bool | false | Output as JSON |
| `--private` | `P` | bool | false | Make the repository private |
| `--public` | `p` | bool | false | Make the repository public |

**示例**

```bash
gitcode repo create my-repo --public
gitcode repo create my-repo --private
gitcode repo create my-repo --description "My project"
```

### `gitcode repo delete`

Delete a repository

`用法: gitcode repo delete <repository>`

参数: `<repository>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview the deletion without deleting the repository |
| `--json` | — | bool | false | Output as JSON |
| `--yes` | `y` | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode repo delete owner/repo
gitcode repo delete owner/repo --yes
gitcode repo delete owner/repo --yes --json
```

### `gitcode repo edit`

Edit repository settings

`用法: gitcode repo edit`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--default-branch` | — | string | — | Default branch |
| `--description` | — | string | — | Repository description |
| `--homepage` | — | string | — | Homepage URL |
| `--json` | — | bool | false | Output as JSON |
| `--name` | — | string | — | Repository name (rename) |
| `--private` | — | bool | false | Make repository private |
| `--public` | — | bool | false | Make repository public |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode repo edit --description "New description" -R owner/repo
gitcode repo edit --private -R owner/repo
gitcode repo edit --default-branch main -R owner/repo
```

### `gitcode repo fork`

Fork a repository

`用法: gitcode repo fork [<repository>]`

参数: `<repository>`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--clone` | `c` | bool | false | Clone the fork after creating |
| `--json` | — | bool | false | Output as JSON |

**示例**

```bash
gitcode repo fork owner/repo
gitcode repo fork owner/repo --clone
gitcode repo fork owner/repo --json
```

### `gitcode repo list`

List repositories

`用法: gitcode repo list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of repos to list |
| `--owner` | `o` | string | — | List repos for an organization |
| `--per-page` | — | int | 0 | API page size (default: --limit) |
| `--visibility` | `v` | string | — | Filter by visibility (public/private)（可选: public, private） |

**示例**

```bash
gitcode repo list
gitcode repo list --limit 50
gitcode repo list --visibility public
```

### `gitcode repo log`

List repository commits

`用法: gitcode repo log`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--branch` | `b` | string | — | Branch, tag, or commit SHA |
| `--file` | — | string | — | Filter commits that touched this file path |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of commits to list |
| `--page` | — | int | 1 | Page number to fetch |
| `--per-page` | — | int | 0 | API page size (default: --limit) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode repo log -R owner/repo
gitcode repo log -R owner/repo --file src/main.go --branch main
gitcode repo log -R owner/repo --file src/main.go --branch main --json
```

### `gitcode repo pr-settings update`

Update pull request settings

`用法: gitcode repo pr-settings update`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--close-issue-on-merge` | — | bool | false | Close the issues referenced by a merged pull request |
| `--delete-source-branch` | — | bool | false | Delete source branch on merge |
| `--force-merge` | — | bool | false | Allow admin force merge |
| `--json` | — | bool | false | Output as JSON |
| `--merge-method` | — | string | — | Merge method (merge/rebase_merge/ff) |
| `--no-self-merge` | — | bool | false | Disable merging own pull requests |
| `--pipeline-required` | — | bool | false | Require pipeline success before merge |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--reviewers` | — | int | 0 | Minimum number of reviewers (0 to disable) |

**示例**

```bash
gitcode repo pr-settings update --pipeline-required -R owner/repo
gitcode repo pr-settings update --reviewers 2 -R owner/repo
gitcode repo pr-settings update --no-self-merge -R owner/repo
```

### `gitcode repo pr-settings view`

View pull request settings

`用法: gitcode repo pr-settings view`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode repo pr-settings view -R owner/repo
gitcode repo pr-settings view -R owner/repo --json
```

### `gitcode repo set-default`

Set or view the default repository

`用法: gitcode repo set-default [<owner>/<repo>]`

参数: `<owner>/<repo>`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--unset` | — | bool | false | Clear the default repository |
| `--view` | — | bool | false | View the current default repository |

**示例**

```bash
gitcode repo set-default
gitcode repo set-default owner/repo
gitcode repo set-default --view
```

### `gitcode repo stats`

Get code contribution statistics

`用法: gitcode repo stats`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--author` | `a` | string | — | Filter by author username |
| `--branch` | `b` | string | main | **必填** Branch name (required) |
| `--json` | — | bool | false | Output as JSON |
| `--only-self` | — | bool | false | Only show your own stats |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--since` | — | string | — | Only commits after this date (YYYY-MM-DD) |
| `--until` | — | string | — | Only commits before this date (YYYY-MM-DD) |

**示例**

```bash
gitcode repo stats --branch main -R owner/repo
gitcode repo stats --branch main --author username -R owner/repo
gitcode repo stats --branch main --only-self -R owner/repo
```

### `gitcode repo sync`

Sync a local directory into another repository and create a PR

`用法: gitcode repo sync`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--base` | — | string | — | Base branch in the target repository (default: target default branch) |
| `--body` | — | string | — | Pull request body |
| `--branch` | — | string | — | Sync branch name in the target repository |
| `--commit-message` | — | string | — | Commit message for the sync commit |
| `--draft` | — | bool | false | Create the target pull request as draft |
| `--json` | — | bool | false | Output as JSON |
| `--source-dir` | — | string | — | **必填** Source directory in the current repository |
| `--target-dir` | — | string | — | **必填** Target directory inside the target repository |
| `--target-repo` | — | string | — | **必填** Target repository (owner/repo) |
| `--title` | — | string | — | Pull request title |
| `--yes` | — | bool | false | Skip confirmation prompt before pushing and creating the target PR |

**示例**

```bash
gitcode repo sync \
--target-repo infra-test/target-repo \
--source-dir docs/api \
--target-dir sync/api
gitcode repo sync \
--target-repo infra-test/target-repo \
--source-dir pkg/contracts \
--target-dir mirror/contracts \
--base main \
--title "sync: update contracts"
gitcode repo sync --target-repo owner/repo --source-dir src --target-dir dst --json
```

### `gitcode repo unarchive`

Unarchive a repository

`用法: gitcode repo unarchive <repository>`

参数: `<repository>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview without unarchiveing the repository |
| `--json` | — | bool | false | Output as JSON |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode repo unarchive owner/repo --yes
```

### `gitcode repo view`

View a repository

`用法: gitcode repo view [<repository>]`

参数: `<repository>`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--web` | `w` | bool | false | Open in browser |

**示例**

```bash
gitcode repo view owner/repo
gitcode repo view
gitcode repo view owner/repo --web
```
