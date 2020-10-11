It's time to plot the strategy.

Open the editor to continue the code: `step2.py`{{open}}

<pre class="file" data-filename="step2.py" data-target="append">
fig = plt.figure()
plt = cerebro.plot(iplot=True, volume=False)

# the cerebro plot returns a 2D list, so
fig.savefig('bollinger_band.png')
</pre>

Run the script to view the plot.

```
python step2.py

```{{execute}}

Click `bollinger_band.png`{{open}} to visualize the plot.

With that, you have successfully implemented a bollinger band strategy and have completed all the katacodas on Quantitative Trading using Python! Congratulations!

There's always more to learn and develop on top of all this. All the best!