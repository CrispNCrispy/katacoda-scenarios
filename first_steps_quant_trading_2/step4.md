Finally, let's plot the cummulative returns that helps us visualise the investment returns of the apple stock over the years. To do so, we will be using matplotlib, a library dedicated for visualizations. The `plot()` method (which uses matplotlib behind the scenes) associated with a dataframe can be used directly and quickly to produce the require line graph.

We will continue to use previous python script, step2.py.

Open `step2.py`{{open}}  in the editor.

<pre class="file" data-filename="step2.py" data-target="append">
fig = plt.figure()
plt = df["cum_daily_return"].plot(figsize=(12,8))
fig.savefig('cummulative_return.png')
</pre>

Run the script that saves the final plot.

```
python step2.py

```{{execute}}

Click `cummulative_return.png`{{open}} to visualize cummulative returns.

As an exercise, try to make inferences on the plot. Look at where there were very high returns and where there were steep dips and attribute reasons for the same.