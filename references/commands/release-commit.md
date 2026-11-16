# release / commit — 发布与提交命令

> 自动生成：`scripts/gen_references.py` ← `gitcode schema`（CLI 0.17.0）。请勿手工编辑；需要现场真值时用 `python scripts/gc_query.py "<命令路径>"`。

## 命令清单

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode commit comments create` | Create a comment on a commit | — |
| `gitcode commit comments edit` | Edit a commit comment | — |
| `gitcode commit comments list` | List commit comments | ✓ |
| `gitcode commit comments list-by-sha` | List comments for a specific commit | ✓ |
| `gitcode commit comments view` | View a commit comment | ✓ |
| `gitcode commit diff` | Get commit diff | — |
| `gitcode commit patch` | Get commit patch | — |
| `gitcode commit view` | View a commit | ✓ |
| `gitcode release create` | Create a new release | ✓ |
| `gitcode release delete` | Delete a release | — |
| `gitcode release delete-asset` | Delete a release asset | — |
| `gitcode release download` | Download release assets | — |
| `gitcode release edit` | Edit a release | ✓ |
| `gitcode release list` | List releases | ✓ |
| `gitcode release upload` | Upload assets to a release | ✓ |
| `gitcode release view` | View release details | ✓ |

## 命令组

### `gitcode commit`

Manage commits

子命令: `comments`, `diff`, `patch`, `view`

### `gitcode commit comments`

Manage commit comments

子命令: `create`, `edit`, `list`, `list-by-sha`, `view`

### `gitcode release`

Manage releases

子命令: `create`, `delete`, `delete-asset`, `download`, `edit`, `list`, `upload`, `view`

## 详细参数

### `gitcode commit comments create`

Create a comment on a commit

`用法: gitcode commit comments create <sha>`

参数: `<sha>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | **必填** Comment body (required) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode commit comments create abc123 --body "Nice work!" -R owner/repo
```

### `gitcode commit comments edit`

Edit a commit comment

`用法: gitcode commit comments edit <id>`

参数: `<id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--body` | `b` | string | — | **必填** New comment body (required) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode commit comments edit 123 --body "Updated text" -R owner/repo
```

### `gitcode commit comments list`

List commit comments

`用法: gitcode commit comments list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--order` | — | string | — | Sort order: asc or desc（可选: asc, desc） |
| `--page` | `p` | int | 1 | Page number |
| `--per-page` | `P` | int | 20 | Results per page (max 100) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode commit comments list -R owner/repo
gitcode commit comments list -R owner/repo --page 1 --per-page 50
gitcode commit comments list -R owner/repo --json
```

### `gitcode commit comments list-by-sha`

List comments for a specific commit

`用法: gitcode commit comments list-by-sha <sha>`

参数: `<sha>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--page` | `p` | int | 1 | Page number |
| `--per-page` | `P` | int | 20 | Results per page (max 100) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode commit comments list-by-sha abc123 -R owner/repo
gitcode commit comments list-by-sha abc123 -R owner/repo --page 1 --per-page 50
gitcode commit comments list-by-sha abc123 -R owner/repo --json
```

### `gitcode commit comments view`

View a commit comment

`用法: gitcode commit comments view <id>`

参数: `<id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode commit comments view 123 -R owner/repo
gitcode commit comments view 123 -R owner/repo --json
```

### `gitcode commit diff`

Get commit diff

`用法: gitcode commit diff <sha>`

参数: `<sha>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode commit diff abc123 -R owner/repo
```

### `gitcode commit patch`

Get commit patch

`用法: gitcode commit patch <sha>`

参数: `<sha>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode commit patch abc123 -R owner/repo
```

### `gitcode commit view`

View a commit

`用法: gitcode commit view <sha>`

参数: `<sha>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--show-diff` | — | bool | false | Show diff files |
| `--web` | `w` | bool | false | Open in browser |

**示例**

```bash
gitcode commit view abc123 -R owner/repo
gitcode commit view abc123 -R owner/repo --show-diff
gitcode commit view abc123 -R owner/repo --web
```

### `gitcode release create`

Create a new release

`用法: gitcode release create <tag>`

参数: `<tag>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--draft` | `d` | bool | false | Mark as draft (currently unsupported by GitCode release create API) |
| `--json` | — | bool | false | Output as JSON |
| `--notes` | `n` | string | — | Release notes |
| `--notes-file` | `F` | string | — | Read release notes from file |
| `--prerelease` | `p` | bool | false | Mark as prerelease |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--target` | — | string | — | Target commitish |
| `--title` | `t` | string | — | Release title |

**示例**

```bash
gitcode release create v1.0.0 -R owner/repo
gitcode release create v1.0.0 -R owner/repo --title "Version 1.0" --notes "Release notes"
gitcode release create v1.0.0 -R owner/repo --notes-file CHANGELOG.md
```

### `gitcode release delete`

Delete a release

`用法: gitcode release delete <tag>`

参数: `<tag>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview the deletion without deleting the release |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode release delete v1.0.0 -R owner/repo --dry-run
gitcode release delete v1.0.0 -R owner/repo --yes
```

### `gitcode release delete-asset`

Delete a release asset

`用法: gitcode release delete-asset <tag> <asset-id>`

参数: `<tag>`（必填）, `<asset-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview the deletion without deleting the asset |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode release delete-asset v1.0.0 12345 -R owner/repo
gitcode release delete-asset v1.0.0 12345 -R owner/repo --yes
gitcode release delete-asset v1.0.0 12345 -R owner/repo --dry-run
```

### `gitcode release download`

Download release assets

`用法: gitcode release download [<tag>] [asset]`

参数: `<tag>`, `asset`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--all` | `A` | bool | false | Download source archives as well |
| `--clobber` | — | bool | false | Overwrite existing files |
| `--output` | `o` | string | . | Output directory |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--skip-existing` | — | bool | false | Skip downloading when a file of the same name exists |

**示例**

```bash
gitcode release download -R owner/repo
gitcode release download v1.0.0 -R owner/repo
gitcode release download v1.0.0 app.zip -R owner/repo
```

### `gitcode release edit`

Edit a release

`用法: gitcode release edit <tag>`

参数: `<tag>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--draft` | — | string | — | Mark as draft (true/false) |
| `--json` | — | bool | false | Output as JSON |
| `--notes` | `n` | string | — | Release notes |
| `--notes-file` | `F` | string | — | Read release notes from file |
| `--prerelease` | — | string | — | Mark as prerelease (true/false) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--target` | `T` | string | — | Target branch or commit SHA |
| `--title` | `t` | string | — | Release title |

**示例**

```bash
gitcode release edit v1.0.0 -R owner/repo --title "New Title" --notes "New notes"
gitcode release edit v1.0.0 -R owner/repo --prerelease true
gitcode release edit v1.0.0 -R owner/repo --prerelease false
```

### `gitcode release list`

List releases

`用法: gitcode release list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of releases to list (fetched across API pages when greater than 100) |
| `--page` | — | int | 0 | Page number to fetch (single request; the API returns at most 100 per page) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode release list -R owner/repo
gitcode release list -R owner/repo --limit 10
gitcode release list -R owner/repo --limit 150
```

### `gitcode release upload`

Upload assets to a release

`用法: gitcode release upload <tag> <file>...`

参数: `<tag>`（必填）, `<file>`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--label` | `l` | string | — | Asset label |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode release upload v1.0.0 app.zip -R owner/repo
gitcode release upload v1.0.0 app.zip checksum.txt -R owner/repo
gitcode release upload v1.0.0 app.zip -R owner/repo
```

### `gitcode release view`

View release details

`用法: gitcode release view <tag>`

参数: `<tag>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--web` | `w` | bool | false | Open in browser |

**示例**

```bash
gitcode release view v1.0.0 -R owner/repo
gitcode release view v1.0.0 -R owner/repo --web
gitcode release view v1.0.0 -R owner/repo --json
```
