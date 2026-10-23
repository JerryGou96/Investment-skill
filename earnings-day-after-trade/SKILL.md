---
name: earnings-day-after-trade
description: >
  Build and execute a structured post-earnings next-day intraday trade plan using
  the opening-range breakout/breakdown framework. Use when the user wants an
  earnings day-after trade setup, asks how to trade the morning after earnings,
  wants long/short triggers from the first 1-3 minutes, needs invalidation and
  stop logic, or references a trader's "day after trade" process. Triggers
  include: "earnings day after trade", "day after earnings setup",
  "opening range after earnings", "how to trade tomorrow after earnings",
  "post-earnings breakout", "long above opening high", "short below opening low",
  or requests for a repeatable next-day earnings trading playbook.
---

# Earnings Day After Trade

## Overview

Use this skill to turn a post-earnings idea into a rules-based next-day trade plan.
Anchor on the first valid opening range, trade only confirmed breaks, and cut fast when the break fails.

## Workflow

### 1. Confirm the setup deserves a day-after trade

Proceed only when most of these are true:
- Earnings or guidance created a real catalyst.
- The stock has elevated volume, gap, or unusual premarket attention.
- There is a clean narrative: strong beat, weak guide, sell-the-news, sympathy move, or sector read-through.
- The stock normally moves enough intraday to pay for the risk.

Avoid forcing the setup when:
- The stock barely reacted to earnings.
- Premarket range is tiny and volume is dead.
- The name is illiquid or spreads are sloppy.
- The user wants a swing thesis rather than an intraday trade.

### 2. Build the premarket plan

Before the open, define:
- The earnings/guidance takeaway.
- Bias: bullish, bearish, or two-sided.
- Key levels from the prior day, premarket high/low, gap fill, and obvious support/resistance.
- Which side would confirm continuation vs failure.

If live market data is needed, use available market-data skills or yfinance for recent price context, but state clearly when premarket or real-time data is unavailable.

### 3. Wait for a valid opening range

Do **not** trigger from the first random print.
Let the market build a real top and bottom first.

Default opening-range rule:
- Start with the first **1-3 minutes** after the open.
- Extend to **5 minutes** only if the first minutes are chaotic, spreads are wide, or prints look unreliable.
- Record the opening-range **high**, **low**, and approximate **midpoint**.

The goal is a definable box, not a fixed clock.

### 4. Trigger the trade

Trade only on confirmation:
- **Long** when price breaks and holds above the opening-range high.
- **Short** when price breaks and holds below the opening-range low.

Prefer the break when:
- Volume expands.
- The move aligns with the earnings narrative.
- The stock is moving with its sector or peer group.
- The breakout is not immediately rejected.

Do **not** chase extended candles far beyond the trigger unless the user explicitly wants aggressive momentum entries.

### 5. Invalidation and stop logic

Treat this as a robotic trade.
If wrong, exit quickly.

Default invalidation:
- Long: fail back into the range or lose the breakout candle low.
- Short: reclaim the range or lose the breakdown candle high.

Risk rules:
- Define risk before entry.
- Keep size smaller than a normal intraday trade when earnings volatility is extreme.
- If the opening range is too wide for sensible sizing, pass.

### 6. Manage the winner

Use simple management first:
- First target: 1R or the next obvious level.
- Then trail using higher lows for longs or lower highs for shorts.
- If the stock trends cleanly, allow for a runner because strong day-after trades can persist for many points.

If the move stalls immediately after the break:
- Reduce size.
- Tighten the stop.
- Be willing to scratch the trade.

### 7. Produce the trading plan for the user

When responding, give a compact execution plan with:
- Earnings takeaway.
- Bias.
- Opening-range method to use.
- Long trigger.
- Short trigger.
- Stop/invalidation.
- First and second targets.
- Specific no-trade conditions.

Use this template:

```text
Ticker:
Catalyst:
Bias:
Opening-range rule:
Long only above:
Short only below:
Initial stop:
Target 1:
Target 2 / runner logic:
No-trade if:
```

## Guardrails

- Do not present this as guaranteed or easy money.
- Do not invent live prices when real-time data is unavailable.
- Say clearly when levels are illustrative versus live.
- Prefer no trade over a messy trade.
- If the user asks for a backtest or deeper playbook examples, read `references/playbook.md`.

## Reference files

- `references/playbook.md` — checklist, filters, and example plan formats for bullish and bearish earnings day-after trades.
