# earnings-recap

财报事实速览与股价反应。

分类：财报研究。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

财报事实速览与股价反应。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

ticker、财季或公告日期；可补充财报发布材料。

## 会得到什么

实际值与预期、季度趋势、指引变化、公告后股价反应及事实背景。

## 使用示例

- “使用 earnings-recap：复盘 AAPL 最近一季财报，只要事实和股价反应。”
- “使用 earnings-recap：这次收入和 EPS 分别相对预期如何？”

## 边界与相邻技能

不输出主动投资立场；估值及持仓判断使用 post-earnings-investment-review。

## 环境与依赖

- Python 3
- yfinance
- pandas
- numpy（按所用计算需要）

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py earnings-recap` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `earnings-recap/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `references/api_reference.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
