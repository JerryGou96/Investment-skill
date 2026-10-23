---
name: us-market-close-recap
description: "生成美股盘后市场日报。用于盘后总结、日报、正式版、美股复盘。覆盖指数表现、SPY/QQQ技术面、11板块轮动、AI硬件、IGV/SaaS软件、光互联、宏观、Market Regime和下一交易日观察清单。周报/本周总结请使用 us-weekly-cross-asset-recap。"
---

# US Market Close Recap

Use for Jerry's market-level after-close recap. This is not the account/portfolio P&L review.

## Triggers

- "盘后总结"、"美股盘后"、"日报"、"正式版"、"今日市场复盘"
- End-of-day market recap requests without portfolio screenshots or trade data

If the user provides holdings/trades/account screenshots, use `daily-portfolio-review` for the account-level review instead.
If the user asks for a weekly recap, use `us-weekly-cross-asset-recap`.

## Data Sources

Use current/live verification because market data changes:

- Yahoo Finance daily data for ETFs, stocks, rates proxies, DXY, WTI, gold.
- AP/Reuters or equivalent market wrap for index-level confirmation.
- Official macro source when relevant: BEA, BLS, Fed, Treasury.
- FedChirp / CME FedWatch / Fed futures for year-end policy-path framing when available.
- AgentBrain for Jerry-specific themes and prior research.

Opening source line:

`数据源: Yahoo Finance 日线(截至美股收盘)、AP/Reuters 市场报道、FedChirp/Fed futures 页面。若个别宏观/期货收盘口径与实时终端略有差异,以交易所终端为准。`

## Output Style

- Chinese by default.
- Discord-friendly: numbered sections and bullets, no Markdown tables.
- Direct, investment-focused, concise but complete.
- Separate "trend still intact" from "short-term overbought / crowded".
- Do not give mechanical buy/sell advice; give watch/discipline framing.

## Daily Template

Title:

`美股盘后总结｜YYYY-MM-DD`

### 1. 指数表现

Include:

- SPY, QQQ, DIA, IWM, VIX: close and daily %.
- Spot index supplement: S&P 500, Nasdaq, Dow, Russell 2000: level and daily %.
- One-line conclusion: high-level market tone, e.g. high-level consolidation, narrow AI-led risk-on, broad risk-off.

### 2. 指数技术面

For SPY and QQQ include:

- RSI(14).
- MACD / Signal / Hist.
- Daily volume, 20-day average volume, volume multiple.
- 8-day, 21-day, 50-day, 200-day EMAs.
- Trend/risk interpretation: above/below key EMAs, overbought state, meaning of losing 8EMA/21EMA.

### 3. 板块表现

Rank S&P 11 sector ETFs from strong to weak:

- XLY, XLP, XLC, XLB, XLV, XLI, XLRE, XLK, XLU, XLF, XLE.
- Name Strongest and Weakest.
- Rotation signal: what money bought/sold, and whether this is AI/tech-led, defensive, value/cyclical, energy-led, etc.
- If AI/semis matter, include SMH/SOXX and key AI names.

Mandatory light check:

- IGV/SaaS software. If IGV or representative SaaS names materially outperform/underperform QQQ/XLK, note whether this is software mispricing repair, AI-adaptation re-rating, or continuation/reversal of the popular `long hardware / short software` pair trade.

### 4. 基本面环境: 市场在买什么、卖什么

Cover:

- Buy side: sectors/themes/chains bought and why.
- Sell side: sectors/themes/chains sold and why.
- Earnings/theme narrative: what the market actually traded today.
- Distinguish medium-term thesis intact vs short-term profit-taking.
- Include Jerry-specific themes when active: AI server, optical interconnect, MRVL/LITE/COHR/AAOI, AI power, crypto, SaaS/IGV.

### 5. 宏观环境

Include:

- Rates: 10Y, 5Y, 30Y Treasury yields and daily move; TLT optional.
- Dollar: DXY.
- Oil: WTI, and whether oil was a key macro variable.
- Gold: GC.
- Fed expectations: year-end policy path / implied rate framing where possible.
- Next trading day's important macro events.

### 6. 一句话 Market Regime

Format:

`Regime: ...`

Then explain next-session implications:

- Is the index trend still bullish?
- Are RSI/MACD/volume supportive or stretched?
- Is chasing attractive, or is waiting for 8dma/21dma pullback better?
- Which sectors/themes must confirm continuation?

### 7. 观察清单/下一交易日重点

List 3-6 items:

- Key events/earnings/conferences.
- Important technical levels.
- Rotation checks.
- Theme divergences or profit-taking to monitor.
- Jerry-specific watch items.

## Implementation Notes

- Use yfinance for daily and weekly returns where possible.
- For weekly performance, use the actual trading week. If Monday was a holiday, state that the week was shortened.
- For spot index levels, use AP/Reuters or reliable market wrap if Yahoo ETF proxies are not enough.
- For volatile claims and event dates, verify with live sources and include links when useful.
