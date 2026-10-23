# Shared account-review rules

Used by daily-portfolio-review and the Tiger trading-review adapter.

1. Identify account date, market timezone, currency and coverage of positions/orders. Missing data stays unavailable; never turn missing into zero.
2. Prefer broker-reported account/day P&L when available. Identify whether commissions are already included before deducting them. Reconcile cash flows and realized/unrealized figures when provided; do not mistake deposits for performance.
3. Sort position contributions by their account P&L contribution, not simply by percentage price change. Missing cost basis prevents reliable realized-P&L calculation.
4. Net traded notional = total filled buys minus total filled sells. This measures net buying/selling, not profit. Separate orders from fills and list fees separately.
5. Show the denominator for weights. Distinguish equity-only weights from total account weights including cash. Map stocks by verified sector; use underlying exposure for funds and identify diversified funds separately.
6. Compare account and benchmark returns over the same period, timezone and currency. Do not compare a dollar account P&L directly to a benchmark percent return.
7. For GICS and ETF examples, consult sector-mapping.md and gics-mapping.md here; validate current classifications rather than treating example lists as live data.
8. Generation returns a report to the current conversation. Scheduled delivery uses the job's configured destination; interactive external sending requires a user request specifying or establishing the destination.

The full daily report adds beta, concentration, position news and catalysts. The compact Tiger report can omit those sections if not requested; it still follows the accounting rules above.
