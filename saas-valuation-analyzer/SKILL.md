---
name: saas-valuation-analyzer
description: "评估 SaaS 公司的估值和运营效率，参考 BVP Cloud Index 网站 (cloudindex.bvp.com) 的关键指标和估值方法。可用于分析收入倍数、增长率、毛利率、Unit Economics 等。"
---

# SaaS Valuation Analyzer

## 功能描述

此 skill 旨在帮助 Jerry 评估 SaaS 公司的估值和运营效率，核心参考 BVP Cloud Index (cloudindex.bvp.com) 网站上提供的行业标准指标和估值框架。它将提供以下分析能力：

- **估值倍数分析：** 对比公司与行业平均的 EV/Revenue 倍数 (Current/NTM)，并结合增长率进行估值。
- **增长效率：** 分析公司的收入增长率 (Revenue Growth YoY) 及其与估值的关系。
- **盈利能力：** 评估公司的毛利率 (Gross Margin)、运营利润率 (Operating Margin) 等关键盈利指标。
- **Unit Economics：** 关注客户获取成本 (CAC)、客户生命周期价值 (LTV) 等效率指标。
- **SaaS 特定指标：** 如 Rule of 40、净收入留存率 (Net Revenue Retention, NRR)、客户数增长 (Customer Growth) 等。

## 触发条件

当 Jerry 提到以下关键词时应触发此 skill：

- "SaaS 估值", "SaaS 分析", "SaaS 指标", "评估 SaaS 公司", "SaaS 运营效率", "cloud index", "BVP"
- 提供 SaaS 公司 ticker 并要求进行“估值分析”或“效率评估”时。

## Workflow 步骤

1. **获取公司数据：** 根据提供的公司名称或 ticker，尝试从 `cloudindex.bvp.com` 或其他金融数据源获取最新财务和运营数据。
2. **提取关键指标：** 自动识别并提取收入、增长率、毛利率、Operating Margin、RPO、ARR 等关键 SaaS 指标。
3. **计算估值倍数：** 根据当前收入或预期收入 (NTM Revenue) 计算 EV/Revenue 倍数。
4. **对比行业基准：** 将目标公司的指标与 `cloudindex.bvp.com` 提供的行业平均值或最佳实践进行对比。
5. **生成分析报告：** 结构化输出，包括核心指标、估值分析、效率评估、风险提示和投资建议。
6. **Q&A/交互：** 根据 Jerry 的进一步提问，深入分析特定指标或情景。

## 外部数据源

- **BVP Cloud Index (cloudindex.bvp.com)：** 主要数据来源，用于获取行业基准、估值框架和主要 SaaS 公司数据。
- **YFinance/其他金融数据接口：** 补充实时股价、市值等信息，以计算估值倍数。

## 输出格式

- **默认中文输出**，格式清晰、易读，适应 Discord。
- 避免使用复杂的 Markdown 表格，转而使用分段和 bullet points。
- 重点突出关键指标对比、估值结论和潜在风险。


## 本地辅助文件状态

`references/bvp_cloud_index_data.json` 是旧快照且当前为空，不能作为实时估值依据。`scripts/parse_bvp_data.py` 是旧文本解析原型，内嵌历史网页样例并依赖旧相对输出路径；当前流程不要执行它。复用时按上方工作流获取带时间戳的最新数据，或使用用户提供的结构化数据。
