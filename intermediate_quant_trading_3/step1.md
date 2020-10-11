In the previous scenario, you may have noticed that we harcoded the value of 5 in the strategy class to sell a stock after 5 bars have passed. But this is not fully practical as we would want a way to change this easily. This is where parameters come in.

Parameters can be assigned within the class strategy by assigning a tuple of all the parameters to a variable called params. For example, `params = (('myparam', 27), ('exitbars', 5))`

Alternatively, we could pass these values when adding the strategy to Cerebro. For example, `cerebro.addstrategy(TestStrategy, myparam=20, exitbars=7)`

Let's create a .py file to edit our previous strategy to implement parameters.
```
exit()
touch step1.py
```{{execute}}

Open the newly created file by clicking: `step1.py`{{open}}

<pre class="file" data-filename="step1.py" data-target="append">

import backtrader as bt # Import the backtrader platform
from datetime import datetime  # For datetime objects

# Create a Stratey
class TestStrategy(bt.Strategy):

    params = (
        ('exitbars', 5),
    )

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.dataclose[0] < self.dataclose[-1]:
                    # current close less than previous close

                    if self.dataclose[-1] < self.dataclose[-2]:
                        # previous close less than the previous close

                        # BUY, BUY, BUY!!! (with default parameters)
                        self.log('BUY CREATE, %.2f' % self.dataclose[0])

                        # Keep track of the created order to avoid a 2nd order
                        self.order = self.buy()

        else:

            # Already in the market ... we might sell
            if len(self) >= (self.bar_executed + self.params.exitbars):
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()

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
cerebro.addstrategy(TestStrategy)

# Set the commission - 0.1% ... divide by 100 to remove the %
cerebro.broker.setcommission(commission=0.001)

# Run the strategy and watch the log
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

</pre>

Run the script to observe the output. Feel free to chage the value to see the difference.

```
python step1.py

```{{execute}}