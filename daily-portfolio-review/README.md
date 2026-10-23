# daily-portfolio-review

账户风险、盈亏归因与交易行为的完整复盘。

分类：组合复盘。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

账户风险、盈亏归因与交易行为的完整复盘。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

持仓和日期、账户市值、交易流水、手续费；支持文本/CSV/截图。

## 会得到什么

净 P&L 归因、集中度、Beta、相对表现、新闻、催化剂及次日观察事项。

## 使用示例

- “使用 daily-portfolio-review：根据这份持仓 CSV 和交易流水复盘今天账户。”
- “使用 daily-portfolio-review：解释今天账户相对 SPY 的表现，指出缺失数据。”

## 边界与相邻技能

需要账户数据；不适用于只有市场走势的日报。佣金已计入净值时不重复扣减。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py daily-portfolio-review` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `daily-portfolio-review/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `assets/report-template.md`
- `references/catalyst-types.md`
- `references/gics-mapping.md`
- `references/review-core.md`
- `references/sector-mapping.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。

## Finance 合并记录

保留 Investment 的账户边界、输出格式、共用复盘口径和手续费修正；Finance 的报告模板、催化剂类型与板块映射均已包含且完全一致。原始版权与许可见 [LICENSE](LICENSE)，来源提交及取舍见 [ORIGIN.md](ORIGIN.md)。
