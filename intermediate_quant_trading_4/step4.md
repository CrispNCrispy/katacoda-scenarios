It's time to plot the strategy.

Open the editor to continue the code: `step2.py`{{open}}

<pre class="file" data-filename="step2.py" data-target="append">
figure = cerebro.plot()[0][0]
figure.savefig('bollinger_band.png')
</pre>

Run the script to view the plot.

```
python step2.py

```{{execute}}

Click `bollinger_band.png`{{open}} to visualize the plot.

With that, you have successfully implemented a bollinger band strategy!