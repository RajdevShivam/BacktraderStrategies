import backtrader as bt
import strategies
import yfinance as yf

ticker = "TSLA"
startTime = '2018-01-01'
endTime = '2021-06-30'
initialCash = 1000000

cerebro = bt.Cerebro()

# Add/Change the strategy
cerebro.addstrategy(strategies.RSI)

# You may want to change the default cash for different strategy
cerebro.broker.setcash(initialCash)

data = bt.feeds.PandasData(dataname=yf.download(ticker, startTime, endTime))

# Add the Data Feed to Cerebro
cerebro.adddata(data)
thestrats = cerebro.run()
thestrat = thestrats[0]

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()

