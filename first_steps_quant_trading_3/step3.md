For this step, we shall be calculating and plotting the exponentially weighted moving average for two different values of alpha, 0.1 and 0.5.

We will continue using the previous .py file.
Open `step2.py`{{open}}  in the editor.

We use the `ewm()` method cascaded with the `mean()` function similar to how we did so in step 2. Here, we provide a value of alpha as an argument - the same alpha from the formula shown in step 1. Reminder:

<img src="/orm-harshit-tyagi/scenarios/first_steps_quant_trading_3/assets/ewma.png" alt="Dataset">

![](/harshit-tyagi/first_steps_quant_trading_3/assets/ewma.png)

Let's add the code to compute and plot it.

<pre class="file" data-filename="step2.py" data-target="append">
# Short moving window rolling mean
df['ewma_alpha_0.1'] = adj_close_px.ewm(alpha=0.1, adjust=False).mean()

# Long moving window rolling mean - 252 days
df['ewma_alpha_0.5'] = adj_close_px.ewm(alpha=0.5, adjust=False).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
# Plotting from January 2018 for clearer visualization
fig = plt.figure()
plt = df.loc['2018-01-01':,['Adj_Close', 'ewma_alpha_0.1', 'ewma_alpha_0.5']].plot(figsize=(12,8))
fig.savefig('exp_moving_avg.png')
</pre>


Run the script to view the plot.

```
python step2.py

```{{execute}}

Click `exp_moving_avg.png`{{open}} to visualize the plot of exponential moving avg for an alpha of 0.1 vs. 0.5 plotted alongside the adjusted closing prices.