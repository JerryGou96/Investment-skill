
import json

def parse_bvp_data(text_content):
    companies = []
    lines = text_content.split('\n')
    # Skip header lines and irrelevant text
    data_lines = [line for line in lines if line and '$' in line and 'x' in line and '%' in line]

    for line in data_lines:
        # Split by multiple spaces to handle varying spacing
        parts = line.split()

        # Attempt to find the ticker which is usually the second part and all caps
        # And make sure it's not a number
        ticker_index = -1
        for i, part in enumerate(parts):
            if part.isupper() and len(part) >= 2 and not part.replace('.', '', 1).isdigit():
                ticker_index = i
                break

        if ticker_index == -1:
            continue # Skip if ticker not found

        company_name = parts[0]
        ticker = parts[ticker_index]

        # Extract numeric values starting from the element after the ticker
        numeric_values = []
        for part in parts[ticker_index + 1:]:
            try:
                # Remove non-numeric characters before conversion
                cleaned_part = part.replace('$', '').replace('x', '').replace('%', '').replace(',', '')
                numeric_values.append(float(cleaned_part))
            except ValueError:
                continue # Skip if not a valid number

        # Ensure we have enough numeric values for all metrics
        if len(numeric_values) < 8: # Stock Price, Market Cap, EV/R, NTM EV/R, Rev Growth, GM, OM, Rule of 40
            continue

        company_data = {
            "name": company_name,
            "ticker": ticker,
            "stock_price": numeric_values[0],
            "market_cap_mm": numeric_values[1],
            "ev_revenue_current": numeric_values[2],
            "ev_revenue_ntm": numeric_values[3],
            "revenue_growth_yoy": numeric_values[4],
            "gross_margin": numeric_values[5],
            "operating_margin": numeric_values[6],
            "rule_of_40": numeric_values[7]
        }
        companies.append(company_data)
    return companies

# The content fetched from web_fetch
bvp_text_content = """
Market cap in millions of dollars

Market Cap:

AdobeADBE$241.44$97,5903.8x3.5x52.3%12.0%89.6%40.3%
AgilysysAGYS$82.62$2,3216.7x5.7x32.2%11.7%64.4%20.5%
AlkamiALKT$17.59$1,8824.3x3.7x37.3%28.9%58.6%8.4%
AppFolioAPPF$159.18$5,6285.3x4.5x42.8%20.4%63.8%22.4%
AsanaASAN$6.66$1,5811.7x1.6x19.7%9.2%87.8%10.5%
AtlassianTEAM$93.29$23,6743.3x3.0x48.6%31.7%86.5%16.9%
AvePointAVPT$10.27$2,1773.7x3.1x48.5%26.0%72.8%22.5%
Bill.comBILL$34.85$3,4712.0x1.7x37.0%13.5%84.6%23.6%
BlackLineBL$27.11$1,5902.4x2.2x32.2%9.7%76.0%22.5%
BrazeBRZE$23.36$2,6312.8x2.4x38.0%30.2%65.7%7.8%
C3.aiAI$10.22$1,4854.3x4.1x-105.7%-46.1%17.3%-59.6%
CellebriteCLBT$13.20$3,2935.4x4.5x50.2%19.3%82.5%30.9%
CloudflareNET$228.11$80,62931.3x24.4x45.6%33.5%71.2%12.1%
CrowdstrikeCRWD$671.00$170,79431.9x26.0x48.4%23.3%76.1%25.1%
DatadogDDOG$225.24$80,17619.1x15.8x58.5%32.1%79.2%26.4%
DigitalOceanDOCN$151.91$15,85416.1x11.6x39.2%22.4%56.1%16.8%
DocuSignDOCU$49.58$9,6332.7x2.5x39.4%7.8%79.8%31.6%
DynatraceDT$40.51$11,8085.1x4.4x44.4%19.4%81.1%24.9%
ElasticESTC$57.61$5,9632.9x2.6x32.0%17.7%76.4%14.3%
FastlyFSLY$16.94$2,6513.9x3.6x28.3%19.8%62.5%8.5%
FigmaFIG$23.46$12,3968.1x6.7x64.1%46.1%79.4%17.9%
Five9FIVN$22.83$1,7481.5x1.4x26.9%9.2%55.9%17.7%
FreshworksFRSH$9.00$2,4881.9x1.7x42.6%16.5%84.8%26.1%
GitlabGTLB$27.93$4,7163.3x2.9x44.5%23.2%86.6%21.3%
HubSpotHUBS$198.80$10,1822.5x2.2x44.4%23.4%83.5%21.1%
IntappINTA$20.60$1,5872.5x2.2x36.5%13.2%75.8%23.3%
JFrogFROG$72.77$8,81413.1x11.4x50.4%25.8%78.2%24.6%
KlaviyoKVYO$14.74$4,4112.5x2.1x43.3%27.9%75.1%15.3%
Monday.comMNDY$77.49$3,9342.1x1.8x46.3%24.4%89.2%21.9%
MongoDBMDB$325.68$26,1758.6x7.5x44.7%26.8%73.0%18.0%
nCinoNCNO$15.85$1,7363.1x2.8x28.0%10.6%63.3%17.4%
NutanixNTNX$48.81$13,1474.5x4.0x37.4%10.0%86.9%27.4%
OktaOKTA$94.72$16,6094.8x4.4x40.3%11.6%77.9%28.8%
PagerDutyPD$7.44$5701.0x1.0x25.2%2.8%85.9%22.4%
PalantirPLTR$143.34$343,63151.4x34.9x125.9%84.7%86.8%41.2%
Palo Alto NetworksPANW$257.77$209,05119.8x15.5x49.3%14.9%73.6%34.4%
PaycomPAYC$136.80$6,3793.1x2.8x27.3%7.8%89.0%19.5%
PaylocityPCTY$110.88$5,9372.9x2.7x34.7%10.5%72.3%24.2%
ProcorePCOR$47.54$7,1734.6x4.1x33.0%15.7%80.4%17.3%
Q2QTWO$45.14$2,8263.2x2.9x37.4%14.1%59.1%23.3%
QualysQLYS$100.37$3,5354.1x3.8x51.2%9.8%83.3%41.4%
RingcentralRNG$41.86$3,5101.8x1.7x28.6%5.3%72.2%23.3%
RubrikRBRK$70.32$14,4739.2x7.9x63.1%46.3%81.5%16.8%
SailPointSAIL$16.55$9,3887.7x6.5x26.8%22.7%67.1%4.1%
SalesforceCRM$176.17$144,2833.9x3.6x46.2%13.3%76.9%32.9%
SamsaraIOT$31.57$18,3969.7x8.1x40.0%28.3%76.4%11.7%
SentinelOneS$18.02$6,1325.1x4.3x27.2%20.2%72.6%7.0%
ServiceNowNOW$108.73$112,1347.1x5.9x52.8%22.1%75.1%30.7%
ServiceTitanTTAN$65.79$6,2675.8x5.0x31.7%21.4%70.3%10.3%
ShopifySHOP$115.03$149,65311.3x9.3x51.0%34.3%48.8%16.7%
SnowflakeSNOW$239.20$82,59614.6x11.6x54.5%33.5%66.6%21.0%
SprinklrCXM$5.36$1,3341.0x1.0x26.8%8.9%65.7%17.9%
SPS CommerceSPSC$53.52$1,9652.4x2.2x27.5%5.8%69.2%21.7%
TenableTENB$25.95$2,8622.8x2.6x34.3%9.6%78.4%24.7%
ToastTOST$24.96$14,4692.0x1.6x31.9%21.9%27.5%10.0%
TwilioTWLO$184.60$28,0174.8x4.3x37.0%20.0%48.7%17.0%
UiPathPATH$11.58$6,0672.3x2.1x31.9%13.6%84.7%18.3%
Veeva SystemsVEEV$164.38$26,8276.1x5.4x57.4%16.0%74.5%41.5%
WeaveWEAV$5.76$4581.7x1.5x21.0%17.4%72.6%3.7%
WixWIX$52.65$2,2030.8x0.7x37.7%14.3%65.3%23.4%
WorkdayWDAY$130.01$32,1093.1x2.8x42.7%13.5%76.2%29.2%
WorkivaWK$46.57$2,6132.6x2.2x37.3%19.9%80.4%17.4%
ZetaZETA$20.18$5,0303.1x2.7x62.5%49.9%59.0%12.6%
ZscalerZS$130.04$21,0295.7x4.9x53.8%25.4%77.4%28.3%
"""

parsed_data = parse_bvp_data(bvp_text_content)

# Save to a JSON file
file_path = "skills/saas-valuation-analyzer/references/bvp_cloud_index_data.json"
with open(file_path, "w") as f:
    json.dump(parsed_data, f, indent=2)

print(f"Data saved to {file_path}")

# Also print the parsed data for review
print("\n--- Parsed Data Sample ---")
print(json.dumps(parsed_data[:5], indent=2))
