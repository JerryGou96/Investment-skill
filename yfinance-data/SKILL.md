---
name: yfinance-data
description: "Fetch requested price history, quotes, financial statements, options or other Yahoo Finance data via yfinance. Use for explicit data retrieval or as a helper for an analysis workflow; a bare ticker alone does not determine user intent."
---

# yfinance Data Skill

Fetches financial and market data from Yahoo Finance using the yfinance Python library.

## Usage

When the user asks for stock data, use Python with yfinance.

### Setup check

First verify yfinance is available:

```python
import importlib.util
print("installed" if importlib.util.find_spec("yfinance") else "missing")
```

If missing, install it:

```python
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "yfinance"])
```

## Common tasks

- Current quote: `yf.Ticker("AAPL").info` or `.fast_info`
- Price history: `ticker.history()` or `yf.download()`
- Income statement: `ticker.income_stmt`
- Balance sheet: `ticker.balance_sheet`
- Cash flow: `ticker.cashflow`
- Earnings / analyst targets / recommendations / options / dividends

## Rules

1. Always use try/except because Yahoo may rate-limit.
2. Use `yf.download()` for multiple tickers.
3. For quarterly financials, use `quarterly_` variants.
4. For readable output, convert DataFrames with `.to_markdown()` or select key columns.
5. Prefer direct data extraction over browser scraping when possible.

## Outputs

For Jerry, default to:
- clear conclusion first
- then supporting data
- tables when useful

See `references/api_reference.md` for sample code patterns.
