So far, we've seen how we create a buy or sell order using the buy() or sell() functions. But we have been using the default value of 1 stock per function call. 

The following is the signature of the buy() function:
`def buy(self, data=None,
        size=None, price=None, plimit=None,
        exectype=None, valid=None, tradeid=0, **kwargs):`

We could specify the size within the function call itself. But the default stake size, as you can see, is None. This is where Sizers come in. `size=None` requests that the Strategy asks its Sizer for the actual stake.

The background machinery adds a default sizer to a Strategy if the user has not added one. The default Sizer added to a strategy is SizerFix. The initial lines of the definition:
`class SizerFix(SizerBase):
    params = (('stake', 1),)`

While there are different ways to change this value and alter it for more complex stakes, we will focus on just one where we change this default sizer value.

Via the cerebro object, we will set a fixed size using the following command:
`cerebro.addsizer(bt.sizers.SizerFix, stake=20)`

Let's create a .py file to edit our previous strategy to implement a stake of 2.
```
touch step2.py
```{{execute}}

Open the newly created file by clicking: `step2.py`{{open}}

<pre class="file" data-filename="step2.py" data-target="append">

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

# Change the stake value
cerebro.addsizer(bt.sizers.SizerFix, stake=2)

# Run the strategy and watch the log
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

</pre>

Run the script to observe the change in final portfolio value and printed outputs.
Feel free to chage the stake value to see the difference.

```
python step2.py

```{{execute}}