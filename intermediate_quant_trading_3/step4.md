With our strategy now complete, all that is left is to plot it to view a more in depth understanding of when the stock was bought and sold as well as the variations in price and SMA.

Open the same .py file we used in the last step.
Open `step3.py`{{open}}.

<pre class="file" data-filename="step2.py" data-target="append">
fig = plt.figure()
plt = cerebro.plot(iplot=True, volume=False)

# the cerebro plot returns a 2D list, so
fig.savefig('backtest_plot.png')
</pre>

Run the script to view the plot.

```
python step3.py

```{{execute}}

Click `backtest_plot.png`{{open}} to visualize the plot.

With that, you have successfully implemented a more robust strategy. In the next scenario we will use whatever we learnt for an even more complicated strategy.
