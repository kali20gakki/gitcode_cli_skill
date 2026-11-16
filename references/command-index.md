# 命令总索引

> 自动生成（CLI 0.17.0），共 **161** 个叶命令 + 命令组。
> `completion` / `help` 为 cobra 内建命令，不出现在 `gitcode schema` 中，用法见 `global-contract.md`。
>
> 需要完整参数：读对应 `commands/<家族>.md`；需要现场真值：`python scripts/gc_query.py "<命令路径>"`。

| 家族 | 参考文件 |
| --- | --- |
| `actions` | `commands/ops.md` |
| `api` | `commands/ops.md` |
| `auth` | `commands/ops.md` |
| `browse` | `commands/ops.md` |
| `commit` | `commands/ops.md` |
| `config` | `commands/ops.md` |
| `discussions` | `commands/ops.md` |
| `doctor` | `commands/ops.md` |
| `issue` | `commands/ops.md` |
| `label` | `commands/ops.md` |
| `lark` | `commands/ops.md` |
| `milestone` | `commands/ops.md` |
| `pr` | `commands/ops.md` |
| `precommit` | `commands/ops.md` |
| `release` | `commands/ops.md` |
| `repo` | `commands/ops.md` |
| `schema` | `commands/ops.md` |
| `search` | `commands/ops.md` |
| `ssh-key` | `commands/ops.md` |
| `update` | `commands/ops.md` |
| `user` | `commands/ops.md` |
| `version` | `commands/ops.md` |

## actions

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

## api

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode api` | Make an authenticated GitCode REST API request | — |

## auth

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode auth git-credential` | Provide stored GitCode credentials to git (helper protocol) | — |
| `gitcode auth login` | Log in to a GitCode account | — |
| `gitcode auth logout` | Log out of a GitCode account | — |
| `gitcode auth setup-git` | Configure git to use gc as a credential helper | — |
| `gitcode auth status` | View authentication status | ✓ |
| `gitcode auth token` | Print an authentication token | ✓ |

## browse

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode browse` | Open a GitCode repository in the browser | — |

## commit

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

## config

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode config clear-cache` | Clear CLI cache | — |
| `gitcode config get` | Read a configuration value | ✓ |
| `gitcode config list` | List all configuration values | ✓ |
| `gitcode config set` | Store a configuration value | ✓ |

## discussions

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

## doctor

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode doctor install` | Inspect installation source and command conflicts | ✓ |

## issue

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

## label

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode label create` | Create a label | ✓ |
| `gitcode label delete` | Delete a label | ✓ |
| `gitcode label edit` | Edit a label | ✓ |
| `gitcode label list` | List labels | ✓ |

## lark

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode lark auth status` | Show lark-cli login status | ✓ |
| `gitcode lark config get` | Show the effective default Feishu/Lark chat id | ✓ |
| `gitcode lark config set` | Set the default Feishu/Lark chat id | — |
| `gitcode lark doctor` | Check lark-cli installation and login readiness | ✓ |
| `gitcode lark install` | Install the official lark-cli tool | — |
| `gitcode lark send` | Send a message to a Feishu/Lark chat or direct message | ✓ |

## milestone

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode milestone create` | Create a milestone | ✓ |
| `gitcode milestone delete` | Delete a milestone | — |
| `gitcode milestone edit` | Edit a milestone | ✓ |
| `gitcode milestone list` | List milestones | ✓ |
| `gitcode milestone view` | View a milestone | ✓ |

## pr

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

## precommit

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode precommit check` | Check pre-commit configuration before committing or pushing | ✓ |

## release

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode release create` | Create a new release | ✓ |
| `gitcode release delete` | Delete a release | — |
| `gitcode release delete-asset` | Delete a release asset | — |
| `gitcode release download` | Download release assets | — |
| `gitcode release edit` | Edit a release | ✓ |
| `gitcode release list` | List releases | ✓ |
| `gitcode release upload` | Upload assets to a release | ✓ |
| `gitcode release view` | View release details | ✓ |

## repo

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

## schema

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode schema` | Print machine-readable command metadata | — |

## search

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode search issues` | Search for issues | ✓ |
| `gitcode search repos` | Search for repositories | ✓ |
| `gitcode search users` | Search for users | ✓ |

## ssh-key

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode ssh-key add` | Add an SSH public key | ✓ |
| `gitcode ssh-key delete` | Delete an SSH public key | ✓ |
| `gitcode ssh-key list` | List SSH public keys | ✓ |
| `gitcode ssh-key view` | View an SSH public key | ✓ |

## update

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode update` | Check for or apply an installation-channel update | ✓ |

## user

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode user edit` | Edit your user profile | ✓ |
| `gitcode user view` | View a user profile | ✓ |

## version

| 命令 | 摘要 | JSON |
| --- | --- | --- |
| `gitcode version` | Print gitcode version | ✓ |
