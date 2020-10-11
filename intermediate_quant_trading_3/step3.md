The strategy we have been using until now isn't something you would put into practice. Rather than buying when the price falls 3 bars in a row, we may consider using a Simple Moving Average Indicator to buy a stock when the price crosses over the SMA value.

We will now use a strategy based on SMA (Short Moving Average) where:

* When the close price goes above the 20-day SMA, buy one share.
* When the close price falls below the 20-day SMA and we have a share, sell it.
* We can only have a maximum of one share at any given time.

Let's create a .py file to implement this.
```
touch step3.py
```{{execute}}

Open the newly created file by clicking: `step3.py`{{open}}

<pre class="file" data-filename="step3.py" data-target="append">

from datetime import datetime
import backtrader as bt
import matplotlib.pyplot as plt

class SmaStrategy(bt.Strategy):
    
    #SMA Period, can be changed to whatever value we want
    params = (('ma_period', 20), )

    def __init__(self):
        '''
        constructor to keep track of objects 
        like close price, order, commission, etc
        ''' 
        self.data_close = self.datas[0].close

        self.order = None
        self.price = None
        self.comm = None

        # SMA Indicator!!
        self.sma = bt.ind.SMA(self.datas[0],
                              period=self.params.ma_period)

    def log(self, txt):
        '''
        to log the executable instructions
        '''
        dt = self.datas[0].datetime.date(0).isoformat()
        print(f'{dt}, {txt}')

    def notify_order(self, order):
        '''
        reporting the status of order, important for cases like:
        - the order might not be carried out
        - we might have insufficience cash
        - removes pending order
        '''
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED --- Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Commission: {order.executed.comm:.2f}')
                self.price = order.executed.price
                self.comm = order.executed.comm
            else:
                self.log(f'SELL EXECUTED --- Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Commission: {order.executed.comm:.2f}')

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin,
                              order.Rejected]:
            self.log('Order Failed')

        self.order = None

    def notify_trade(self, trade):
        # to notify the trade results
        if not trade.isclosed:
            return

        self.log(f'OPERATION RESULT --- Gross: {trade.pnl:.2f}, Net: {trade.pnlcomm:.2f}')

    def next(self):
        '''
        contains trading strategy logic
        checks if any order is pending, checks
        if we have a position already, checks if the closing price is greater than than the moving average and places an order.
        '''
        if self.order:
            return

        if not self.position:
            if self.data_close[0] > self.sma[0]:
                self.log(f'BUY CREATED --- Price: {self.data_close[0]:.2f}')
                self.order = self.buy()
        else:
            if self.data_close[0] < self.sma[0]: 
                self.log(f'SELL CREATED --- Price: {self.data_close[0]:.2f}')
                self.order = self.sell()
                
##downloading apple stock price data for the year 2019
data = bt.feeds.YahooFinanceData(dataname='AAPL', 
                                 fromdate=datetime(2019, 1, 1),
                                 todate=datetime(2019, 12, 31))

# Instantiate an object of the bt.Cerebro class
cerebro = bt.Cerebro()

# Create the Data Feed - We will use Apple in 2019 this time.
data = bt.feeds.YahooFinanceData(dataname='AAPL', 
                                 fromdate=datetime(2019, 1, 1),
                                 todate=datetime(2019, 12, 31))

# Add the data feed to the cerebro object
cerebro.adddata(data)

# Add money to cerebro.broker
cerebro.broker.setcash(1000.0)

# Add the strategy to the cerebro object
cerebro.addstrategy(SmaStrategy)

# Set the commission - 0.1% ... divide by 100 to remove the %
cerebro.broker.setcommission(commission=0.001)

# Run the strategy and watch the log
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue()) 

</pre>

Run the script to observe the output!

```
python step3.py

```{{execute}}

We have now completed a more intricate strategy. Well done! Finally, let's move on to the last step where we'll plot our result.