---
name: financial-report-analyzer
description: 专门用于上市公司财报（如年度报告、季度报告）的深度分析。能够提取关键财务指标，计算核心财务比率，结合行业背景生成专业的财务分析报告。
---

# 财报分析技能 (Financial Report Analyzer)

## Overview

This skill provides comprehensive guidance on analyzing financial reports (annual and quarterly reports) of listed companies. It extracts key financial indicators, calculates core financial ratios, and generates professional financial analysis reports combined with industry context.

## Available Tools

Use these tools available in OpenClaw:
- `exec` / `python`: Execute scripts and calculations
- `web_fetch`: Fetch financial data from web sources
- `pdf`: Analyze PDF financial reports
- `browser`: Navigate financial websites

## Instructions

### 1. Data Collection

When analyzing a company's financial report, first gather:
- Revenue and Net Profit
- Total Assets and Liabilities
- Cash Flow data
- Key financial ratios

Data sources:
- Company investor relations website (annual/quarterly reports in PDF)
- Yahoo Finance, MarketWatch, StockAnalysis
- SEC EDGAR (for US listed companies)

### 2. Key Financial Ratios to Calculate

**Profitability Ratios:**
- Gross Margin = (Revenue - COGS) / Revenue
- Net Profit Margin = Net Profit / Revenue
- ROE = Net Profit / Shareholders' Equity
- ROA = Net Profit / Total Assets
- ROIC = EBIT / (Total Debt + Equity - Cash)

**Liquidity Ratios:**
- Current Ratio = Current Assets / Current Liabilities
- Quick Ratio = (Current Assets - Inventory) / Current Liabilities

**Leverage Ratios:**
- Debt-to-Equity = Total Debt / Shareholders' Equity
- Debt-to-Assets = Total Debt / Total Assets

**Efficiency Ratios:**
- Asset Turnover = Revenue / Total Assets
- Inventory Turnover = COGS / Average Inventory
- Receivables Turnover = Revenue / Average Accounts Receivable

**Valuation Ratios:**
- P/E Ratio = Market Cap / Net Profit
- P/S Ratio = Market Cap / Revenue
- P/B Ratio = Market Cap / Book Value
- EV/EBITDA = Enterprise Value / EBITDA

### 3. Analysis Framework

Analyze from four dimensions:

1. **Profitability Analysis (盈利能力分析)**
   - Gross margin trend (improving or declining?)
   - Net profit margin vs industry average
   - ROE and ROA trends
   - Non-recurring gains/losses impact

2. **Solvency & Risk Analysis (偿债与风险分析)**
   - Debt level and debt-to-equity ratio
   - Interest coverage ratio
   - Current ratio and quick ratio
   - Cash burn rate

3. **Efficiency Analysis (营运效率分析)**
   - Asset turnover improvement
   - Working capital management
   - Inventory and receivables turnover
   - Operating cash flow conversion

4. **Cash Flow & Quality Analysis (现金流与利润质量分析)**
   - Operating cash flow vs net profit
   - Free cash flow
   - Cash flow sustainability
   - Capex requirements

### 4. Output Format

When analyzing a financial report, provide:

```json
{
  "eval_note": <float -1 to 1>,
  "confidence": <float 0-1>,
  "recommendation": "Buy" | "Hold" | "Sell",
  "key_metrics": {
    "revenue": "XXB",
    "net_profit": "XXB", 
    "gross_margin": "XX%",
    "net_margin": "XX%",
    "roe": "XX%",
    "debt_to_equity": "XX%",
    "current_ratio": "XX"
  },
  "strengths": ["strength1", "strength2"],
  "risks": ["risk1", "risk2"],
  "description": "Detailed analysis explaining the reasoning"
}
```

## Analysis Process

### Step 1: Gather Basic Information
- Company name, ticker, exchange
- Reporting period (Q1/Q2/Q3/Q4 Annual)
- Revenue, Net Profit, EPS
- Total Assets, Total Liabilities, Equity
- Cash and Cash Equivalents

### Step 2: Calculate Key Ratios
Use the formulas in Section 2 to calculate:
- Profitability ratios
- Liquidity ratios  
- Leverage ratios
- Efficiency ratios
- Valuation ratios

### Step 3: Trend Analysis
- Compare with same period last year (YoY)
- Compare with industry peers
- Identify trend direction (improving/stable/declining)

### Step 4: Risk Assessment
- Identify key risks from financial statements
- Assess debt levels and liquidity
- Evaluate non-recurring items impact

### Step 5: Write Analysis Report
Structure the analysis as:
1. Executive Summary
2. Revenue & Profitability
3. Balance Sheet & Liquidity
4. Cash Flow Analysis
5. Key Risks
6. Investment Conclusion

## Common Red Flags

Watch for these warning signs:
- Rapid revenue growth but declining cash flow
- Increasing debt faster than assets
- Sudden drop in gross margin
- Large non-recurring gains inflating profits
- Accounts receivable growing faster than revenue
- Inventory buildup
- Related party transactions
- Auditor changes or qualifications

## Best Practices

1. Always read the "Management Discussion & Analysis" (MD&A) section
2. Pay attention to accounting policy changes
3. Understand the business model before analyzing numbers
4. Compare with industry peers for context
5. Look at multi-year trends, not just single year
6. Adjust for non-recurring items to assess true profitability
7. Consider macroeconomic environment and industry trends

## Usage Example

When Jerry asks to analyze a company's financial report:

1. "分析 NVDA 2024年财报"
2. Fetch the financial data from web sources
3. Calculate key ratios using Python/exec
4. Structure the analysis using this framework
5. Present findings in the JSON format above