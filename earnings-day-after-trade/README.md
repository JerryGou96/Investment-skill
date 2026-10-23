# earnings-day-after-trade

财报次日开盘区间交易计划。

分类：交易框架。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

财报次日开盘区间交易计划。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

ticker、财报或指引催化剂、盘前及开盘价格/成交量。

## 会得到什么

多空触发位、1–3 分钟开盘区间、失效条件、目标与不交易条件。

## 使用示例

- “使用 earnings-day-after-trade：为财报次日制定开盘区间交易计划。”
- “使用 earnings-day-after-trade：这次盘前跳空是否适合 day-after trade？”

## 边界与相邻技能

是盘中计划框架，区别于多月箱体突破；不自动下单，缺乏实时数据时不得给出伪实时点位。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py earnings-day-after-trade` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `earnings-day-after-trade/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `references/playbook.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
