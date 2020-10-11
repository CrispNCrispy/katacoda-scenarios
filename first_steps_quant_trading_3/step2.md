For this step, we shall be calculating and plotting simple moving average and cumulative moving average.

Let's exit the python shell and create a new file:
```
exit()
touch step2.py
```{{execute}}

Open `step2.py`{{open}}  in the editor.

In python, we can use the `rolling()` method to create a series of subsets based on the window size (i.e. number of days) and then cascade it with the `mean()` function to calculate the average over that window of data. With a similar logic, we use the `expanding()` method cascaded with the `mean()` function to calculate the cumulative moving average.

<pre class="file" data-filename="step2.py" data-target="append">
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

df =  pd.read_csv("https://raw.githubusercontent.com/dswh/python_fundamentals/master/images/apple_stock_eod_prices.csv",
                parse_dates=True, header=0, index_col=0)

# Isolate the adjusted closing prices into a series
adj_close_px = df['Adj_Close']

# Calculate the moving average - let's try it for a short period of # 40 days
moving_avg = adj_close_px.rolling(window=40).mean()

# Inspect the result
print(moving_avg)

</pre>

Based on the window size, we can calculate the short term and long term averages and plot them as well:

<pre class="file" data-filename="step2.py" data-target="append">
# Short moving window rolling mean
df['sma_40'] = adj_close_px.rolling(window=40).mean()

# Long moving window rolling mean - 252 days
df['sma_252'] = adj_close_px.rolling(window=252).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
fig = Figure()
plt = df[['Adj_Close', 'sma_40', 'sma_252']].plot(figsize=(12,8))
fig.savefig('moving_avg.png')
</pre>

Now, let's add the code to calculate the cumulative moving average and plot it alongside the adjusted closing price.

<pre class="file" data-filename="step2.py" data-target="append">
# Culumlative moving average
df['cma'] = adj_close_px.expanding().mean()

# Plot the adjusted closing price, the short and long windows of rolling means
fig = Figure()
plt = df[['Adj_Close', 'cma']].plot(figsize=(12,8))
fig.savefig('cumulative_moving_avg.png')
</pre>


Run the script to view the simple moving average values and the two created plots.

```
python step2.py

```{{execute}}

Click `moving_avg.png`{{open}} to visualize the plot of simple moving average for 40 days vs. simple moving average for 252 days vs. adjusted closing prices
Click `cumulative_moving_avg.png`{{open}} to visualize cumulative moving average vs. the adjusted closing price.