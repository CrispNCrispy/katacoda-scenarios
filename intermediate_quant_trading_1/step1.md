The entirety of this and the next 3 scenarios will cover how one can implement backtesting of any trading strategy using Python. We will extensively be using the **Backtrader** python library to systematically build up our understanding of how strategies can be created to finally build two strategies - A Simple Moving Average strategy and a Bollinger Band strategy. You can of course further build upon this to backtest your own custom strategies! Having at least an intermediate knowledge of Python is required to fully understand what is happening under the hood.

Note: Remember to read the comments alongside the code!


Here is what we will cover in this and the following scenarios:

* Scenario 5 (Intermidate Quant Trading 1): Building blocks of working with backtrader
* Scenario 6 (Intermidate Quant Trading 2): Implementaiton of a simple buy and sell strategy
* Scenario 7 (Intermidate Quant Trading 3): Implementation of a Simple Moving Average strategy
* Scenario 8 (Intermidate Quant Trading 4): Implementation of a Bollinger Band strategy.


**Backtesting** is the process of applying a trading strategy or analytical method to historical data to see how accurately the strategy or method would have predicted actual results.

For example, let's assume you devise a model that you think consistently predicts the future value of the NIFTY 50. By using historical data, you can backtest the model to see whether it would have worked in the past. By comparing the predicted results of the model against the actual historical results, backtesting can determine whether the model has predictive value.


There are two key concepts crucial to Backtrader. 

1. **Lines**: Data Feeds, Indicators and Strategies have lines (You will see what these are subsequently - especially in Data Feeds). A line is a succession of points that when joined together form this line. When talking about the markets, a Data Feed has usually the following set of points per day: Open, High, Low, Close, Volume, OpenInterest. The series of “Open”s along time is a Line. And therefore a Data Feed has usually 6 lines. If we also consider “DateTime” (which is the actual reference for a single point), we could count 7 lines.

2. **Index 0 Approach**: When accessing the values in a line, the current value is accessed with index: 0. And the “last” output value is accessed with -1. This in line with Python conventions for iterables (and a line can be iterated and is therefore an iterable) where index -1 is used to access the “last” item of the iterable/array. In our case is the last output value what’s getting accessed. As such and being index 0 right after -1, it is used to access the current moment in line.

The first step is to install and import all the required libraries and frameworks.

So, let's setup our environment first.

Install backtrader and create a new file where the our code would reside:
```
exit()
pip install backtrader
```{{execute}}

The backtrader framework has a few key features that include:
* A good number of available technical indicators and performance measures.
* Ease of building and applying new indicators.
* Multiple data sources available (including Yahoo Finance, Quandl).
* Simulating many aspects of real brokers, such as different types of orders, slippage, commission, going long/short, etc.
* A one-line call for a plot, with all results.

Now that we have a small understanding of Backtrader and backtesting, it's time to move on to the next step where we'll begin coding!