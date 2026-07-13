---
name: ai-infra-five-factor-investing
description: "Analyze AI infrastructure and semiconductor stocks with sector maps, five-factor conviction checks, and disciplined sizing."
---

# AI Infra Five-Factor Investing

Use this skill when Jerry asks to analyze, compare, rank, size, buy/sell, rebalance, or build a watchlist for AI infrastructure / semiconductor names, especially compute, memory, storage, optical, networking, power, packaging, foundry, equipment, OSAT, data center, neocloud, or custom silicon stocks.

This is a workflow skill, not a source of price targets or automatic stock recommendations. Separate the author's framework from JJ-I interpretation and from verified market data.

## Source Frame

Distilled from Damnang's Substack post, "How I Invest in AI Infrastructure" (2026-07-11), plus JJ-I's investment-memory context around AI capex, EPS revision maps, memory/storage, optics, and token-factory themes.

Core idea:

> Invest first in durable AI infrastructure sectors, then use technical / industry mapping to find companies where growth, perception gap, catalysts, and stamina justify conviction. Size by conviction, not by hoped-for upside.

## Workflow

1. Define the sector layer before judging the stock.
   - Classify the name into AI infra layers: compute, custom ASIC, CPU, GPU, memory/HBM, storage, optical lasers/InP, optical DSP, copper/AEC, networking, power, thermal, data center shell, neocloud, packaging, foundry, equipment, OSAT, software/application demand proof.
   - Identify the bottleneck the stock claims to solve.
   - Ask whether the layer benefits from hyperscaler capex duration, especially 2027/2028 AI capex expectations.

2. Build or update the industry map.
   - List upstream inputs, direct customers, substitutes, adjacent technologies, and likely winners if the technology path changes.
   - For complicated layers like optics, power, memory, and packaging, do not jump straight to ticker calls. Explain the technical bottleneck in plain language first.
   - Mark whether the stock is a pure-play bottleneck, diversified beneficiary, or optionality name.

3. Score the five factors qualitatively.
   - **Sector Durability**: Will the sector keep drawing capital and attention? Can we rebut negative headlines? If the stock falls, can we explain whether the decline is thesis-relevant?
   - **Company Growth**: What is the company's technical moat inside its layer? Is hiring, capex, R&D, customer activity, or product roadmap expanding in the direction of AI infra growth?
   - **Theme Resilience**: Can the business survive if one technology route fails or one customer delays? Does it have multiple demand legs, or is it a single-layer/single-customer bet?
   - **Perception Gap**: Is there a structural change in the business that the market still underappreciates? Is the company being misclassified by old narratives?
   - **Catalysts & Stamina**: Are there pre-earnings catalysts such as hyperscaler capex, supplier investment, purchase commitments, policy support, hiring, standards, capacity expansion, or customer wins? Does the company have financial stamina to survive until catalysts become earnings?

4. Translate score into position logic.
   - Large/core position: only when sector durability is high, company growth is visible, theme resilience is acceptable, and conviction is strong enough to sit through volatility.
   - Medium position: several factors are strong, but one major uncertainty remains, such as revenue conversion, technology route, customer concentration, or valuation.
   - Small/trading position: bottleneck may be real, but company stamina, customer concentration, liquidity, or volatility is too risky for serious capital.
   - Avoid/monitor: theme is interesting but evidence is not yet investable, or perception gap already closed.

5. Define buy discipline.
   - Do not chase purely from FOMO.
   - Treat corrections as potential discount windows only after rechecking the five factors.
   - Add when price falls but factor assessment is intact or improved.
   - Prefer building conviction quarter by quarter when revenue proof is not yet visible.

6. Define sell / trim discipline.
   - Sell or cut when sector durability, company growth direction, customer proof, or financial stamina deteriorates.
   - Trim when the perception gap has fully closed and everyone now tells the same story.
   - Use sharp drawdowns as alarms to re-examine the thesis. If the reassessment shows the market knew something first, cut without anchoring to cost basis.
   - Rebalance when position weight no longer matches conviction.

## Ticker Lens Examples

Use these as examples of how to apply the framework, not as standing recommendations.

- **AMD**: AI demand overflow can reward the number two player without AMD beating NVIDIA. CPU/GPU/FPGA legs improve theme resilience.
- **MRVL**: Custom ASIC plus scale-up networking plus optical interconnect can create a data-infrastructure-semiconductor perception gap. Hiring and strategic investment are important catalyst signals.
- **QCOM**: Data center accelerator/custom silicon optionality, but build conviction only as customer wins convert to revenue.
- **CSCO**: Old networking narrative may hide Silicon One, Acacia optics, and security stack exposure.
- **MU**: HBM may structurally improve memory profit pools, but business concentration means sector study must stay current.
- **LITE / COHR**: Lasers and InP capacity can be AI bandwidth bottlenecks; route diversity across EML/CW/VCSEL helps, but single-layer optics exposure requires continuous validation.
- **CRDO / ALAB**: Interconnect names that may benefit across technology path changes, but smaller-company stamina must be checked quarterly.
- **NOK**: Infinera plus AI-RAN optionality creates a possible perception gap; telecom cash flow provides stamina, but AI/optics mix still needs tracking.
- **STM**: Diversified analog/power/sensor/MCU base can dampen portfolio volatility; AI data-center contribution must be verified.

## Output Format

For a single stock, answer in this structure:

- One-line view
- Sector layer and bottleneck
- Five-factor check
- Position logic: core / medium / small-trade / watchlist / avoid
- Buy zone logic or wait-for-proof trigger
- Sell/trim triggers
- Key data to verify next

For a watchlist or comparison, group names by role:

- Core conviction candidates
- Revision-beta / upside candidates
- Optionality names
- Small/trading-only names
- Watchlist until proof

## JJ-I Overlay

Always connect AI infra stock analysis back to the current top-down cycle:

- Hyperscaler capex path, especially 2027/2028 durability.
- Buy-side vs sell-side capex and EPS revision gaps.
- Revenue/GW, utilization, depreciation, financing cost, and FCF conversion for hyperscalers/neoclouds.
- Supplier conversion from capex narrative into orders, capacity, revenue, margin, and EPS.

Risk rule:

> A company can be right about the theme and still fail as an investment if it lacks financial stamina, customer diversity, execution proof, or valuation support.

## Memory Behavior

If Jerry says this analysis is important, asks to remember it, or sends a durable research source, update the relevant AgentBrain note/tracker and today's workspace memory. For normal one-off summaries, do not auto-ingest unless the content is clearly durable specialist material or Jerry asks to save it.
