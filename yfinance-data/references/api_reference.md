# yfinance quick reference

## Current quote
```python
import yfinance as yf

t = yf.Ticker("AAPL")
print(t.fast_info)
print(t.info.get("currentPrice"))
```

## Historical prices
```python
import yfinance as yf

df = yf.download(["AAPL","MSFT"], period="1mo", interval="1d", auto_adjust=True)
print(df.tail())
```

## Financial statements
```python
import yfinance as yf

t = yf.Ticker("MSFT")
print(t.income_stmt)
print(t.balance_sheet)
print(t.cashflow)
```

## Earnings and analyst data
```python
import yfinance as yf

t = yf.Ticker("NVDA")
print(t.earnings_history)
print(t.analyst_price_targets)
print(t.recommendations)
```

## Options chain
```python
import yfinance as yf

t = yf.Ticker("AAPL")
print(t.options)
if t.options:
    chain = t.option_chain(t.options[0])
    print(chain.calls.head())
    print(chain.puts.head())
```
