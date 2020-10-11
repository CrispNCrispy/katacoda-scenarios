For **Simple Return**, we shall be using the `pct_change()` method from pandas. All it does is take a series as input (the Adjusted Close values to be specific) and returns the series of simple return values. We then add this returned series as a column in our dataframe.

Side Note: A series is nothing but a data structure representing a single column. A dataframe (what we have used till now) is a combination of multiple columns (or multiple Series). For example, by printing df['Close'], it outputs a single column (Series) containing the closing prices from our dataframe. Series and Dataframes contain their own respective mehods and functions and are handled differently by Python though they are related in many ways.

For **Log Return**, we will be using numpy's `log()` function to compute the log values of the Adjusted Close value series. But in this case, since the `log()` function merely computes the log values and not the log return, we use the `shift()` method associated with a series in conjunction to divide the log value of the current row with the previous row. 

Side Note: A method and a function are very similar, with the only difference being that a method is associated with an instance of a class object - for example, the pct_change() method we used earlier was associated with the dataframe df, hence why the method followed 'df' as in 'df.pct_change()'. Ultimately, the both take in some arguments, do some computations and return a value. We may sometimes use it interchangeably.

Let's create a new file:
```
touch step2.py
```{{execute}}

Open `step2.py`{{open}}  in the editor.

Let's first append the commands to import the libraries we need and load the data. We will be using a .csv file containing the data instead of relying on an API like we had done so in scenario 1.

<pre class="file" data-filename="step2.py" data-target="append">

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =  pd.read_csv("https://raw.githubusercontent.com/dswh/python_fundamentals/master/images/apple_stock_eod_prices.csv",
                parse_dates=True, header=0, index_col=0)

</pre>

We will now append the commands to obtain the two return values. Pay close attention to how they're computed!

<pre class="file" data-filename="step2.py" data-target="append">

df['simple_return'] = df['Adj_Close'].pct_change()
df['log_return'] = np.log(df['Adj_Close']/df['Adj_Close'].shift(1))
print("Look for Simple and Log return columns")
print(df.head())

</pre>

These lines would essentially create two new columns in our dataframe, 'simple_return' and 'log_return'.

Now run the script. Notice the two new created columns at the very end of the dataframe. Also notice the NA values in the first row. This happens because the there is no row before the first row to compute a return from.

```
python step2.py

```{{execute}}