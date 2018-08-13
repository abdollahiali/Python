import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader.data as web


start = dt.datetime(1990, 1, 1)
end = dt.date.today()

cmp_symbol1 = 'AAPL' # symbol of the company; 'AAPL' is the symbol of Apple
df1 = web.DataReader(cmp_symbol1, 'yahoo', start, end)

cmp_symbol2 = 'MSFT' # symbol of the company; 'MSFT' is the symbol of Microsoft
df2 = web.DataReader(cmp_symbol2, 'yahoo', start, end)

plt.figure()
plt.plot(df1['Adj Close'], 'b')
plt.hold
plt.plot(df2['Adj Close'], 'r')
plt.legend([cmp_symbol1, cmp_symbol2])
plt.show()



