# actions — 流水线、Job、Artifact 与 Runner 命令

> 自动生成：`scripts/gen_references.py` ← `gitcode schema`（CLI 0.17.0）。请勿手工编辑；需要现场真值时用 `python scripts/gc_query.py "<命令路径>"`。

## 命令清单

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode actions artifact delete` | Delete an artifact | ✓ |
| `gitcode actions artifact download` | Download an artifact | — |
| `gitcode actions artifact list` | List repository artifacts | ✓ |
| `gitcode actions artifact view` | View an artifact | ✓ |
| `gitcode actions job list` | List workflow jobs of a pipeline run | ✓ |
| `gitcode actions job log` | Download a workflow job log | — |
| `gitcode actions job view` | View a workflow job | ✓ |
| `gitcode actions plugin list` | List official Actions plugins | ✓ |
| `gitcode actions plugin view` | View an Actions plugin detail and README | ✓ |
| `gitcode actions run list` | List pipeline runs | ✓ |
| `gitcode actions run rerun` | Rerun all jobs of a pipeline run | ✓ |
| `gitcode actions run retry` | Retry failed or canceled jobs of a pipeline run | ✓ |
| `gitcode actions run stop` | Stop a running pipeline run | ✓ |
| `gitcode actions run view` | View a pipeline run | ✓ |
| `gitcode actions run watch` | Watch a pipeline run until completion | ✓ |
| `gitcode actions runner list` | List repository host runners | ✓ |
| `gitcode actions runner shared-runners` | List shared host runners for a repository | ✓ |
| `gitcode actions runner-group list` | List organization runner groups | ✓ |
| `gitcode actions runner-group runner list` | List host runners in a runner group | ✓ |
| `gitcode actions runner-group runner-set list` | List K8S runner sets in a runner group | ✓ |
| `gitcode actions runner-group shared-namespace list` | List shared namespaces for a runner group | ✓ |
| `gitcode actions runner-group view` | View a runner group | ✓ |
| `gitcode actions runner-set list` | List repository K8S runner sets | ✓ |
| `gitcode actions runner-set shared-runner-sets` | List shared K8S runner sets for a repository | ✓ |
| `gitcode actions setting` | Enable or disable repository Actions | ✓ |
| `gitcode actions workflow list` | List workflows | ✓ |
| `gitcode actions workflow run` | Trigger a workflow run | ✓ |
| `gitcode actions yaml validate` | Validate workflow YAML syntax | ✓ |

## 命令组

### `gitcode actions`

Manage GitCode Actions

子命令: `artifact`, `job`, `plugin`, `run`, `runner`, `runner-group`, `runner-set`, `setting`, `workflow`, `yaml`

### `gitcode actions artifact`

Manage workflow artifacts

子命令: `delete`, `download`, `list`, `view`

### `gitcode actions job`

Manage workflow jobs

子命令: `list`, `log`, `view`

### `gitcode actions plugin`

Query official Actions plugins

子命令: `list`, `view`

### `gitcode actions run`

Manage pipeline runs

子命令: `list`, `rerun`, `retry`, `stop`, `view`, `watch`

### `gitcode actions runner`

Manage repository runners

子命令: `list`, `shared-runners`

### `gitcode actions runner-group`

Manage organization runner groups

子命令: `list`, `runner`, `runner-set`, `shared-namespace`, `view`

### `gitcode actions runner-group runner`

Manage runners in a runner group

子命令: `list`

### `gitcode actions runner-group runner-set`

Manage K8S runner sets in a runner group

子命令: `list`

### `gitcode actions runner-group shared-namespace`

Manage shared namespaces for a runner group

子命令: `list`

### `gitcode actions runner-set`

Manage repository K8S runner sets

子命令: `list`, `shared-runner-sets`

### `gitcode actions workflow`

Manage workflow files

子命令: `list`, `run`

### `gitcode actions yaml`

Manage workflow YAML configuration

子命令: `validate`

## 详细参数

### `gitcode actions artifact delete`

Delete an artifact

`用法: gitcode actions artifact delete <artifact-id>`

参数: `<artifact-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--dry-run` | — | bool | false | Preview the deletion without deleting |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | `y` | bool | false | Skip confirmation (required in non-interactive mode) |

**示例**

```bash
gitcode actions artifact delete <artifact-id> -R owner/repo
gitcode actions artifact delete <artifact-id> -R owner/repo --yes
gitcode actions artifact delete <artifact-id> -R owner/repo --dry-run
```

### `gitcode actions artifact download`

Download an artifact

`用法: gitcode actions artifact download <artifact-id>`

参数: `<artifact-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--output` | `o` | string | — | Write artifact ZIP to FILE (default: stdout) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions artifact download <artifact-id> -R owner/repo --output artifact.zip
gitcode actions artifact download <artifact-id> -R owner/repo > artifact.zip
```

### `gitcode actions artifact list`

List repository artifacts

`用法: gitcode actions artifact list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--direction` | — | string | — | Sort direction (asc/desc)（可选: asc, desc） |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of artifacts to list |
| `--name` | — | string | — | Filter by artifact name (fuzzy) |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--run` | — | string | — | Filter by workflow run id (list run-scoped artifacts) |
| `--sort` | — | string | — | Sort by created（可选: created） |

**示例**

```bash
gitcode actions artifact list -R owner/repo
gitcode actions artifact list -R owner/repo --run <run-id>
gitcode actions artifact list -R owner/repo --name build
```

### `gitcode actions artifact view`

View an artifact

`用法: gitcode actions artifact view <artifact-id>`

参数: `<artifact-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions artifact view <artifact-id> -R owner/repo
gitcode actions artifact view <artifact-id> -R owner/repo --json
```

### `gitcode actions job list`

List workflow jobs of a pipeline run

`用法: gitcode actions job list <run-id>`

参数: `<run-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions job list <run-id> -R owner/repo
gitcode actions job list <run-id> -R owner/repo --format table
gitcode actions job list <run-id> -R owner/repo --json
```

### `gitcode actions job log`

Download a workflow job log

`用法: gitcode actions job log <run-id> <job-id>`

参数: `<run-id>`（必填）, `<job-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--output` | `o` | string | — | Write log to FILE (default: stdout) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions job log <run-id> <job-id> -R owner/repo --output job-log.zip
unzip job-log.zip
gitcode actions job log <run-id> <job-id> -R owner/repo > job-log.zip
```

### `gitcode actions job view`

View a workflow job

`用法: gitcode actions job view <run-id> <job-id>`

参数: `<run-id>`（必填）, `<job-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions job view <run-id> <job-id> -R owner/repo
gitcode actions job view <run-id> <job-id> -R owner/repo --json
```

### `gitcode actions plugin list`

List official Actions plugins

`用法: gitcode actions plugin list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--files` | — | string | — | Write output to file (UTF-8 bytes, avoids shell encoding issues) |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 0 | Maximum number of plugins to list (0 = no limit, fetch all) |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |
| `--repo` | `R` | string | — | Repository (owner/repo, defaults to current repo or gitcode-cli/cli) |

**示例**

```bash
gitcode actions plugin list -R owner/repo
gitcode actions plugin list -R owner/repo --page 1 --per-page 20
gitcode actions plugin list -R owner/repo --json
```

### `gitcode actions plugin view`

View an Actions plugin detail and README

`用法: gitcode actions plugin view <plugin-name>`

参数: `<plugin-name>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--files` | — | string | — | Write output to file (UTF-8 bytes, avoids shell encoding issues) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo, defaults to current repo or gitcode-cli/cli) |

**示例**

```bash
gitcode actions plugin view checkout -R owner/repo
gitcode actions plugin show checkout -R owner/repo
gitcode actions plugin view checkout -R owner/repo --json
```

### `gitcode actions run list`

List pipeline runs

`用法: gitcode actions run list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--branch` | — | string | — | Filter by branch |
| `--commit` | — | string | — | Filter by exact full commit SHA |
| `--created` | — | string | — | Filter runs created on or after date (YYYY-MM-DD) |
| `--event` | — | string | — | Filter by trigger event (MR/Push/Manual)（可选: MR, Push, Manual） |
| `--executor` | — | string | — | Filter by executor username |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum number of runs to list |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |
| `--pr` | — | string | — | Filter by PR number |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--status` | — | string | — | Filter by run status (COMPLETED/RUNNING/FAILED/CANCELED/IGNORED/PAUSED/SUSPEND)（可选: COMPLETED, RUNNING, FAILED, CANCELED, IGNORED, PAUSED, SUSPEND） |
| `--workflow` | — | string | — | Filter by workflow name |
| `--workflow-id` | — | string | — | Filter by workflow id |

**示例**

```bash
gitcode actions run list -R owner/repo
gitcode actions run list -R owner/repo --status FAILED --event Push
gitcode actions run list -R owner/repo --branch main --executor dev
```

### `gitcode actions run rerun`

Rerun all jobs of a pipeline run

`用法: gitcode actions run rerun <run-id>`

参数: `<run-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode actions run rerun <run-id> -R owner/repo
gitcode actions run rerun <run-id> -R owner/repo --yes
gitcode actions run rerun <run-id> -R owner/repo --yes --json
```

### `gitcode actions run retry`

Retry failed or canceled jobs of a pipeline run

`用法: gitcode actions run retry <run-id>`

参数: `<run-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--failed` | — | bool | false | Retry all failed/canceled jobs of the run |
| `--job` | — | stringArray | [] | Job id to retry (repeatable) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode actions run retry <run-id> --job <job-id> --job <job-id-2> -R owner/repo
gitcode actions run retry <run-id> --failed -R owner/repo
gitcode actions run retry <run-id> --failed --yes -R owner/repo
```

### `gitcode actions run stop`

Stop a running pipeline run

`用法: gitcode actions run stop <run-id>`

参数: `<run-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--yes` | — | bool | false | Skip confirmation prompt |

**示例**

```bash
gitcode actions run stop <run-id> -R owner/repo
gitcode actions run stop <run-id> -R owner/repo --yes
gitcode actions run stop <run-id> -R owner/repo --yes --json
```

### `gitcode actions run view`

View a pipeline run

`用法: gitcode actions run view <run-id>`

参数: `<run-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions run view <run-id> -R owner/repo
gitcode actions run view <run-id> -R owner/repo --json
```

### `gitcode actions run watch`

Watch a pipeline run until completion

`用法: gitcode actions run watch <run-id>`

参数: `<run-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--compact` | — | bool | false | Show only failed steps |
| `--exit-status` | — | bool | false | Exit with non-zero status if run failed |
| `--interval` | `i` | int | 3 | Refresh interval in seconds |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |
| `--wait` | — | bool | false | In non-interactive mode, keep polling until the run reaches a terminal state |

**示例**

```bash
gitcode actions run watch <run-id> -R owner/repo
gitcode actions run watch <run-id> -R owner/repo --interval 10
gitcode actions run watch <run-id> -R owner/repo --compact
```

### `gitcode actions runner list`

List repository host runners

`用法: gitcode actions runner list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--keyword` | — | string | — | Filter by keyword |
| `--limit` | `L` | int | 30 | Maximum number of runners to list |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions runner list -R owner/repo
gitcode actions runner list -R owner/repo --keyword prod
gitcode actions runner list -R owner/repo --paginate --per-page 100
```

### `gitcode actions runner shared-runners`

List shared host runners for a repository

`用法: gitcode actions runner shared-runners`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--keyword` | — | string | — | Filter by keyword |
| `--limit` | `L` | int | 30 | Maximum number of runners to list |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions runner shared-runners -R owner/repo
gitcode actions runner shared-runners -R owner/repo --keyword prod
gitcode actions runner shared-runners -R owner/repo --paginate --per-page 100
```

### `gitcode actions runner-group list`

List organization runner groups

`用法: gitcode actions runner-group list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--format` | — | string | — | Output format (json/simple/table)（可选: json, simple, table） |
| `--json` | — | bool | false | Output as JSON |
| `--keyword` | — | string | — | Filter by keyword |
| `--limit` | `L` | int | 30 | Maximum number of runner groups to list |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |

**示例**

```bash
gitcode actions runner-group list --org my-org
gitcode actions runner-group list --org my-org --keyword prod
gitcode actions runner-group list --org my-org --paginate --per-page 100
```

### `gitcode actions runner-group runner list`

List host runners in a runner group

`用法: gitcode actions runner-group runner list <runner-group-id>`

参数: `<runner-group-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--keyword` | — | string | — | Filter by keyword |
| `--limit` | `L` | int | 30 | Maximum number of runners to list |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |

**示例**

```bash
gitcode actions runner-group runner list <runner-group-id> --org my-org
gitcode actions runner-group runner list <runner-group-id> --org my-org --keyword prod
gitcode actions runner-group runner list <runner-group-id> --org my-org --paginate --per-page 100
```

### `gitcode actions runner-group runner-set list`

List K8S runner sets in a runner group

`用法: gitcode actions runner-group runner-set list <runner-group-id>`

参数: `<runner-group-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--keyword` | — | string | — | Filter by keyword |
| `--limit` | `L` | int | 30 | Maximum number of runner sets to list |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |

**示例**

```bash
gitcode actions runner-group runner-set list <runner-group-id> --org my-org
gitcode actions runner-group runner-set list <runner-group-id> --org my-org --keyword prod
gitcode actions runner-group runner-set list <runner-group-id> --org my-org --paginate --per-page 100
```

### `gitcode actions runner-group shared-namespace list`

List shared namespaces for a runner group

`用法: gitcode actions runner-group shared-namespace list <runner-group-id>`

参数: `<runner-group-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--keyword` | — | string | — | Filter by keyword |
| `--limit` | `L` | int | 30 | Maximum number of shared namespaces to list |
| `--org` | — | string | — | **必填** Organization path (required) |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |

**示例**

```bash
gitcode actions runner-group shared-namespace list <runner-group-id> --org my-org
gitcode actions runner-group shared-namespace list <runner-group-id> --org my-org --keyword prod
gitcode actions runner-group shared-namespace list <runner-group-id> --org my-org --paginate --per-page 100
```

### `gitcode actions runner-group view`

View a runner group

`用法: gitcode actions runner-group view <runner-group-id>`

参数: `<runner-group-id>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | **必填** Organization path (required) |

**示例**

```bash
gitcode actions runner-group view <runner-group-id> --org my-org
gitcode actions runner-group view <runner-group-id> --org my-org --json
```

### `gitcode actions runner-set list`

List repository K8S runner sets

`用法: gitcode actions runner-set list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--keyword` | — | string | — | Filter by keyword |
| `--limit` | `L` | int | 30 | Maximum number of runner sets to list |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions runner-set list -R owner/repo
gitcode actions runner-set list -R owner/repo --keyword prod
gitcode actions runner-set list -R owner/repo --paginate --per-page 100
```

### `gitcode actions runner-set shared-runner-sets`

List shared K8S runner sets for a repository

`用法: gitcode actions runner-set shared-runner-sets`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--keyword` | — | string | — | Filter by keyword |
| `--limit` | `L` | int | 30 | Maximum number of runner sets to list |
| `--page` | — | int | 0 | Page number to fetch |
| `--paginate` | — | bool | false | Fetch all pages |
| `--per-page` | — | int | 0 | API page size (default: --limit, or 100 with --paginate) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions runner-set shared-runner-sets -R owner/repo
gitcode actions runner-set shared-runner-sets -R owner/repo --keyword prod
gitcode actions runner-set shared-runner-sets -R owner/repo --paginate --per-page 100
```

### `gitcode actions setting`

Enable or disable repository Actions

`用法: gitcode actions setting <enable|disable>`

参数: `<enable|disable>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--org` | — | string | — | Organization name; batch every repository in it (mutually exclusive with -R) |
| `--repo` | `R` | string | — | Repository (owner/repo, defaults to the current repository) |
| `--with-token` | — | bool | false | Read the gitcode.com web session JWT from standard input |
| `--yes` | `y` | bool | false | Skip confirmation (required in non-interactive mode) |

**示例**

```bash
gitcode actions setting enable -R owner/repo
gitcode actions setting enable
gitcode actions setting disable -R owner/repo --yes
```

### `gitcode actions workflow list`

List workflows

`用法: gitcode actions workflow list`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--json` | — | bool | false | Output as JSON |
| `--limit` | `L` | int | 30 | Maximum results per page |
| `--page` | — | int | 0 | Page number |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions workflow list -R owner/repo
gitcode actions workflow list -R owner/repo --json
```

### `gitcode actions workflow run`

Trigger a workflow run

`用法: gitcode actions workflow run [<workflow-id> | <filename>]`

参数: `<workflow-id>`, `|`（必填）, `<filename>`（必填）

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--field` | `f` | stringArray | [] | Add string input in key=value format |
| `--json` | — | bool | false | Output as JSON |
| `--ref` | — | string | — | Branch or tag name (required) |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions workflow run wf-1 -R owner/repo --ref main
gitcode actions workflow run ci.yml -R owner/repo --ref main
gitcode actions workflow run ci.yml -R owner/repo --ref main -f key1=value1 -f key2=value2
```

### `gitcode actions yaml validate`

Validate workflow YAML syntax

`用法: gitcode actions yaml validate`

| Flag | 简写 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `--file` | — | string | — | Workflow YAML file to validate (use - for stdin) |
| `--json` | — | bool | false | Output as JSON |
| `--repo` | `R` | string | — | Repository (owner/repo) |

**示例**

```bash
gitcode actions yaml validate --file .gitcode/workflows/ci.yml -R owner/repo
cat ci.yml | gitcode actions yaml validate --file - -R owner/repo
gitcode actions yaml validate --file ci.yml -R owner/repo --json
```
