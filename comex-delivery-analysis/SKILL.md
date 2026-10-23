---
name: comex-delivery-analysis
description: Analyze CME/COMEX metals futures delivery reports (silver, gold, copper, platinum, palladium, aluminum). Extract and interpret delivery data showing which institutions are receiving (Issuer), which clients must deliver (Client Short), and which exchanges/market makers must deliver (House Short). Use when analyzing monthly delivery patterns, market structure, supply-demand signals, or institutional positioning in metals futures markets.
---

# COMEX Delivery Analysis

## Overview

Analyze CME/COMEX metals futures delivery reports to extract delivery obligations and generate market insights. This skill handles PDF reports containing year-to-date delivery data across multiple metals.

## Data Structure

### Column Definitions

COMEX delivery reports use a three-column structure per firm:

- **|I|** = Issuer (Long position) - Clients wanting to receive physical commodity
- **|C|S|** = Client Short - Clients who must deliver commodity  
- **|H|S|** = House Short - Exchange/market maker who must deliver commodity

### Delivery Flow

```
Long clients receive ← Client deliveries (|C|S|) + House deliveries (|H|S|)
```

Validation formula: |C|S| + |H|S| = |I|

## Analysis Workflow

### Step 1: Extract Data from PDF

1. Identify the product (e.g., "COMEX 5000 SILVER FUTURES")
2. Identify the analysis month from the column headers (DEC, JAN, FEB, etc.)
3. Extract three data columns for the target month:
   - |I| column (long positions wanting delivery)
   - |C|S| column (client delivery obligations)
   - |H|S| column (house delivery obligations)
4. Extract firm names and their corresponding values
5. Locate the TOTALS row at bottom of each product section

### Step 2: Calculate Summary Statistics

1. **Compute totals:**
   - Total long demand = Sum of all |I| values
   - Total client delivery = Sum of all |C|S| values
   - Total house delivery = Sum of all |H|S| values

2. **Validate balance:**
   - Verify: Client delivery + House delivery = Long demand
   - Flag any discrepancies

3. **Calculate percentages:**
   - Client delivery % = (Client delivery / Long demand) × 100
   - House delivery % = (House delivery / Long demand) × 100

### Step 3: Rank Top Participants

1. **Client Short Top 5:**
   - Rank firms by |C|S| values (descending)
   - Show: Firm name, delivery amount, % of total client delivery

2. **House Short Top 5:**
   - Rank firms by |H|S| values (descending)
   - Show: Firm name, delivery amount, % of total house delivery

Note: Same firm may appear in both rankings if they have both |C|S| and |H|S| positions.

### Step 4: Market Analysis

Analyze across four dimensions:

#### Dimension 1: Delivery Pressure Distribution

Analyze concentration and distribution patterns across both client and house delivery obligations:

**Client Delivery Concentration Analysis:**
- Calculate Herfindahl-Hirschman Index (HHI) for client shorts or use top-3/top-5 concentration ratios
- **Highly Concentrated (Top 3 > 75%)**: Few firms control delivery, potential coordination or forced liquidation
- **Moderately Concentrated (Top 3: 50-75%)**: Normal market structure with identifiable major players
- **Distributed (Top 3 < 50%)**: Competitive delivery market, broad participation

**House Delivery Concentration Analysis:**
- Assess whether exchange/dealers are centralizing or distributing delivery burden
- **Single Dominant House (>60% of house total)**: One dealer/exchange managing supply, inventory control concerns
- **Dual Leadership (Top 2: 60-80%)**: Shared responsibility between major market makers
- **Distributed Houses (Top 2 < 60%)**: Multiple dealers actively delivering, healthy liquidity

**Client vs. House Balance:**
- Calculate Client-to-House ratio: |C|S| / |H|S|
- **Ratio > 2.0**: Client-dominated delivery, ample physical supply in market
- **Ratio 0.5-2.0**: Balanced market, normal functioning
- **Ratio < 0.5**: House-dominated delivery, exchange releasing inventory, potential supply constraints

**Cross-Participant Patterns:**
- Identify firms appearing in both |C|S| and |H|S| (market makers managing both sides)
- Assess whether same firms dominate both client and house delivery (oligopolistic structure)
- Flag unusual patterns (e.g., major receiver also major deliverer)

**Delivery Pressure Conclusion:**
Synthesize findings to answer:
1. Which side (client or house) bears primary delivery responsibility?
2. Is delivery burden concentrated or distributed within each category?
3. What does this structure suggest about market health and supply availability?
4. Are there concentration risks or forced delivery scenarios?

#### Dimension 2: Market Participant Roles
- Identify major market makers and their behavior
- Identify primary delivery institutions
- Market structure characteristics

#### Dimension 3: Supply-Demand Signals

Interpret based on ratios:
- **High client delivery (>50%)**: Ample physical supply, competitive delivery market
- **High house delivery (>70%)**: Exchange releasing inventory, potential future supply pressure
- **High long demand**: Strong bullish sentiment or hedging activity
- **Month-over-month trends**: Directional changes in market structure

#### Dimension 4: Risks and Opportunities
- Inventory adequacy assessment
- Supply chain stress evaluation  
- Price support levels
- Delivery cost dynamics

## Output Format

Generate analysis as structured markdown with these sections:

### Basic Statistics
```
Product: [Product Name]
Report Date: [Date]
Analysis Month: [Month]

Total Long Demand: [number] contracts
Total Client Delivery: [number] contracts ([percentage]%)
Total House Delivery: [number] contracts ([percentage]%)

Validation: [client] + [house] = [total] ✓
```

### Top Participants
```
Client Delivery Obligations - Top 5:
1. [Firm Name] [number] contracts ([percentage]% of client delivery)
2. ...

House Delivery Obligations - Top 5:
1. [Firm Name] [number] contracts ([percentage]% of house delivery)
2. ...
```

### Market Analysis

Provide detailed analysis covering all four dimensions from Step 4.

### Month-over-Month Comparison (if multiple months available)

Compare current month to previous month(s), highlighting:
- Change in total delivery volume
- Shift in client vs. house balance
- New or departing major participants
- Trend implications

### Conclusions and Investment Implications

Synthesize findings into actionable market signals.

## Special Situations

### High Client Short Concentration
When a single firm has exceptionally high |C|S|:
- Firm faces significant delivery pressure
- May indicate bearish positioning or position unwinding

### High House Short Concentration  
When a single firm has exceptionally high |H|S|:
- Exchange/dealer has ample inventory
- May signal intentional inventory release for market stability

### Surge in Long Demand (|I|)
When long positions spike:
- Strong bullish sentiment
- Rising hedging activity
- May push up spot premiums

### House Delivery Dominance (>70%)
When house delivery exceeds 70% of total:
- Exchange carrying primary delivery burden
- Inventory drawdown occurring
- Potential future supply constraints

### Client Delivery Dominance (>50%)
When client delivery exceeds 50% of total:
- Active inter-client delivery market
- Physical supply not constrained
- Competitive market conditions

## Important Notes

- Always extract actual data from PDFs - NEVER fabricate numbers
- Each product section in the PDF is separate (Silver, Gold, Copper, etc.)
- Firms may appear multiple times with different position types (|C|S| and |H|S|)
- Month columns may be empty - only analyze months with data
- Pay attention to PREV column which shows previous month for comparison
- Different products may have different market dynamics
