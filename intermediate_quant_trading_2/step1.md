Now that we have seen how to go about using the backtrader API in a simple fashion, it's time to create a strategy that involves buying and selling of stocks. For our first step, we will focus on buying stocks. We will incorporate a simple strategy - Buy whenever the close prices drops for 3 bars in a row.

Let's create a .py file.
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

        if self.dataclose[0] < self.dataclose[-1]:
            # current close less than previous close

            if self.dataclose[-1] < self.dataclose[-2]:
                # previous close less than the previous close

                # BUY, BUY, BUY!!! (with all possible default parameters)
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.buy()



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
* Close prices of every day in 2019
* Buy orders
* Change in our portfolio value
```
python step1.py

```{{execute}}

Several “BUY” creation orders were issued, our porftolio value has increased in one year.

Several important things to note:
* The stake is provided behind the scenes by a position sizer which uses a fixed stake, being the default “1”.
* self.datas[0] (the main data aka system clock) is the target asset if no other one is specified.
* The order is executed “At Market”. The broker executes this using the opening price of the next bar, because that’s the 1st tick after the current under examination bar. But we still do not know what price it was executed at - or if it was executed at all (creation of order and execution is different. For all we know, our order might have been rejected). We will work on printing this notification in step 3.

In the next step, we will add a sell strategy.