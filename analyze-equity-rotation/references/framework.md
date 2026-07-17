# Equity and AI Rotation Framework

## Contents

1. Market layers
2. Starter universe
3. AI taxonomy
4. Metrics
5. Rotation score
6. Interpretation patterns

## 1. Market layers

Analyze four nested layers:

1. **Regime:** risk appetite, capitalization, style, rates, volatility, credit, dollar, and breadth.
2. **Traditional sectors:** the 11 GICS sectors and relevant industries.
3. **AI industry chain:** compute through applications, including infrastructure bottlenecks.
4. **Stock validation:** leaders, second-line suppliers, and breadth within each custom basket.

Use at least two time scales:

- Tactical: 1-day and 5-day
- Trend: 20-day and 60-day

When possible, add a catalyst horizon:

- Immediate: next session to two weeks
- Fundamental: one to two earnings cycles

## 2. Starter universe

Verify that every security is current, correctly classified, and actively traded before use. This is a seed list, not a permanent source of truth.

### Regime and style

| Question | Common proxies |
|---|---|
| Broad market | SPY, QQQ, DIA, IWM |
| Equal weight | RSP, QEW or a verified Nasdaq equal-weight proxy |
| Growth/value | IWF, IWD |
| High beta/low volatility | SPHB, SPLV |
| Semiconductors | SOXX, SMH, SOX index when available |
| Software | IGV or another verified software proxy |
| Volatility | VIX; MOVE for rates volatility |
| Credit | HYG, LQD, or verified option-adjusted spreads |

### Traditional sectors

Use XLK, XLC, XLY, XLP, XLF, XLV, XLI, XLB, XLE, XLU, and XLRE as common liquid proxies. Confirm sector definitions and quote timestamps.

## 3. AI taxonomy

Use custom equal-weight baskets because many narrow themes lack clean ETFs. Prefer at least three names per basket; if fewer are available, label the result low-confidence.

| AI sub-sector | Exposure | Representative starting points to verify |
|---|---|---|
| Compute | GPU, CPU, ASIC accelerators | NVDA, AMD, AVGO |
| Foundry and packaging | Leading-edge wafer and advanced packaging | TSM, INTC, AMKR |
| Semiconductor equipment | Lithography, deposition, etch, cleaning, inspection/metrology, advanced packaging and test | ASML, AMAT, LRCX, KLAC, ONTO, CAMT, TER, COHU |
| Memory and storage | HBM/DRAM, NAND, HDD, enterprise storage | MU, SNDK, WDC, STX |
| Optical connectivity | 800G/1.6T, EML/DFB, silicon photonics, coherent/DCI | COHR, LITE, CIEN, MTSI, GLW |
| Networking | Switch silicon, Ethernet/InfiniBand, DPU/NIC | ANET, MRVL, AVGO, CSCO |
| PCB and interconnect | PCB/CCL, connectors, copper, test | Build from current listed suppliers; regional baskets may be required |
| Data-center systems | Servers, racks, storage systems, ODM exposure | DELL, SMCI, HPE |
| Power and cooling | UPS, power distribution, transformers, liquid cooling | VRT, ETN, GEV, HUBB |
| Energy supply | Nuclear, utilities, gas and power generation | CEG and other verified direct beneficiaries |
| Cloud and neocloud | Hyperscale cloud and GPU rental | MSFT, AMZN, GOOGL, ORCL, CRWV |
| Software infrastructure | Data, observability, databases, developer tools | SNOW, DDOG, MDB, ESTC |
| AI applications | Enterprise workflows and monetizing applications | PLTR, NOW, CRM, ADBE |
| Robotics and edge AI | Industrial automation, robotics, edge processors | Build a verified basket appropriate to the market requested |

Assign each company to one primary basket for scoring. Mention secondary exposures qualitatively.

### Semiconductor equipment is a required independent group

Do not fold semiconductor equipment into foundry/packaging. Its earnings and price cycle is driven by wafer-fab equipment spending, process complexity, capacity additions, memory/logic mix, advanced packaging, export controls, bookings, backlog, and service revenue. It can therefore lead or lag foundries and chip designers.

When data permits, split the group into:

- Lithography: verify ASML and relevant regional suppliers
- Deposition and etch: verify AMAT, LRCX and relevant regional suppliers
- Inspection and metrology: verify KLAC, ONTO, CAMT and relevant regional suppliers
- Cleaning and thermal processing: build a verified regional basket
- Advanced packaging, bonding and assembly equipment: verify KLIC, BESI and direct peers
- Test and handlers: verify TER, COHU and direct peers

Use ASML, AMAT, LRCX and KLAC as a liquid core basket only after checking current listings and exposures. Add ONTO/CAMT for advanced-packaging inspection and TER/COHU for test when the requested scope warrants it. Do not treat SOXX or SMH as pure equipment proxies because chip designers and manufacturers dominate them.

For fundamental confirmation, track:

- Foundry, logic and memory capex revisions
- Equipment bookings, backlog, shipment timing and service growth
- Leading-edge node and layer-count intensity
- Advanced-packaging capacity and hybrid-bonding adoption
- China revenue exposure and export-control changes
- Utilization recovery at memory and mature-node fabs

Interpretation examples:

- Equipment outperforming compute and foundry over 5-day and 20-day windows, with rising capex or bookings, supports upstream capex expansion.
- Equipment falling less during an AI selloff is only relative defense unless absolute price, breadth and revisions improve.
- Strong foundry demand with weak equipment orders can mean existing capacity is sufficient, capex is delayed, or expectations were already priced; investigate before inferring a broken AI thesis.

For deeper optical analysis, optionally split into:

- Pluggable 800G/1.6T modules
- EML/DFB lasers
- Silicon photonics
- DSP
- Micro TEC
- FAU/glass bridge
- Coherent DCI
- CPO/NPO
- Fiber and connectors

For deeper memory analysis, optionally split into:

- HBM
- Commodity DRAM
- NAND
- Enterprise SSD/HDD
- Memory equipment
- CXL/CDB
- Testing and packaging

Do not force a public-equity basket when the pure-play suppliers are private or listed only in another region. Say so and use upstream/downstream proxies carefully.

## 4. Metrics

### Price and relative strength

For group `g` and benchmark `b`:

\[
RS_{g,b,t}=R_{g,t}-R_{b,t}
\]

Calculate 1-day, 5-day, 20-day, and 60-day returns when verified. Use both:

- Equal-weight basket return: participation and typical member
- Market-cap-weighted return: index and portfolio impact

### Breadth

Useful measures include:

\[
Breadth_{20}=\frac{\text{members above 20-day moving average}}{\text{valid members}}
\]

- Members above 20-day and 50-day moving averages
- Advancers/decliners
- New highs/new lows
- Fraction outperforming SPY or QQQ
- Up-volume/down-volume
- Median member return versus basket return

### Leadership and dispersion

Compare:

- Leaders versus second-line suppliers
- Basket average versus median
- Best and worst constituent
- Equal-weight versus capitalization-weighted return

A rising cap-weighted basket with weak median participation is concentrated leadership, not broad confirmation.

### Fundamentals

Track only evidenced changes:

- Revenue, EPS, gross margin, and free-cash-flow revisions
- Hyperscaler capex and AI revenue
- Orders, backlog, shipments, capacity, utilization, and lead times
- Sampling, validation, qualification, ramp, and revenue-recognition timing
- Supply constraints and price changes

Classify the price/fundamental matrix:

| Price | Fundamentals | Interpretation |
|---|---|---|
| Strong | Strong | Healthy leadership |
| Strong | Weak/flat | Sentiment, multiple, or crowding risk |
| Weak | Strong | Expectations digestion or potential dislocation |
| Weak | Weak | Confirmed deterioration |

## 5. Rotation score

Use a 100-point score only when the data is sufficiently complete. Otherwise provide the component evidence without a false-precision total.

| Component | Weight | Evidence |
|---|---:|---|
| Relative strength | 25 | 5-day, 20-day, 60-day excess return |
| Momentum change | 15 | Acceleration or deceleration in relative strength |
| Breadth | 15 | Participation above moving averages and benchmark |
| Volume confirmation | 10 | Relative volume and up/down-volume behavior |
| Earnings/fundamental revisions | 15 | Direction and breadth of estimate changes |
| Catalysts | 10 | Confirmed near-term events and fundamental milestones |
| Valuation/crowding | 10 | Valuation percentile, positioning, and price extension |

Default labels:

- 75–100: Leading
- 60–74: Improving
- 40–59: Neutral or Unconfirmed
- 25–39: Weakening
- 0–24: Lagging

Do not score missing components as zero. Either normalize disclosed components transparently or omit the composite.

## 6. Interpretation patterns

### Concentrated leadership

Large AI leaders rise while equal-weight AI, second-line suppliers, and breadth lag. Interpret as certainty-seeking, not healthy expansion.

### Upstream bottleneck expansion

Compute consolidates while memory, optics, networking, power, or cooling gain relative strength with breadth confirmation. Interpret as infrastructure expansion.

### Hardware-to-application rotation

Hardware relative strength weakens while a broad software/application basket, not one stock, strengthens over 5-day and 20-day windows. Confirm with improving revenue or estimate evidence.

### Second-line catch-up

Leaders consolidate while suppliers show improving breadth and volume. Treat as catch-up only if the move persists beyond one session.

### Defensive rotation

Technology weakens while healthcare, staples, utilities, real estate, and low volatility strengthen. Distinguish this from healthy cyclical broadening by checking financials, industrials, materials, small caps, credit, and rates.

### Local AI de-risking

AI hardware falls sharply while equal-weight broad-market performance remains healthy and volume is not capitulatory. Interpret as localized crowding reduction unless breadth and credit deteriorate broadly.
