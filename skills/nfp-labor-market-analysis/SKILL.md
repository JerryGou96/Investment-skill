---
name: nfp-labor-market-analysis
description: Analyze U.S. Employment Situation / Nonfarm Payrolls (NFP) reports using JJ-Macro's labor-market framework. Use when Jerry asks to analyze, recap, compare, or preview NFP, jobs report, unemployment rate, payrolls, household survey, establishment survey, labor force participation, not-in-labor-force, employment population, U-6, wages, or monthly labor-market data, including phrases like “分析 NFP”, “四月非农”, “jobs report 怎么看”, or “按我们的 NFP 框架”.
---

# NFP Labor Market Analysis

## Core requirement

Always verify the report with live official or primary data before analyzing. Prefer BLS Employment Situation release and tables first; use market consensus/reaction sources only for estimates and asset moves.

Official source pattern:
- Current release: `https://www.bls.gov/news.release/empsit.htm`
- Archive: `https://www.bls.gov/news.release/archives/empsit_<MMDDYYYY>.htm`

## Analysis workflow

1. Identify the report month and release date. If the user says “this month / last month / 四月”, map it to the exact Employment Situation report month and state the date.
2. Pull actual vs consensus when available:
   - Headline nonfarm payrolls
   - Unemployment rate
   - Average hourly earnings MoM/YoY
   - Labor force participation rate
3. Separate the two surveys:
   - Establishment Survey = payroll jobs, industries, wages, hours
   - Household Survey = employed persons, unemployed persons, labor force, not in labor force, participation, employment-population ratio
4. Decompose unemployment-rate change using Jerry’s framework:
   - Employment population change
   - Unemployed population change
   - Labor force change
   - Not in labor force change
   - Participation rate and employment-population ratio
5. Classify the labor-market signal:
   - **Healthy supply expansion**: unemployment rate rises because labor force expands faster than jobs; employed population stable/up.
   - **Demand cooling**: employed population weakens and unemployed population rises; payrolls slow but not collapsing.
   - **Hidden weakness**: unemployment rate stable/falls because labor force participation drops or people leave labor force.
   - **Reacceleration / overheating**: payrolls broad-based strong, wages hot, hours stable/up, unemployment low.
   - **Recessionary deterioration**: payrolls weak/negative, employed persons down, unemployed persons up, U-6/part-time for economic reasons rising.
6. Check quality and breadth:
   - Private vs government payrolls
   - Cyclical vs defensive industries
   - Full-time/part-time if relevant
   - Part-time for economic reasons
   - U-6 underemployment
   - Revisions to prior months
7. Translate to macro and markets:
   - Fed / rate-cut pricing implication
   - Treasury yields and dollar
   - Equities / risk appetite
   - Crypto / gold if relevant
   - Sector tilt: cyclicals, defensives, small caps, financials, high duration tech

## Default output format

Use Chinese by default. Keep conclusion first.

1. **一句话结论**
2. **数据总览**: actual vs consensus, revisions, wages
3. **企业端 Establishment Survey**: payrolls, private/government, industries, hours/wages
4. **家庭端 Household Survey**: unemployment rate decomposition with employed, unemployed, labor force, not in labor force
5. **框架判断**: supply expansion / demand cooling / hidden weakness / overheating / recessionary deterioration
6. **市场影响**: Fed, 美债/美元, 美股, 加密/黄金, 行业
7. **接下来盯什么 / 反证条件**

## Important nuance

Do not treat the unemployment rate alone as the labor-market truth. Always explain whether the rate changed because of employment, unemployment, labor-force entry/exit, or participation changes.

When establishment and household surveys conflict, say so directly and avoid overclaiming. Label it as “企业端 vs 家庭端分歧” and explain which side markets are likely to trade first vs reassess later.

## Quick reusable sentence

“The key is not just whether the unemployment rate rose or fell, but whether that move came from job creation, unemployment, labor-force entry, or people leaving the labor market.”
