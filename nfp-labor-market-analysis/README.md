# nfp-labor-market-analysis

非农报告与劳动力市场结构分析。

分类：市场与宏观。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

非农报告与劳动力市场结构分析。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

报告月份、发布日期；BLS 报告、预期及市场反应数据。

## 会得到什么

企业调查与家庭调查拆分、失业率归因、就业质量、宏观信号及市场传导。

## 使用示例

- “使用 nfp-labor-market-analysis：分析这次 NFP，解释失业率为什么上升。”
- “使用 nfp-labor-market-analysis：比较家庭调查和企业调查是否出现分歧。”

## 边界与相邻技能

区分数据所属月份与发布日期；不把失业率单一变化当成完整劳动市场结论。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py nfp-labor-market-analysis` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `nfp-labor-market-analysis/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `references/nfp-framework.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。

## Finance 合并记录

Finance 的 SKILL.md 与 references/nfp-framework.md 与现有维护版完全一致，合并为同一个根目录包。原始版权与许可见 [LICENSE](LICENSE)，来源提交及取舍见 [ORIGIN.md](ORIGIN.md)。
