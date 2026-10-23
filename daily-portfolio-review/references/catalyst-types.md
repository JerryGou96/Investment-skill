# 催化剂类型详解 + 搜索关键词

用于"近期催化剂日历"一节。每类催化剂都给出搜索查询模板,确保覆盖完整。

## 📊 财报类

**优先级**:最高 — 自家持仓的财报必须列出

**搜索查询**:
- `{TICKER} earnings date next`
- `{TICKER} Q{N} earnings call`
- `{SECTOR} earnings calendar this week`(看同业)

**需要捕获的字段**:
- 报告日期
- BMO(盘前)/ AMC(盘后)
- Consensus EPS / Revenue 预期
- 是否有特别的指引日(guidance day)

**关键同业财报也要列**:
- 持仓 NVDA → 还要看 AMD、TSM、AVGO 财报
- 持仓 ALB → 还要看 SQM、LAC、PLL 财报
- 持仓银行股 → 还要看 JPM(银行季的"开局")

## 🏛️ 宏观经济

**优先级**:高 — 影响所有持仓

**核心日程**(按月度循环):

| 数据 | 频率 | 发布时间 (ET) | 影响 |
|---|---|---|---|
| FOMC 决议 | 8次/年 | 14:00 | 利率/全市场 |
| FOMC 会议纪要 | 滞后 3 周 | 14:00 | 政策细节 |
| Fed 主席演讲 | 不定期 | — | 风险事件 |
| CPI | 月度 | 08:30 | 通胀 |
| Core PCE | 月度 | 08:30 | Fed 偏好指标 |
| PPI | 月度 | 08:30 | 上游通胀 |
| NFP(非农) | 月度首周五 | 08:30 | 就业/利率预期 |
| 失业救济申请 | 周度(周四) | 08:30 | 就业边际变化 |
| 零售销售 | 月度 | 08:30 | 消费 |
| ISM PMI | 月度 | 10:00 | 制造业/服务业 |
| GDP | 季度 | 08:30 | 增长 |
| Beige Book | 8次/年 | 14:00 | Fed 区域观察 |

**搜索查询**:
- `economic calendar this week`
- `FOMC meeting schedule`
- `CPI release date`

## 🛢️ 商品/能源

**优先级**:中(取决于持仓)

**关键日程**:

| 事件 | 频率 |
|---|---|
| EIA 原油库存 | 周度(周三 10:30) |
| EIA 天然气库存 | 周度(周四 10:30) |
| OPEC+ 会议 | 不定期(查 OPEC 官网) |
| OPEC 月报 (MOMR) | 月度 |
| IEA 月报 | 月度 |
| LME 库存日报 | 每日 |
| COMEX 交割窗口 | 月度(First Notice Day / Last Trade Day) |
| 农产品 WASDE 报告 | 月度 |

**搜索查询**:
- `OPEC meeting schedule`
- `EIA report calendar`
- `COMEX silver delivery first notice day`

## 💊 公司事件

**FDA 相关**(医药持仓必查):
- PDUFA 日期(新药审批截止日)
- AdCom(咨询委员会)会议
- 临床试验数据公布
- 搜索:`{TICKER} FDA PDUFA date` / `{TICKER} clinical readout`

**产品发布 / 投资者日**:
- 苹果 WWDC、特斯拉 Investor Day、英伟达 GTC 等
- 搜索:`{TICKER} investor day` / `{TICKER} product launch`

**分拆 / 并购**:
- Spin-off 日期
- 并购股东投票日
- 反垄断审查关键节点
- 搜索:`{TICKER} spin-off date` / `{TICKER} merger vote`

## ⚖️ 政策 / 监管

**优先级**:中 — 但对受影响持仓很关键

**关键事件类型**:
- 关税公告 / 贸易谈判节点(中美/中欧/USMCA)
- 出口管制清单更新(BIS Entity List)
- SEC 规则发布 / 听证会
- 反垄断诉讼判决
- 行政命令(EO)
- 国会听证(科技、生物、银行业 CEO)

**搜索查询**:
- `{INDUSTRY} regulation news this month`
- `tariff announcement schedule`
- `SEC rule proposal calendar`

## 🔓 股东事件

**IPO 解禁**(对近期 IPO 持仓很关键):
- Lock-up 到期日 = IPO 后 180 天
- 搜索:`{TICKER} lockup expiration date`

**回购 / 分红**:
- 除权日(ex-dividend)
- 派发日
- 回购授权公告
- 搜索:`{TICKER} ex-dividend date` / `{TICKER} buyback announcement`

**股东大会**:
- 年度股东大会(Annual Meeting)
- 特别股东大会(并购投票)
- 搜索:`{TICKER} annual meeting date`

**配股 / 增发**:
- 优先购买权(rights offering)
- 公开增发(secondary offering)
- 可转债发行

## 信息来源优先级

1. **公司 IR 页面**(权威)
2. **SEC EDGAR**(8-K、S-1、DEF 14A)
3. **官方机构**(Fed、Treasury、BLS、EIA)
4. **彭博 / 路透 / WSJ / FT**(财经一线)
5. **Investing.com / Earnings Whispers / TipRanks**(日历聚合)
6. **公司公告社交媒体**(慎用,需交叉验证)

## 时间窗口规则

- **未来 1 周内**:必须列出,即使是低优先级事件
- **1-4 周**:列出所有"📊 财报"和"🏛️ 宏观",其他按重要性筛选
- **4-8 周**:只列出明确日期且对持仓有重大影响的事件
- **超过 8 周**:仅列出"硬日期"(财报、PDUFA、解禁)
