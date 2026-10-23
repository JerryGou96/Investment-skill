# summarizing-earnings-calls

电话会正文、管理层口径与分析师 Q&A 摘要。

分类：财报研究。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

电话会正文、管理层口径与分析师 Q&A 摘要。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

电话会 transcript、公司/财季及来源链接；可补充一致预期。

## 会得到什么

业绩/指引、分部 KPI、管理层语气、关键问答、风险及观察事项。

## 使用示例

- “使用 summarizing-earnings-calls：总结这份电话会，重点看管理层是否回避关键问题。”
- “使用 summarizing-earnings-calls：比较本季度与上季度的指引措辞和 Q&A。”

## 边界与相邻技能

不是只凭价格反应生成财报结论；标注 transcript 日期、来源和缺失部分。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py summarizing-earnings-calls` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `summarizing-earnings-calls/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
