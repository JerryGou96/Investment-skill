# Earnings Day-After Trade Playbook

## Quick checklist

Use this setup only when at least 4 of 6 are true:
- Clear earnings or guidance catalyst
- Stock gapped materially or had outsized after-hours move
- Premarket volume is clearly active
- There is an obvious narrative continuation or failure thesis
- Opening-range width is tradable relative to account risk
- The stock has room to move beyond the first target

## Opening-range selection

### Use 1 minute when
- Price discovery is clean
- Spreads are tight
- Volume is heavy and orderly

### Use 3 minutes when
- The first minute is noisy but still usable
- You want fewer fake breaks
- The stock is liquid but emotional

### Use 5 minutes when
- The open is chaotic
- The range is whipping on both sides
- Large-cap mega momentum names are printing erratically

## Common filters

Skip the trade when:
- The trigger is already too extended from the range by the time you notice it
- Breakout volume is weak
- Sector ETF and peers are moving the other way
- The stock immediately re-enters the range twice
- The opening range is so wide that the stop ruins position sizing

## Example bullish plan

```text
Ticker: CLS
Catalyst: Strong earnings and raised guide, but initial sell-the-news reaction
Bias: Two-sided with upside recovery potential
Opening-range rule: Use first 3 minutes unless first minute is very clean
Long only above: Opening-range high after hold/acceptance
Short only below: Opening-range low if rejection continues
Initial stop: Back inside range or below breakout candle low
Target 1: 1R
Target 2 / runner logic: Prior intraday resistance, then trail higher lows
No-trade if: Range is too wide, breakout fails instantly, or volume fades hard
```

## Example bearish plan

```text
Ticker: AMD
Catalyst: Hot stock with post-earnings disappointment and heavy positioning
Bias: Bearish unless opening low holds and reclaims range
Opening-range rule: Use 3-5 minutes because first minute may contain noise
Long only above: Opening-range high only if sector also firms up
Short only below: Opening-range low on volume expansion
Initial stop: Back inside range or above breakdown candle high
Target 1: 1R or prior premarket support
Target 2 / runner logic: Trend lower using lower highs
No-trade if: Breakdown lacks follow-through or semis reverse sharply higher
```

## Response style

Keep the trading plan short and executable.
Prefer concrete triggers and invalidation over long explanations.
If live data is missing, say that the user should apply the framework to the actual first 1-3 minute range after the open.
