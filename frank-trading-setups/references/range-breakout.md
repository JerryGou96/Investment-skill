# Volume Range Breakout Setup

Framework source: Frank Trading Substack post `10/19/2025真正的干货：实战中我最喜欢的setup`; accessible public portion states: long-term high-volume sideways consolidation, then huge-volume break out of the range, tradable both upward and downward. Treat the rest as Jerry's/internal trading framework, not a verbatim copy of paid content.

## Core Pattern

A high-conviction momentum continuation/reversal setup:

1. **Long sideways range**: price spends enough time in a visible box/base, with clear upper/lower boundaries.
2. **Volume stays active during the range**: repeated elevated/meaningful volume suggests accumulation, distribution, position transfer, or institutional interest.
3. **Decisive expansion candle**: price breaks above range resistance or below range support with a clear volume spike.
4. **Follow-through or clean retest**: avoid chasing if breakout immediately fails back into the box.

Works in both directions:
- **Long**: range high breaks on huge volume.
- **Short**: range low breaks on huge volume.

## Data to Check

Use live chart/market data when possible:
- Daily and 4H candles; weekly for context.
- Range duration: ideally multi-week to multi-month; shorter intraday ranges require lower conviction.
- Range width: percent distance between support/resistance.
- Volume ratio: breakout volume vs 20D average volume.
- Relative strength/weakness vs SPY/QQQ and sector peers.
- Market regime: risk-on/risk-off, sector trend, liquidity/event risk.
- Catalyst: earnings, guidance, product, macro, ETF flow, crypto narrative, news.

## Setup Quality Score

Grade A/B/C/Reject.

**A setup**
- Range is obvious and has at least 3 clean touches/failed attempts.
- Breakout volume >= 2x 20D average, or visibly largest in weeks/months.
- Break candle closes outside the box, preferably near the extreme.
- Name shows relative strength for longs / relative weakness for shorts.
- Market/sector backdrop supports direction.
- Stop is clear and risk-reward >= 2:1.

**B setup**
- Range is valid but not perfect, or volume is strong but not exceptional.
- Breakout closes outside the range but candle has some wick/extension.
- Market/sector backdrop is neutral.
- Risk-reward is acceptable, not outstanding.

**C setup**
- Breakout exists but range is messy/short, volume ambiguous, or entry is late.
- Needs retest confirmation; do not chase.

**Reject**
- Breakout without volume.
- Price re-enters the box quickly.
- Stop is too wide or risk-reward < 1.5:1.
- Breakout happens directly into major resistance/support.
- Event risk is binary and unmanaged.

## Entry Playbook

Prefer one of two entries:

1. **Breakout entry**
   - Enter when price breaks range boundary with confirmed volume.
   - Best when volume is exceptional and candle is not too extended.

2. **Retest entry**
   - Wait for price to retest the breakout level and hold.
   - Best when initial breakout candle is too large or extended.

Avoid entering in the middle of the old range.

## Stop Logic

Choose the tightest logical invalidation level that avoids normal noise:

- Long: below breakout level after retest, below breakout candle low, or back inside box.
- Short: above breakdown level after retest, above breakdown candle high, or back inside box.
- If stop distance is too large, reduce size or skip.

## Target Logic

Use multiple target methods and pick realistic zones:

- Measured move: range height projected from breakout point.
- Prior high/low or supply/demand zone.
- ATR extension: avoid taking first entry if price is already far beyond normal move.
- Scale plan: trim at 1R/2R, trail remainder if trend accelerates.

## Risk Controls

- Do not force setup in weak liquidity names unless position size is small.
- For earnings-driven breakouts, separate technical setup from binary event risk.
- If market index is breaking down, downgrade long setups unless the name has exceptional RS.
- If market is squeezing/risk-on, downgrade shorts unless the name has clear idiosyncratic weakness.
- Never average down inside a failed breakout.

## Output Format

When analyzing a ticker, answer in this structure:

```markdown
**Setup verdict:** A/B/C/Reject — Long/Short/No trade

**Why:**
- Range: ...
- Volume: ...
- Breakout/breakdown quality: ...
- Relative strength/market context: ...

**Trade plan:**
- Entry: ...
- Stop / invalidation: ...
- Targets: ...
- R:R: ...
- Position sizing note: ...

**What would change my mind:**
- ...
```

Keep the conclusion direct. If the setup is not clean, say so and recommend waiting for retest or skipping.

## Additional context preserved from the Frank entrypoint

### Behavioral Logic

- Elevated volume means disagreement and active share transfer.
- Long sideways trading creates accumulation/distribution and washes out weaker holders.
- After enough turnover, supply above the range can become thin because many earlier sellers already sold.
- New buyers inside the range often have higher target prices, so the marginal sell wall moves upward.
- This creates the classic “long base, strong vertical move” dynamic.

### Preferred Examples / Pattern Anchors

Use these as mental anchors, not as exact historical claims to repeat unless verified live:
- GC: multi-month high-volume range before breakout and trend acceleration.
- TSLA: high-volume range into breakout.
- NVDA: long 2023–early 2024 consolidation before breakout.
- HOOD: long base, then earnings/catalyst ignited move.



## Range duration and options

Prefer multi-month bases (3+ months in the original Frank notes); shorter bases need lower confidence. If options are requested, the original framework uses 3–6 month calls/call spreads for high-conviction equity longs. These are framework preferences, not a substitute for current liquidity, implied volatility, or the user's horizon.
