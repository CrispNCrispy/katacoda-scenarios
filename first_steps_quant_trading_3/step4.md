The final step is to determine the volatility of the stock which would tell us how risky it is to invest in this stock.

We use standard deviation `std()` function for calculating volatility alongside the `rolling()` method.

We will continue using the previous .py file.
Open `step2.py`{{open}}  in the editor.

<pre class="file" data-filename="step2.py" data-target="append">
# Define the minumum of periods to consider 
min_periods = 75 

# Calculate the volatility
vol = adj_close_px.rolling(min_periods).std() * np.sqrt(min_periods) 

# Plot the volatility
fig = Figure()
plt = vol.plot(figsize=(10, 8))

# Show the plot
fig.savefig('vol.png')
</pre>

Run the script to view the plot.

```
python step2.py

```{{execute}}

Click `vol.png`{{open}} to visualize the plot of volitility for the stock.