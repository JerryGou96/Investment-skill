# yfinance-data

Yahoo Finance 数据获取辅助层。

分类：数据与技术分析。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

Yahoo Finance 数据获取辅助层。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

ticker、字段、日期范围、频率及期望数据格式。

## 会得到什么

可供分析使用的价格、财报、期权等数据及获取时间/缺失说明。

## 使用示例

- “使用 yfinance-data：获取 MSFT 最近一年的调整后价格数据。”
- “使用 yfinance-data：导出某公司的季度现金流与资产负债表。”

## 边界与相邻技能

仅负责明确的数据获取或给分析流程供数；裸 ticker 不自动触发全部分析。

## 环境与依赖

- Python 3
- yfinance
- pandas
- numpy（按所用计算需要）

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py yfinance-data` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `yfinance-data/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `references/api_reference.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
