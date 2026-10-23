# saas-valuation-analyzer

SaaS 估值、增长效率和经营指标分析。

分类：公司研究。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

SaaS 估值、增长效率和经营指标分析。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

公司 ticker、带时间戳的财务/运营数据与可比公司。

## 会得到什么

EV/Revenue、增长率、利润率、Rule of 40、NRR 等及相对估值判断。

## 使用示例

- “使用 saas-valuation-analyzer：分析这家 SaaS 公司的估值是否被增长率支持。”
- “使用 saas-valuation-analyzer：比较三家 SaaS 公司的增长效率与收入倍数。”

## 边界与相邻技能

旧 BVP 快照为空；旧解析脚本内嵌历史数据且未适配当前路径，标为 legacy，不运行它获取实时结果。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py saas-valuation-analyzer` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `saas-valuation-analyzer/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `references/bvp_cloud_index_data.json`
- `scripts/parse_bvp_data.py`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
