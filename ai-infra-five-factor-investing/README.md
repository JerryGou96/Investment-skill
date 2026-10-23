# ai-infra-five-factor-investing

AI 基建产业链与五因素投资框架。

分类：公司研究。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

AI 基建产业链与五因素投资框架。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

公司或 ticker、产业链环节、研究时间范围；可附已有持仓或研究资料。

## 会得到什么

产业瓶颈、五因素判断、证据强弱、仓位逻辑及后续验证条件。

## 使用示例

- “使用 ai-infra-five-factor-investing：用五因素框架比较 MU、MRVL 和 CRDO。”
- “使用 ai-infra-five-factor-investing：分析这家公司的 AI 基建增长逻辑，哪些证据会推翻它？”

## 边界与相邻技能

不把历史 ticker 示例当成当前推荐；AgentBrain 是可选的本地笔记集成。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py ai-infra-five-factor-investing` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `ai-infra-five-factor-investing/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
