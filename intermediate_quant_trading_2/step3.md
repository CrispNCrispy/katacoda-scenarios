With a buy and sell strategy in place, let us alter the TestStrategy class to include a notification that would tell us if a buy/sell order was executed and if so, at what price.

To do this, we introduce a new variable and a new function.
* self.order - This variable is initially assigned as None, but is assigned the buy or sell functions depending on if we are buying or selling which in turn is structurerd in such a way that it's status changes to either Completed, Accepted, Cancelled, Margin or Rejected. We will be using it as part of if conditions. If an order is pending, we cannot place a buy/sell order.
* notify_order() function - This function will log the execution if it has happened and reassigns the self.order to None once the execution is confirmed/accepted.

Also, the self.bar_executed is moved into notify_order().

Create a .py file.

```
touch step3.py
```{{execute}}

Open the newly created file by clicking: `step3.py`{{open}}

<pre class="file" data-filename="step2.py" data-target="append">
import backtrader as bt # Import the backtrader platform
from datetime import datetime  # For datetime objects

# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders
        self.order = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

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
            if len(self) >= (self.bar_executed + 5):
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

'''
Add comission charges if needed
'''

# Run the strategy and watch the log
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
</pre>

Read the code, read the comments and execute the code to observe:
* Close prices of every day in 2019.
* Buy orders and executions when the price drops 3 days in a row.
* Sell orders and executions 5 bars after a stock has been bought.
* Change in our portfolio value.

Note: Buying and selling of only 1 stock is happening as of right now.

```
python step3.py

```{{execute}}

One thing you may have been asking youself is what about the commission comment in the code? When are we going to add commission? We will cover that in the next step.