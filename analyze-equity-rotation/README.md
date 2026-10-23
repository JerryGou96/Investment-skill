# analyze-equity-rotation

美股、风格及 AI 产业链轮动分析。

分类：市场与宏观。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

美股、风格及 AI 产业链轮动分析。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

指定市场日期或用户报告；需要跨期分析时提供或获取相应价格历史。

## 会得到什么

市场环境、行业/AI 子行业强弱、广度验证、领先/改善/转弱/落后分类及反证条件。

## 使用示例

- “使用 analyze-equity-rotation：分析本周 AI 硬件内部轮动，单独看半导体设备。”
- “使用 analyze-equity-rotation：仅根据这份报告判断行业轮动，不补充最新行情。”

## 边界与相邻技能

单日涨跌不能推导 20 日趋势；半导体设备保留独立分组。此次保留远端技能，不额外改变本地 Agent 安装范围。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py analyze-equity-rotation` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `analyze-equity-rotation/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `agents/openai.yaml`
- `references/framework.md`
- `references/output-template.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
