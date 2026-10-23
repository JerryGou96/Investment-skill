# post-earnings-investment-review

保留 investment 定制的财报投资判断。

分类：财报研究。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

保留 investment 定制的财报投资判断。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

ticker、财报日期、预期/指引与估值数据；可附持仓背景。

## 会得到什么

结论先行、预期差、业务拆分、估值/PEG、风险收益与观察指标。

## 使用示例

- “使用 post-earnings-investment-review：这份财报改变了投资逻辑吗？分析估值和风险收益。”
- “使用 post-earnings-investment-review：收入超预期但股价下跌，是否是预期差或估值问题？”

## 边界与相邻技能

研究判断须有证据，区分共识、whisper 和个人推断；与事实版 earnings-recap 分开触发。

## 环境与依赖

- Python 3
- yfinance
- pandas
- numpy（按所用计算需要）

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py post-earnings-investment-review` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `post-earnings-investment-review/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `references/api_reference.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
