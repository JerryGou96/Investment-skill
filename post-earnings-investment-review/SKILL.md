---
name: post-earnings-investment-review
description: "Generate a focused post-earnings investment review: verdict, beat/miss, expectations gap, price reaction, business mix, valuation/PEG, risk-reward, and watch items."
---

# Post-Earnings Investment Review

Generates a focused post-earnings investment review using Yahoo Finance data, company releases, and market context. Prioritize what moved the stock and what changed for the thesis; do not bury the lede in generic tables.

**Important**: Data is for research and educational purposes only. Not financial advice. yfinance is not affiliated with Yahoo, Inc.

---

## Step 1: Ensure yfinance Is Available

**Current environment status:**

```
!`python3 -c "import yfinance; print('yfinance ' + yfinance.__version__ + ' installed')" 2>/dev/null || echo "YFINANCE_NOT_INSTALLED"`
```

If `YFINANCE_NOT_INSTALLED`, install it:

```python
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "yfinance"])
```

If already installed, skip to the next step.

---

## Step 2: Identify the Ticker and Gather Data

Extract the ticker from the user's request. Fetch all relevant post-earnings data in one script.

```python
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

ticker = yf.Ticker("AAPL")  # replace with actual ticker

# --- Earnings result ---
earnings_hist = ticker.earnings_history

# --- Financial statements ---
quarterly_income = ticker.quarterly_income_stmt
quarterly_cashflow = ticker.quarterly_cashflow
quarterly_balance = ticker.quarterly_balance_sheet

# --- Price reaction ---
# Get ~30 days of history to capture the reaction window
hist = ticker.history(period="1mo")

# --- Context ---
info = ticker.info
news = ticker.news
recommendations = ticker.recommendations
```

### What to extract

- `earnings_history`: EPS estimate, actual, difference, surprise percent.
- Company release / 8-K / call: revenue, segment revenue, guidance, margin, FCF, management target language.
- `quarterly_income_stmt`: revenue, gross profit, operating income, net income, EPS.
- `quarterly_cashflow`: operating cash flow, capex, free cash flow.
- `history()`: close before print, after-hours/next-session reaction, recent run-up into print.
- `info`: current price, market cap, EV, trailing/forward P/E, PEG, P/S, EV/revenue, EV/EBITDA, FCF, growth, target price.
- News / consensus sources: reported consensus, whisper/buy-side bar if available, and post-earnings analyst framing.

---

## Step 3: Determine the Most Recent Earnings

The most recent earnings result is the first row (most recent date) in `earnings_history`. Use its date to:

1. **Identify the earnings date** for the price reaction analysis
2. **Match to the corresponding quarter** in the financial statements
3. **Calculate stock price reaction** — compare the close before earnings to the next trading day's close (or open, depending on whether earnings were before/after market)

### Price reaction calculation

```python
import numpy as np

# Find the earnings date from earnings_history index
earnings_date = earnings_hist.index[0]  # most recent

# Get daily prices around the earnings date
hist_extended = ticker.history(start=earnings_date - timedelta(days=5),
                                end=earnings_date + timedelta(days=5))

# The reaction is typically measured as:
# - Close on the last trading day before earnings -> Close on the first trading day after
# Be careful with before/after market reports
if len(hist_extended) >= 2:
    pre_price = hist_extended['Close'].iloc[0]
    post_price = hist_extended['Close'].iloc[-1]
    reaction_pct = ((post_price - pre_price) / pre_price) * 100
```

**Note**: The exact reaction window depends on when the company reported (before market open vs after close). The price data will reflect this — look for the biggest gap between consecutive closes near the earnings date.

---

## Step 4: Build the Earnings Recap

### Section 1: Verdict First

Start with a direct 2-4 sentence judgment:
- Was the print strong, weak, mixed, or deceptively strong?
- Why did the stock move the way it did?
- Is the issue fundamentals, expectations, valuation, positioning, or guidance language?
- State the actionable stance: chase, wait, hold, trim, buy-the-dip candidate, or avoid.

For strong reports with weak price action, explicitly frame:
"The quarter was strong; the stock is reacting to expectations/valuation, not a broken thesis."

### Section 2: Report Card vs. Expectations

Show only the metrics that matter for the company. Include:
- Revenue actual vs. consensus and company guide
- EPS actual vs. consensus and whisper/buy-side bar if available
- Segment/key product revenue vs. guide
- Margin and FCF
- Next-quarter guidance vs. consensus
- Management target changes or refusal to raise targets

Interpretation rule:
- A report can be a consensus beat but still disappoint if it misses whisper numbers, does not raise an important annual target, or fails to expand the story.
- Label uncertain whisper numbers clearly as market chatter or buy-side bar, not official consensus.

### Section 3: What Actually Changed

Focus on business structure, not just total growth:
- Which segment/product drove the quarter?
- How much growth came from the core bull thesis versus legacy/cyclical lines?
- Is non-core weakness hidden by one strong segment?
- Did margin/FCF improve because of durable mix, operating leverage, or temporary cost control?
- Did guidance require an unusually steep sequential ramp?

For AI/semiconductor/software names, always separate:
- AI or high-growth product revenue
- Non-AI / legacy / cyclical revenue
- Software or recurring cash-flow contribution
- Customer concentration and hyperscaler capex timing risk

Calculate margins from raw financials when available:
- Gross margin = gross profit / revenue
- Operating margin = operating income / revenue
- FCF margin = free cash flow / revenue
- Sequential growth implied by next-quarter guidance

### Section 4: Stock Price Reaction

Explain the price move through a hierarchy:
- Pre-earnings run-up and positioning
- Consensus beat/miss
- Whisper/buy-side expectation gap
- Guidance quality and whether targets were raised
- Valuation and crowding
- Market/sector tape on the same day

For post-earnings selloffs after strong numbers, explicitly answer:
- What was the market hoping to hear?
- What did management not say?
- Is the selloff thesis-breaking or expectation reset?

### Section 5: Valuation & Expectations

Always include a concise valuation read when enough data is available. Pull from `ticker.info`, recent price, financial statements, and company guidance.

Core metrics to check:
- Market cap and enterprise value
- Trailing P/E and forward P/E
- PEG ratio, if available
- EV/revenue and EV/EBITDA
- Price/sales
- Free cash flow yield: `freeCashflow / marketCap`
- Revenue growth and earnings growth
- Analyst target price context if available

Interpretation rules:
- Compare valuation to the new growth profile, margin trend, and forward guidance rather than judging multiples in isolation.
- Use PEG as a sanity check for whether the P/E premium is justified by earnings growth, but flag when it is stale or distorted by one-time estimate revisions.
- Flag whether the quarter was a true estimate reset, an in-line beat, or a high-expectation print where good news may already be priced.
- For high-growth AI/software names, explicitly separate fundamental quality from valuation risk.
- If valuation metrics are missing or stale in Yahoo Finance, say so and use official guidance plus market cap/price as a rough framing.

Output should answer:
- Is the stock cheap, fair, or expensive relative to the updated growth and margin profile?
- Did the earnings report increase, reduce, or merely confirm the valuation premium?
- What price zone or multiple would make risk/reward more attractive, if the data supports that view?

### Section 6: Stance, Levels, and Watch Items

End with the highest-signal trading/investment read:
- Stance: positive/neutral/negative, and whether it is a buy-the-dip candidate.
- Entry discipline: avoid chasing; identify support/valuation zones only when supported by price data.
- Confirmation items before adding: call commentary, 10-Q, target/backlog language, segment recovery, customer concentration, capex timing.
- Main risks: demand timing, guide execution, concentration, valuation compression, sector rotation.

---

## Step 5: Respond to the User

Present the recap as a short investment memo, not a data dump:

1. Lead with verdict and stock-reaction explanation.
2. Then give the key numbers in compact bullets.
3. Include a "why it moved" section when price action conflicts with headline results.
4. Highlight business mix: growth driver, weak spots, margin/FCF quality, and guidance ramp.
5. Include valuation/PEG/FCF yield context.
6. End with stance, price/risk-reward discipline, and what to confirm next.

Avoid generic praise like "strong quarter" unless followed by what matters. Prioritize the 3-5 factors that actually explain the thesis and the stock move.

### Caveats to include
- Yahoo Finance data may not include all details from the earnings call (guidance, segment breakdowns)
- Revenue estimates are harder to compare precisely — yfinance provides YoY comparison from financial statements
- Price reaction may be influenced by broader market moves on the same day
- Valuation fields from Yahoo Finance can lag after earnings; label stale or approximate figures clearly
- Whisper/buy-side expectation numbers are not official consensus; label source quality
- This is not financial advice

---

## Reference Files

- `references/api_reference.md` — Detailed yfinance API reference for earnings history and financial statement methods

Read the reference file when you need exact method signatures or to handle edge cases in the financial data.
