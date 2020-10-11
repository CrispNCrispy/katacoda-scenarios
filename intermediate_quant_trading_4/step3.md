It's time to run the strategy.

Open the editor to continue the code: `step2.py`{{open}}

<pre class="file" data-filename="step2.py" data-target="append">

# Instantiate an object of the bt.Cerebro class
cerebro = bt.Cerebro(stdstats = False, cheat_on_open=True)

# Create the Data Feed - We will use Apple in 2019 this time.
data = bt.feeds.YahooFinanceData(dataname='AAPL', 
                                 fromdate=datetime(2019, 1, 1),
                                 todate=datetime(2019, 12, 31))

# Add the data feed to the cerebro object
cerebro.adddata(data)

# Add money to cerebro.broker
cerebro.broker.setcash(1000.0)

# Add the strategy to the cerebro object
cerebro.addstrategy(BBand_Strategy)

# Set the commission - 0.1% ... divide by 100 to remove the %
cerebro.broker.setcommission(commission=0.001)

# Run the strategy and watch the log
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue()) 
</pre>

Run the script to observe the output!

```
python step2.py

```{{execute}}

Finally, let's plot!