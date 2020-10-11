In the previous step, all we had was some cash but no asset to spend it on. Through a Data Feed, we intend to change that. We will also add a cash amount to the broker explicitly.

Create a .py file for the same.

```
touch step3.py
```{{execute}}

Open the newly created file by clicking: `step3.py`{{open}}

<pre class="file" data-filename="step3.py" data-target="append">

import backtrader as bt
from datetime import datetime

'''
Define the strategy class here

This strategy class inherits the base bt. Strategy class

It then adds to some of the methods of the bt. Strategy class including the __init__() method
for the strategy logic as well as finer controls such as specific types of details to print

'''

# Instantiate an object of the bt.Cerebro class
cerebro = bt.Cerebro()

# Create the Data Feed
data = bt.feeds.YahooFinanceData(dataname='MSFT',fromdate=datetime(2018, 1, 1),todate=datetime(2018, 12, 31))

# Add the data feed to the cerebro object
cerebro.adddata(data)

# Add money to cerebro.broker
cerebro.broker.setcash(1000.0)

'''
Add the strategy to the cerebro object

Add comission charges if needed
'''

# Run the strategy and watch the log
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

print("\n")
print(data)

</pre>

Run the script to output:
* The new initial and final portfolio value.
* The Data Feed object

```
python step3.py

```{{execute}}

backtrader comes with a set of Data Feed parsers (all CSV Based currently) to let you load data from different sources.
* Yahoo (online or already saved to a file)
* VisualChart (see www.visualchart.com)
* Backtrader CSV (own cooked format for testing)
* Generic CSV support

In our above example, we used a Microsoft Data Feed from Yahoo online. We cannot see the values, but the Data Feeds object is meant to work well with the backtrader framework, containing several lines such as Open and Close.

Because we do not have a strategy defined, there is nothing to compute or see. In the next step, we shall add a simple test stratey class.