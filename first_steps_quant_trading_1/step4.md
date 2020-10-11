We have the data loaded into dataframes but we don't know much about what it contains and what each column represents.

We saw we have the following columns in the previous step:
Date - specifies trading date
Open - opening price
High - maximum price during the day
Low - minimum price during the day
Close - close price adjusted for splits
Volume - number of shares traded on a particular day.
Split - Number of shares after split / Number of shares before
Dividend -  Number of shares after dividend / Number of shares before.
AdjOpen - adjusted opening price for that day
AdjHigh - adjusted maximum price for that day
AdjLow - adjusted lowest price for that day
AdjClose - adjusted close price adjusted for both dividends and splits.
AdjVolume - adjusted volume of shares traded

Make sure you have the same `step3.py`{{open}} opened for this step as well.

To get a slightly deeper understanding of the prices and volumes, we should have a good understanding of the summary statistics of each column:

<pre class="file" data-filename="step3.py" data-target="append">

print(df_apple.describe())

</pre>

Next, we should explore the movement of prices of the apple stock over the years. 

Let's plot the adjusted closing prices on the chart:

<pre class="file" data-filename="step3.py" data-target="append">
import matplotlib.pyplot as plt

fig = plt.figure()
plt = df_apple['AdjClose'].plot()
fig.savefig('close_plot.png')
</pre>

To look at the output of the snippets that we've added, we'll have to run the script:
```
python step3.py

```{{execute}}

Looking at the summary statistics and movement of prices give us a high-level picture of how the apple stock has been performing for the past ~10 years. 