Let us now add a simple TestStrategy class! Using this, we are just going to output the Close prices of a particular stock.

Create a .py file for the same.

```
touch step4.py
```{{execute}}

Open the newly created file by clicking: `step4.py`{{open}}

<pre class="file" data-filename="step4.py" data-target="append">

import backtrader as bt
from datetime import datetime

#Define the TestStrategy Class
class TestStrategy(bt.Strategy):
    
    # This logging function is called whenever we need to output something, for example, close 
    # prices in our strategy
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    # This method is called once when the cerebro object is initialized.
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries. We can obtain other
        # lines using this dataseries if needed
        self.dataclose = self.datas[0].close

    # This function is called on each bar of self.datas[0]. This is where the majority of our
    # strategy based logic would reside.
    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])


# Instantiate an object of the bt.Cerebro class
cerebro = bt.Cerebro()

# Create the Data Feed
data = bt.feeds.YahooFinanceData(dataname='MSFT',fromdate=datetime(2018, 1, 1),todate=datetime(2018, 12, 31))

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

Run the script to output:
* The initial and final portfolio value.
* The Close prices for Microsoft in 2018

```
python step4.py

```{{execute}}

You now have a basic understanding of how one can use the backtrader framework. In the next Scenario, we will build a simple buy and sell strategy, while at the same time build upon what we have learnt in this scenario.