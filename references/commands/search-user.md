# search / user / discussions — 发现与协作命令

> 自动生成：`scripts/gen_references.py` ← `gitcode schema`（CLI 0.17.0）。请勿手工编辑；需要现场真值时用 `python scripts/gc_query.py "<命令路径>"`。

## 命令清单

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode discussions comments create` | Create a comment on an organization discussion | ✓ |
| `gitcode discussions comments delete` | Delete a comment on an organization discussion | — |
| `gitcode discussions comments edit` | Edit a comment on an organization discussion | ✓ |
| `gitcode discussions comments list` | List organization discussion comments | ✓ |
| `gitcode discussions comments replies` | List replies to an organization discussion comment | ✓ |
| `gitcode discussions comments reply` | Reply to a comment on an organization discussion | ✓ |
| `gitcode discussions create` | Create an organization discussion | ✓ |
| `gitcode discussions delete` | Delete an organization discussion | — |
| `gitcode discussions edit` | Edit an organization discussion | ✓ |
| `gitcode discussions list` | List organization discussions | ✓ |
| `gitcode discussions project comments create` | Create a comment on a repository discussion | ✓ |
| `gitcode discussions project comments edit` | Edit a comment on a repository discussion | ✓ |
| `gitcode discussions project comments list` | List repository discussion comments | ✓ |
| `gitcode discussions project comments replies` | List replies to a repository discussion comment | ✓ |
| `gitcode discussions project comments reply` | Reply to a comment on a repository discussion | ✓ |
| `gitcode discussions project create` | Create a repository discussion | ✓ |
| `gitcode discussions project delete` | Delete a repository discussion | — |
| `gitcode discussions project edit` | Edit a repository discussion | ✓ |
| `gitcode discussions project list` | List repository discussions | ✓ |
| `gitcode discussions project view` | View a repository discussion | ✓ |
| `gitcode discussions view` | View an organization discussion | ✓ |
| `gitcode search issues` | Search for issues | ✓ |
| `gitcode search repos` | Search for repositories | ✓ |
| `gitcode search users` | Search for users | ✓ |
| `gitcode user edit` | Edit your user profile | ✓ |
| `gitcode user view` | View a user profile | ✓ |

## 命令组

### `gitcode discussions`

Manage organization discussions

子命令: `comments`, `create`, `delete`, `edit`, `list`, `project`, `view`

### `gitcode discussions comments`

Manage organization discussion comments and replies

子命令: `create`, `delete`, `edit`, `list`, `replies`, `reply`

### `gitcode discussions project`

Manage repository discussions

子命令: `comments`, `create`, `delete`, `edit`, `list`, `view`

### `gitcode discussions project comments`

Manage repository discussion comments and replies

子命令: `create`, `edit`, `list`, `replies`, `reply`

### `gitcode search`

Search for repositories, issues, and users

子命令: `issues`, `repos`, `users`

### `gitcode user`

View and edit user profile

子命令: `edit`, `view`

## 详细参数

### `gitcode discussions comments create`

Create a comment on an organization discussion

`用法: gitcode discussions comments create <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | Comment body (required) |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | **必填** Organization path (required) |

**示例**

```bash
gitcode discussions comments create 42 --org my-org --body "Great idea!"
gitcode discussions comments create 42 --org my-org --body-file comment.md
echo "Comment text" | gitcode discussions comments create 42 --org my-org --body-file -
```

### `gitcode discussions comments delete`

Delete a comment on an organization discussion

`用法: gitcode discussions comments delete <number> <comment-id>`

参数: `<number>`（必填）, `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode discussions comments delete 42 123 --org my-org
gitcode discussions comments delete 42 123 --org my-org --yes
```

### `gitcode discussions comments edit`

Edit a comment on an organization discussion

`用法: gitcode discussions comments edit <number> <comment-id>`

参数: `<number>`（必填）, `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | New comment body (required) |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | **必填** Organization path (required) |

**示例**

```bash
gitcode discussions comments edit 42 <comment-id> --org my-org --body "Updated text"
gitcode discussions comments edit 42 <comment-id> --org my-org --body-file comment.md
echo "Updated text" | gitcode discussions comments edit 42 <comment-id> --org my-org --body-file -
```

### `gitcode discussions comments list`

List organization discussion comments

`用法: gitcode discussions comments list <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--order` | — | string | — | Sort: time_asc, time_desc, hot_desc |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--page` | — | int | 0 | Page number (1-based) |
| `--per-page` | — | int | 0 | Page size (max 100, default 20) |

**示例**

```bash
gitcode discussions comments list 42 --org my-org
gitcode discussions comments list 42 --org my-org --order hot_desc --json
```

### `gitcode discussions comments replies`

List replies to an organization discussion comment

`用法: gitcode discussions comments replies <number> <comment-id>`

参数: `<number>`（必填）, `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--page` | — | int | 0 | Page number (1-based) |
| `--per-page` | — | int | 0 | Page size (max 100, default 20) |

**示例**

```bash
gitcode discussions comments replies 42 <comment-id> --org my-org
```

### `gitcode discussions comments reply`

Reply to a comment on an organization discussion

`用法: gitcode discussions comments reply <number> <comment-id>`

参数: `<number>`（必填）, `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | Reply body (required) |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | **必填** Organization path (required) |

**示例**

```bash
gitcode discussions comments reply 42 <comment-id> --org my-org --body "Reply text"
gitcode discussions comments reply 42 <comment-id> --org my-org --body-file reply.md
echo "Reply text" | gitcode discussions comments reply 42 <comment-id> --org my-org --body-file -
```

### `gitcode discussions create`

Create an organization discussion

`用法: gitcode discussions create`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | Discussion body (required) |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--category` | — | string | — | Discussion category name (required) |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--title` | `t` | string | — | Discussion title (required) |

**示例**

```bash
gitcode discussions create --org my-org --title "New idea" --category "Ideas" --body "Description"
gitcode discussions create --org my-org --title "New idea" --category "Ideas" --body-file idea.md
cat idea.md | gitcode discussions create --org my-org --title "New idea" --category "Ideas" --body-file -
```

### `gitcode discussions delete`

Delete an organization discussion

`用法: gitcode discussions delete <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode discussions delete 42 --org my-org
gitcode discussions delete 42 --org my-org --yes
```

### `gitcode discussions edit`

Edit an organization discussion

`用法: gitcode discussions edit <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | New discussion body |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--category` | — | string | — | New discussion category name |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--title` | `t` | string | — | New discussion title |

**示例**

```bash
gitcode discussions edit 42 --org my-org --title "Updated title"
gitcode discussions edit 42 --org my-org --body-file idea.md
gitcode discussions edit 42 --org my-org --category "Q&A"
```

### `gitcode discussions list`

List organization discussions

`用法: gitcode discussions list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--direction` | — | string | — | Sort direction: asc or desc (default desc) |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of discussions to list |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--page` | — | int | 0 | Page number (1-based) |
| `--per-page` | — | int | 0 | Page size (max 100, default 20) |
| `--search` | — | string | — | Filter by title/description |
| `--sort` | — | string | — | Sort field: created (default) or comment_size |

**示例**

```bash
gitcode discussions list --org my-org
gitcode discussions list --org my-org --search "release plan"
gitcode discussions list --org my-org --sort comment_size --direction desc
```

### `gitcode discussions project comments create`

Create a comment on a repository discussion

`用法: gitcode discussions project comments create <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | Comment body (required) |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode discussions project comments create 42 -R owner/repo --body "Great idea!"
gitcode discussions project comments create 42 -R owner/repo --body-file comment.md
echo "Comment text" | gitcode discussions project comments create 42 -R owner/repo --body-file -
```

### `gitcode discussions project comments edit`

Edit a comment on a repository discussion

`用法: gitcode discussions project comments edit <number> <comment-id>`

参数: `<number>`（必填）, `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | New comment body (required) |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode discussions project comments edit 42 <comment-id> -R owner/repo --body "Updated text"
gitcode discussions project comments edit 42 <comment-id> -R owner/repo --body-file comment.md
echo "Updated text" | gitcode discussions project comments edit 42 <comment-id> -R owner/repo --body-file -
```

### `gitcode discussions project comments list`

List repository discussion comments

`用法: gitcode discussions project comments list <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--order` | — | string | — | Sort: time_asc, time_desc, hot_desc |
| `--page` | — | int | 0 | Page number (1-based) |
| `--per-page` | — | int | 0 | Page size (max 100, default 20) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode discussions project comments list 42 -R owner/repo
```

### `gitcode discussions project comments replies`

List replies to a repository discussion comment

`用法: gitcode discussions project comments replies <number> <comment-id>`

参数: `<number>`（必填）, `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--page` | — | int | 0 | Page number (1-based) |
| `--per-page` | — | int | 0 | Page size (max 100, default 20) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode discussions project comments replies 42 <comment-id> -R owner/repo
```

### `gitcode discussions project comments reply`

Reply to a comment on a repository discussion

`用法: gitcode discussions project comments reply <number> <comment-id>`

参数: `<number>`（必填）, `<comment-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | Reply body (required) |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode discussions project comments reply 42 <comment-id> -R owner/repo --body "Reply text"
gitcode discussions project comments reply 42 <comment-id> -R owner/repo --body-file reply.md
echo "Reply text" | gitcode discussions project comments reply 42 <comment-id> -R owner/repo --body-file -
```

### `gitcode discussions project create`

Create a repository discussion

`用法: gitcode discussions project create`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | Discussion body (required) |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--category` | — | string | — | Discussion category name (required) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--title` | `t` | string | — | Discussion title (required) |

**示例**

```bash
gitcode discussions project create -R owner/repo --title "New idea" --category "Ideas" --body "Description"
gitcode discussions project create -R owner/repo --title "New idea" --category "Ideas" --body-file idea.md
cat idea.md | gitcode discussions project create -R owner/repo --title "New idea" --category "Ideas" --body-file -
```

### `gitcode discussions project delete`

Delete a repository discussion

`用法: gitcode discussions project delete <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode discussions project delete 42 -R owner/repo
gitcode discussions project delete 42 -R owner/repo --yes
```

### `gitcode discussions project edit`

Edit a repository discussion

`用法: gitcode discussions project edit <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | New discussion body |
| `--body-file` | `F` | string | — | Read body from file (use - for stdin) |
| `--category` | — | string | — | New discussion category name |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--title` | `t` | string | — | New discussion title |

**示例**

```bash
gitcode discussions project edit 42 -R owner/repo --title "Updated title"
gitcode discussions project edit 42 -R owner/repo --body-file idea.md
gitcode discussions project edit 42 -R owner/repo --category "Q&A"
```

### `gitcode discussions project list`

List repository discussions

`用法: gitcode discussions project list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--direction` | — | string | — | Sort direction: asc or desc (default desc) |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of discussions to list |
| `--page` | — | int | 0 | Page number (1-based) |
| `--per-page` | — | int | 0 | Page size (max 100, default 20) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--search` | — | string | — | Filter by title/description |
| `--sort` | — | string | — | Sort field: created (default) or comment_size |

**示例**

```bash
gitcode discussions project list -R owner/repo
gitcode discussions project list -R owner/repo --search "release plan"
gitcode discussions project list -R owner/repo --sort comment_size --direction desc
```

### `gitcode discussions project view`

View a repository discussion

`用法: gitcode discussions project view <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode discussions project view 42 -R owner/repo
gitcode discussions project view 42 -R owner/repo --json
```

### `gitcode discussions view`

View an organization discussion

`用法: gitcode discussions view <number>`

参数: `<number>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | **必填** Organization path (required) |

**示例**

```bash
gitcode discussions view 42 --org my-org
gitcode discussions view 42 --org my-org --json
```

### `gitcode search issues`

Search for issues

`用法: gitcode search issues <query>`

参数: `<query>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum results per page |
| `--page` | — | int | 0 | Page number |
| `--repo` | `R` | string | — | Limit search to a repository (owner/repo) |
| `--state` | — | string | — | Filter by state (open/closed) |

**示例**

```bash
gitcode search issues "bug report"
gitcode search issues "feature" --repo owner/repo --state open
```

### `gitcode search repos`

Search for repositories

`用法: gitcode search repos <query>`

参数: `<query>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum results per page |
| `--page` | — | int | 0 | Page number |

**示例**

```bash
gitcode search repos "gitcode"
gitcode search repos "cli tool" --json
```

### `gitcode search users`

Search for users

`用法: gitcode search users <query>`

参数: `<query>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum results per page |
| `--page` | — | int | 0 | Page number |

**示例**

```bash
gitcode search users "developer"
gitcode search users "admin" --json
```

### `gitcode user edit`

Edit your user profile

`用法: gitcode user edit`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--bio` | — | string | — | Bio / description |
| `--company` | — | string | — | Company |
| `--email` | — | string | — | Public email |
| `--json` | — | bool | false | Output as JSON |
| `--location` | — | string | — | Location |
| `--name` | — | string | — | Display name |
| `--website` | — | string | — | Website URL |

**示例**

```bash
gitcode user edit --name "New Name"
gitcode user edit --bio "New bio" --company "Acme Inc"
```

### `gitcode user view`

View a user profile

`用法: gitcode user view [<username>]`

参数: `<username>`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

**示例**

```bash
gitcode user view
gitcode user view <username>
gitcode user view --json
```
