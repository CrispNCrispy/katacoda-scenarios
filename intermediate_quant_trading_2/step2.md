With a buy strategy in place, let us alter the TestStrategy class to include a sell strategy. For our sell strategy, we will sell a stock 5 days after buying it, irrespective of the closing prices to keep it simple.

To include the sell strategy, we will need to include two new object variables:
* self.position - This is a variable of a unique position data type that exists as part of the framework itself. It records the number of shares of a particular asset as well as other details. We will be using this in an if condition. If we have not bought a stock, it will result in a buy order. If we already have one stock, it will check if 5 bars have been executed before creating a sell order.
* self.bar_executed - We define this variable to track how many bars have passed since we last executed our buy order to sell our stock after 5 bars have passed.

Create a .py file.

```
touch step2.py
```{{execute}}

Open the newly created file by clicking: `step2.py`{{open}}

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

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

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
                        self.bar_executed = len(self)
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
* Buy orders when the price drops 3 days in a row.
* Sell orders 5 bars after a stock has been bought.
* Change in our portfolio value.

Note: Buying and selling of only 1 stock is happening as of right now.

```
python step2.py

```{{execute}}

Our portfolio has increased by $25 in one year just by buying and selling one single stock using this strategy.

We still have not talked about whether the orders were actually executed and if it had been executed, at what price. We will now delve into this in the next step.