# technical-analysis

趋势、均线、RSI、MACD 与布林带分析。

分类：数据与技术分析。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

趋势、均线、RSI、MACD 与布林带分析。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

标的、周期、OHLCV 数据或图表。

## 会得到什么

趋势状态、关键指标、支撑阻力、量价关系和判断依据。

## 使用示例

- “使用 technical-analysis：分析日线与周线趋势是否一致。”
- “使用 technical-analysis：解释这张图里的 RSI、MACD 和 EMA 信号。”

## 边界与相邻技能

指标组合是框架启发式，不是已验证的交易系统；特定 Frank setup 使用专用技能。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py technical-analysis` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `technical-analysis/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
