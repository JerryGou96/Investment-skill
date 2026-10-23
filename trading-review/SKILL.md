---
name: trading-review
description: Generate a compact daily review from a configured Tiger Brokers read-only account adapter, including account P&L, sector exposure and filled trades. Use for Tiger account reviews or a scheduled trading-review job; general uploaded portfolio data belongs to daily-portfolio-review.
---

# Tiger Trading Review

This skill handles Tiger data acquisition and compact delivery formatting. It depends on `daily-portfolio-review`, which owns shared account-review rules.

## 1. Read account data

Use `scripts/read_account.py` relative to this skill directory. It reads local adapter configuration from `TRADING_REVIEW_CONFIG` or `~/.openclaw/local-config/trading-review.json`, then runs the configured Tiger directory's `.venv/bin/python3 read_only.py`. Do not use the system interpreter for the broker script. This helper is read-only and does not submit orders.

```bash
python3 scripts/read_account.py
```

For first-time setup, copy `config.example.json` outside this skill folder to the local config location and set `tiger_api_dir`. Broker credentials remain in the broker adapter's existing local configuration. If unavailable, report the acquisition error and use supplied data when available.

## 2. Apply the common review core

Read `../daily-portfolio-review/references/review-core.md` and its `gics-mapping.md`. If the dependency is absent, stop with an actionable installation message; do not silently substitute different accounting rules. Pull dated SPY/QQQ returns with the same cutoff as account data.

## 3. Produce the compact report

Use Discord-friendly bullets or monospace blocks, without wide tables:

- Date and account-data cutoff; account net P&L and return if derivable, plus SPY/QQQ benchmarks.
- Positions: symbol, day change, market value and contribution when available.
- Sector exposure: market value, weight and denominator.
- Filled trades: buys, sells, net bought/sold, new/add/reduce/closed positions when supported by the records.
- Realized gains/losses, fees and expired options only when supported by data. Never equate net sold notional with realized profit.
- Reflection area for the user; missing or incomplete-data notes.

For a full risk/beta/news/catalyst report, continue with `daily-portfolio-review` using the acquired data rather than duplicating its workflow here.

## 4. Delivery

Return the report in the current conversation by default. For an existing scheduled job, follow that job's delivery configuration and avoid sending a second copy if the scheduler delivers it. If the user explicitly requests an external send, use the destination established by the request or local config. A destination stored in config alone is not an instruction to send.

No channel ID, account ID, private key or personal filesystem path belongs in the distributable skill.
