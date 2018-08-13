import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader.data as web


start = dt.datetime(2018, 8, 1)
end = dt.datetime(2018, 8, 12)

cmp_symbol = 'AAPL' # symbol of the company; 'AAPL' is the symbol of Apple
df = web.DataReader(cmp_symbol, 'yahoo', start, end)

print("\nPrinting the first 2 items of the dataframe:")
print(df.head(2))

print("\nPrinting the first 3 items of the dataframe:")
print(df.tail(3)) 

print("\nPrinting the whole dataframe:")
print(df)


