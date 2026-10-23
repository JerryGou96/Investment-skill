---
name: catalyst-calendar
description: Build and maintain an investment catalyst calendar for stocks, sectors, crypto, and macro events. Use when Jerry asks for catalyst calendar, upcoming catalysts, earnings calendar, event calendar, catalyst tracker, 未来催化剂, 催化剂日历, 事件日历, 未来4-8周事件, earnings/FOMC/CPI/FDA/conference/product launch/regulatory event tracking, or wants to prioritize positions/watchlist names around upcoming market-moving events.
---

# Catalyst Calendar

Adapted from Anthropic's `financial-services` catalyst-calendar skill for Jerry's OpenClaw/JJ-I workflow.

## Goal

Create a forward-looking calendar of market-moving events across Jerry's coverage universe, watchlist, positions, sectors, crypto themes, and macro calendar. Use it to prioritize attention, risk-manage binary events, and prepare pre/post-event research.

## Inputs to clarify only if missing

- Universe: tickers, positions, watchlist, sector/theme, or “my portfolio”.
- Horizon: default to **next 4-8 weeks** if not specified.
- Region/asset class: default to U.S. equities + relevant macro; include crypto if requested or portfolio includes it.
- Output: default to concise Markdown; create CSV/Excel only if requested.

## Mandatory live verification

Catalyst dates are mutable. Before producing a calendar, verify with current sources when possible:

- Earnings: company IR pages, Nasdaq/NYSE/company events pages, earnings calendars, yfinance if available.
- Macro: Fed/FOMC calendar, BLS, BEA, Census, Treasury, official central bank/economic-release calendars.
- Company/industry events: IR events pages, conference agendas, regulatory calendars, product launch pages, FDA/PDUFA calendars where relevant.
- Existing portfolio/watchlist data: use Jerry's local tools/skills when relevant.

If a date is unverified or tentative, mark it clearly as **tentative/unconfirmed**.

## Event types to capture

- **Earnings & financial**: earnings date/time, guidance updates, investor/analyst day, shareholder meeting, dividend/ex-date, debt maturity/refinancing.
- **Corporate**: product launch, M&A milestone, management change, lockup expiration, major customer/supplier contract event.
- **Regulatory**: FDA/PDUFA, antitrust decision, policy deadline, court/ruling dates.
- **Industry**: conferences, trade shows, monthly industry data, competitor launches, supply-chain events.
- **Macro**: FOMC, CPI, PPI, NFP, GDP, retail sales, Treasury refunding/auctions, major central bank decisions.
- **Crypto**: protocol upgrades, unlocks, ETF/regulatory deadlines, major ecosystem conferences, token-specific events.

## Output format

Use this table unless Jerry asks otherwise:

| Date | Event | Ticker/Sector | Type | Impact | Status | Why it matters | Prep / positioning notes | Sources |
|---|---|---|---|---|---|---|---|---|

Impact: **High / Medium / Low**.  
Status: **confirmed / tentative / unconfirmed**.

Then add:

1. **This week's key events** — bullets ranked by importance.
2. **Next 2-4 weeks watchlist** — early heads-up.
3. **Portfolio/watchlist implications** — what could move Jerry's positions or watchlist.
4. **Research follow-ups** — questions to answer before the event.
5. **Post-event review hooks** — what data/outcome to check afterward.

## Analysis rules

- Separate **date certainty** from **impact estimate**.
- Do not recommend trades purely because an event exists; frame as research/risk-management prep.
- For binary/high-volatility events, call out gap risk and position-sizing relevance.
- For earnings, include consensus/expectations if available and explicitly label source.
- For macro events, state the market-sensitive variable: inflation surprise, labor cooling/tightness, Fed path, yields, USD, liquidity, etc.
- Archive useful past outcomes when Jerry asks to maintain a recurring tracker.

## If building a recurring tracker

Maintain columns for: `date`, `ticker`, `event_type`, `event_name`, `confirmed_status`, `source_url`, `expected_metric`, `actual_outcome`, `price_reaction_1d`, `price_reaction_5d`, `notes`, `follow_up_needed`.
