# api / auth / config / doctor 等通用命令

> 自动生成：`scripts/gen_references.py` ← `gitcode schema`（CLI 0.17.0）。请勿手工编辑；需要现场真值时用 `python scripts/gc_query.py "<命令路径>"`。

## 命令清单

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode api` | Make an authenticated GitCode REST API request | — |
| `gitcode auth git-credential` | Provide stored GitCode credentials to git (helper protocol) | — |
| `gitcode auth login` | Log in to a GitCode account | — |
| `gitcode auth logout` | Log out of a GitCode account | — |
| `gitcode auth setup-git` | Configure git to use gc as a credential helper | — |
| `gitcode auth status` | View authentication status | ✓ |
| `gitcode auth token` | Print an authentication token | ✓ |
| `gitcode browse` | Open a GitCode repository in the browser | — |
| `gitcode config clear-cache` | Clear CLI cache | — |
| `gitcode config get` | Read a configuration value | ✓ |
| `gitcode config list` | List all configuration values | ✓ |
| `gitcode config set` | Store a configuration value | ✓ |
| `gitcode doctor install` | Inspect installation source and command conflicts | ✓ |
| `gitcode lark auth status` | Show lark-cli login status | ✓ |
| `gitcode lark config get` | Show the effective default Feishu/Lark chat id | ✓ |
| `gitcode lark config set` | Set the default Feishu/Lark chat id | — |
| `gitcode lark doctor` | Check lark-cli installation and login readiness | ✓ |
| `gitcode lark install` | Install the official lark-cli tool | — |
| `gitcode lark send` | Send a message to a Feishu/Lark chat or direct message | ✓ |
| `gitcode precommit check` | Check pre-commit configuration before committing or pushing | ✓ |
| `gitcode schema` | Print machine-readable command metadata | — |
| `gitcode ssh-key add` | Add an SSH public key | ✓ |
| `gitcode ssh-key delete` | Delete an SSH public key | ✓ |
| `gitcode ssh-key list` | List SSH public keys | ✓ |
| `gitcode ssh-key view` | View an SSH public key | ✓ |
| `gitcode update` | Check for or apply an installation-channel update | ✓ |
| `gitcode version` | Print gitcode version | ✓ |

## 命令组

### `gitcode auth`

Authenticate with GitCode

子命令: `git-credential`, `login`, `logout`, `setup-git`, `status`, `token`

### `gitcode config`

Read and write GitCode CLI configuration

子命令: `clear-cache`, `get`, `list`, `set`

### `gitcode doctor`

Diagnose the local GitCode CLI installation

子命令: `install`

### `gitcode lark`

Send messages and manage Feishu/Lark integration via lark-cli

子命令: `auth`, `config`, `doctor`, `install`, `send`

### `gitcode lark auth`

Show lark-cli login status

子命令: `status`

### `gitcode lark config`

Manage gc-lark integration settings (default chat)

子命令: `get`, `set`

### `gitcode precommit`

Work with pre-commit configuration and hooks

子命令: `check`

### `gitcode ssh-key`

Manage SSH public keys

子命令: `add`, `delete`, `list`, `view`

## 详细参数

### `gitcode api`

Make an authenticated GitCode REST API request

`用法: gitcode api <endpoint>`

参数: `<endpoint>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--field` | `f` | stringArray | [] | Add a key=value string field; fields are sent as a JSON request body |
| `--header` | `H` | stringArray | [] | Additional HTTP header (Name: value) |
| `--include` | — | bool | false | Include the response status line and headers in the output |
| `--input` | — | string | — | Read request body from file (use - for stdin) |
| `--jq` | — | string | — | Filter the response body through a jq expression |
| `--method` | `X` | string | GET | HTTP method |
| `--paginate` | — | bool | false | Follow the page query parameter until an empty page |
| `--slurp` | — | bool | false | Merge paginated pages into a single JSON array (requires --paginate) |

**示例**

```bash
gitcode api repos/owner/repo/pulls/123/files
gitcode api 'repos/owner/repo/commits?path=src/main.go&sha=main'
gitcode api repos/owner/repo/pulls/123 --method PATCH --input body.json
```

### `gitcode auth git-credential`

Provide stored GitCode credentials to git (helper protocol)

`用法: gitcode auth git-credential [operation]`

参数: `operation`

**示例**

```bash
printf 'protocol=https\nhost=gitcode.com\n\n' | gitcode auth git-credential
gitcode auth setup-git
```

### `gitcode auth login`

Log in to a GitCode account

`用法: gitcode auth login`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--git-protocol` | `p` | string | https | The Git protocol to use for operations (https/ssh)（可选: https, ssh） |
| `--hostname` | `H` | string | — | The hostname of the GitCode instance to authenticate with |
| `--web` | `w` | bool | false | Open GitCode.com in a browser to authenticate |
| `--with-token` | — | bool | false | Read token from standard input |

**示例**

```bash
gitcode auth login
gitcode auth login --web
gitcode auth login --hostname gitcode.com
```

### `gitcode auth logout`

Log out of a GitCode account

`用法: gitcode auth logout`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--hostname` | `H` | string | — | Hostname of the GitCode instance to log out of (hostname only; normalized and validated) |
| `--username` | `u` | string | — | The username to log out of |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode auth logout
! This will log out of gitcode.com
Type the hostname to confirm: gitcode.com
✓ Cleared stored authentication for gitcode.com
gitcode auth logout --hostname gitcode.com
gitcode auth logout --yes
```

### `gitcode auth setup-git`

Configure git to use gc as a credential helper

`用法: gitcode auth setup-git`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--hostname` | `H` | string | — | Configure the credential helper for a specific hostname |

**示例**

```bash
gitcode auth setup-git
gitcode auth setup-git --hostname gitcode.com
```

### `gitcode auth status`

View authentication status

`用法: gitcode auth status`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--hostname` | `H` | string | — | Check a specific hostname |
| `--json` | — | bool | false | Output as JSON |
| `--show-token` | — | bool | false | Display the full auth token |

**示例**

```bash
gitcode auth status
gitcode.com
✓ Logged in as username (GC_TOKEN)
✓ Git operations protocol: https
gitcode auth status --json
```

### `gitcode auth token`

Print an authentication token

`用法: gitcode auth token`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--hostname` | `H` | string | — | The hostname to get the token for |
| `--json` | — | bool | false | Output as JSON |

**示例**

```bash
gitcode auth token
gc_xxxxxxxxxxxx
TOKEN=$(gc auth token)
gitcode auth token --hostname gitcode.com
```

### `gitcode browse`

Open a GitCode repository in the browser

`用法: gitcode browse [<number> | <path>]`

参数: `<number>`, `|`（必填）, `<path>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--branch` | — | string | — | Open a specific branch |
| `--commit` | — | string | — | Open a specific commit |
| `--no-browser` | — | bool | false | Print URL only, do not open browser |
| `--pr` | — | bool | false | Open as pull request (when passing a number) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode browse -R owner/repo
gitcode browse 42 -R owner/repo
gitcode browse 42 --pr -R owner/repo
```

### `gitcode config clear-cache`

Clear CLI cache

`用法: gitcode config clear-cache`

### `gitcode config get`

Read a configuration value

`用法: gitcode config get <key>`

参数: `<key>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

### `gitcode config list`

List all configuration values

`用法: gitcode config list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

### `gitcode config set`

Store a configuration value

`用法: gitcode config set <key> <value>`

参数: `<key>`（必填）, `<value>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

### `gitcode doctor install`

Inspect installation source and command conflicts

`用法: gitcode doctor install`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

### `gitcode lark auth status`

Show lark-cli login status

`用法: gitcode lark auth status`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

**示例**

```bash
gitcode lark auth status
gitcode lark auth status --json
```

### `gitcode lark config get`

Show the effective default Feishu/Lark chat id

`用法: gitcode lark config get`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

**示例**

```bash
gitcode lark config get
gitcode lark config get --json
```

### `gitcode lark config set`

Set the default Feishu/Lark chat id

`用法: gitcode lark config set`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--default-chat` | — | string | — | **必填** Feishu/Lark chat id (oc_xxx) to use as default |

**示例**

```bash
gitcode lark config set --default-chat oc_xxx
```

### `gitcode lark doctor`

Check lark-cli installation and login readiness

`用法: gitcode lark doctor`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

**示例**

```bash
gitcode lark doctor
gitcode lark doctor --json
```

### `gitcode lark install`

Install the official lark-cli tool

`用法: gitcode lark install`

**示例**

```bash
gitcode lark install
```

### `gitcode lark send`

Send a message to a Feishu/Lark chat or direct message

`用法: gitcode lark send`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--as` | — | string | — | Identity: bot \| user (default: lark-cli default, or bot when --to-self) |
| `--body-file` | — | string | — | Read message text from file (use - for stdin) |
| `--chat-id` | — | string | — | Feishu/Lark chat id (oc_xxx); send to a group/chat |
| `--dry-run` | — | bool | false | Preview the lark-cli call without sending |
| `--file` | — | string | — | File path to send as an attachment (forwarded to lark-cli) |
| `--json` | — | bool | false | Output as JSON |
| `--markdown` | — | string | — | Markdown message |
| `--text` | — | string | — | Plain text message |
| `--to-self` | — | bool | false | Send a direct message to the current lark-cli user (resolves open_id from auth status) |
| `--user-id` | — | string | — | Feishu/Lark user open_id (ou_xxx); send a direct message |

**示例**

```bash
gitcode lark send --to-self --text "deploy done"
gitcode lark send --chat-id oc_xxx --text "deploy done"
gitcode lark send --user-id ou_xxx --as bot --text "hi"
```

### `gitcode precommit check`

Check pre-commit configuration before committing or pushing

`用法: gitcode precommit check`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--no-install` | — | bool | false | Only diagnose; never install the tool or hooks |
| `--run` | — | bool | false | Run pre-commit and pre-push stages across all files after verifying |
| `--yes` | `y` | bool | false | Allow environment changes (install/init) in non-interactive mode |

**示例**

```bash
gitcode precommit check
gitcode precommit check --run
gitcode precommit check --no-install
```

### `gitcode schema`

Print machine-readable command metadata

`用法: gitcode schema [command-path]`

参数: `command-path`

**示例**

```bash
gitcode schema
gitcode schema "issue view"
```

### `gitcode ssh-key add`

Add an SSH public key

`用法: gitcode ssh-key add`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--key` | `k` | string | — | **必填** Path to the SSH public key file |
| `--title` | `t` | string | — | **必填** Title for the SSH key |

**示例**

```bash
gitcode ssh-key add --title laptop --key ~/.ssh/id_ed25519.pub
gitcode ssh-key add --title laptop --key key.pub --json
```

### `gitcode ssh-key delete`

Delete an SSH public key

`用法: gitcode ssh-key delete <id>`

参数: `<id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview the deletion without making changes |
| `--json` | — | bool | false | Output as JSON |
| `--yes` | `y` | bool | false | Skip confirmation |

**示例**

```bash
gitcode ssh-key delete 123
gitcode ssh-key delete 123 --yes --json
```

### `gitcode ssh-key list`

List SSH public keys

`用法: gitcode ssh-key list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of SSH keys to list |
| `--page` | — | int | 1 | Page number |
| `--per-page` | — | int | 0 | API page size (default: --limit) |

**示例**

```bash
gitcode ssh-key list
gitcode ssh-key list --limit 50 --page 2
gitcode ssh-key list --json
```

### `gitcode ssh-key view`

View an SSH public key

`用法: gitcode ssh-key view <id>`

参数: `<id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |

**示例**

```bash
gitcode ssh-key view 123 --json
```

### `gitcode update`

Check for or apply an installation-channel update

`用法: gitcode update`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--check` | — | bool | false | Check for an update without installing it |
| `--json` | — | bool | false | Output as JSON |

### `gitcode version`

Print gitcode version

`用法: gitcode version`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
