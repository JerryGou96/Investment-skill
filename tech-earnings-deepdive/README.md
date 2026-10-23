# tech-earnings-deepdive

科技财报的多模块、多视角深度研究。

分类：财报研究。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

科技财报的多模块、多视角深度研究。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

科技公司 ticker、最新财报与估值数据；需网络及脚本依赖。

## 会得到什么

16 模块、6 投资视角、估值矩阵、反偏见检查及研究备忘录。

## 使用示例

- “使用 tech-earnings-deepdive：对 NVDA 最新一季财报做完整深度研究。”
- “使用 tech-earnings-deepdive：从多种投资哲学评估科技公司的估值与反证条件。”

## 边界与相邻技能

保留 Ruby/Star 与 Day1Global 来源。此次验证路径和语法，未验证完整联网财报生成；第三方功能说明不等于已完成端到端验收。

## 环境与依赖

- bash
- Python 3
- jq
- curl
- yfinance 及所选 Python 模块的依赖；当前未锁定完整环境

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 本地运行数据

从本技能目录执行 `bash run.sh --help` 查看入口。缓存/日志/报告默认写入 `~/.openclaw/skill-data/tech-earnings-deepdive`；可用 `TECH_EARNINGS_DATA_DIR` 覆盖。旧模块包含不同分析入口，此次没有承诺所有第三方模块均完成运行验证。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py tech-earnings-deepdive` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `tech-earnings-deepdive/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `FEATURES.html`
- `ORIGIN.md`
- `SKILL.md`
- `config.json`
- `modules/analyze.py`
- `modules/analyze_full.py`
- `modules/batch_analysis.py`
- `modules/bias_framework.py`
- `modules/complete_analysis.py`
- `modules/evidence_search.py`
- `modules/export_report.py`
- `modules/fetch_data.py`
- `modules/key_forces.py`
- `modules/perspectives.py`
- `modules/perspectives_full.py`
- `modules/report.py`
- `modules/valuation.py`
- `modules/valuation_full.py`
- `modules/variant_view.py`
- `references/CHANGELOG.md`
- `references/SHARE_GUIDE.md`
- `run.sh`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
