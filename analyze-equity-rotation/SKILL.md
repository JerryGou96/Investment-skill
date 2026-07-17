---
name: analyze-equity-rotation
description: Analyze current or historical equity-market sector rotation beyond traditional GICS sectors, with a detailed AI industry-chain rotation map, breadth, relative strength, fundamentals, catalysts, and confirmation levels. Use when the user asks about today's market, sector or style rotation, AI-internal rotation, market breadth, a technology daily-report rotation section, whether money is moving between AI hardware and software, or a repeatable rotation dashboard or score from live or supplied data.
---

# Analyze Equity Rotation

Produce an evidence-backed rotation map that distinguishes a one-day move from a durable trend and distinguishes price rotation from fundamental rotation.

## Choose the analysis mode

- For "today", "current", or "latest" analysis, browse for fresh prices, official releases, and current catalysts. State the market date, cutoff time, and whether quotes are closing, delayed, or after-hours.
- For a user-supplied report, stay source-bounded unless the user asks for live enrichment. Clearly separate report statements from external verification.
- For a historical date, use data from that date and avoid leaking later information into the analysis.
- For an incomplete session, label the analysis intraday and avoid calling it a closing rotation.

## Follow the workflow

1. Establish the market regime with broad, equal-weight, size, growth/value, volatility, rates, dollar, credit, and breadth data.
2. Rank traditional sectors by absolute return and relative return versus SPY over 1-day, 5-day, 20-day, and 60-day windows when verified history is available.
3. Build AI sub-sector baskets and compare both market-cap-weighted and equal-weight behavior. Read [references/framework.md](references/framework.md) for the taxonomy, starter universe, and scoring system.
4. Check breadth, volume confirmation, leader/laggard dispersion, and whether second-line stocks confirm the leaders.
5. Separate price action from fundamental evidence such as revenue or EPS revisions, capex, orders, shipment timing, capacity, validation, and margins.
6. Attribute plausible catalysts using company IR, government releases, exchange data, and reputable reporting. Label inference as inference; do not invent causal explanations.
7. Classify each group as Leading, Improving, Weakening, Lagging, or Unconfirmed.
8. Identify the next observable confirmation or invalidation signal. Prefer levels, relative-strength relationships, breadth thresholds, or scheduled catalysts over generic advice.
9. Render the result using [references/output-template.md](references/output-template.md). Keep the conclusion concise enough to scan.

## Apply strict analytical rules

- Never infer a 5-day, 20-day, or 60-day trend from a single session. Write `N/A — insufficient verified history` when necessary.
- Never treat an after-hours quote as an official close. Do not mix timestamps silently.
- Do not call a market-wide risk-off move when weakness is concentrated in capitalization-weighted leaders and equal-weight breadth is healthy.
- Do not call healthy AI-internal rotation when all AI infrastructure groups fall and one group merely falls less.
- Do not call hardware-to-software rotation from one software winner. Require basket-level relative strength and breadth confirmation.
- Use equal-weight baskets to test participation; use market-cap-weighted indexes to measure index impact.
- Avoid double counting a company across AI baskets. Assign a primary exposure for scoring and mention secondary exposure separately.
- Treat ETFs as imperfect proxies. For narrow AI themes, prefer transparent custom baskets with at least three representative names when possible.
- Distinguish `good fundamentals / weak price` as expectations or positioning pressure, not automatically as a broken thesis.
- Distinguish relative strength from absolute strength. A group that falls less is defensive, not necessarily receiving positive inflows.
- Preserve source uncertainty. State when a catalyst is reported, confirmed, inferred, or unknown.
- Provide analysis, not personalized investment instructions. Frame trade observations as confirmation conditions and risks.

## Source hierarchy

Prefer, in order:

1. Exchange or market-data quotes with explicit timestamps
2. Company investor-relations releases and earnings materials
3. Government and central-bank releases
4. Index-provider and ETF-provider data
5. Reuters, AP, or similarly reputable reporting for market context

Use current links near the claims they support. Do not use search-result snippets as the sole support when the underlying source is available.

## Default communication style

Write in Chinese unless the user asks otherwise. Lead with a one-paragraph regime conclusion, then use compact tables and bullet points. Include exact figures only when verified and round consistently. End with the three to five signals that matter most for the next session or the next two weeks.
