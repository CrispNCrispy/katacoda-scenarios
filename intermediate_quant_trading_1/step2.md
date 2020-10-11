Let's begin with the code! For this step, we shall just observe a few building blocks. Do not forget to read the comments in the code.

Create a .py file for the same.

```
touch step2.py
```{{execute}}

Open the newly created file by clicking: `step2.py`{{open}}

<pre class="file" data-filename="step2.py" data-target="append">
import backtrader as bt

'''
Define the strategy class here

This strategy class inherits the base bt. Strategy class

It then adds to some of the methods of the bt. Strategy class including the __init__ method
for the strategy logic as well as finer controls such as specific types of details to print

'''
</pre>

The first major thing we do in backtesting is to decide on our strategy. All of the strategy based code goes in the strategy class.

<pre class="file" data-filename="step2.py" data-target="append">
#Instantiate an object of the bt.Cerebro class
cerebro = bt.Cerebro()

'''
Create the Data Feed

Add the Data Feed to the cerebro object 

Add money to cerebro.broker

Add the strategy to the cerebro object

Add comission charges if needed
'''

# Run the strategy and watch the log
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
</pre>

Notice the steps that are written in the form of comments. As we progress through the tutorial, we will start coding in these steps to show the effect of each of them. Once we have our strategy in place (which we will introduce in step 4), it's a matter of setting a few parameters and running the strategy by initializing and running the cerebro object.

Run the script to output the initial and final portfolio value.

```
python step2.py

```{{execute}}

Since all we did is instantiate the cerebro object and run it. Since we did not yet add a strategy to the object, the object currently does nothing when run. This isn't much but it's important to understand how and what we are trying to achieve in a step by step manner. In the background, the Cerebro engine created a broker with a default amount of 10000.

Next, we shall build upon this to add a Data Feed and Set our cash amount explicitly.