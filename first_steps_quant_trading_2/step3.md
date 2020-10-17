We will now calculate the simple daily cumulative returns using the simple return values. To do so, we will be using the `cumprod()` method. We first add 1 (100%) to the simple returns before using the `cumprod()` method as in the following formula:

<img src="/orm-harshit-tyagi/scenarios/first_steps_quant_trading_2/assets/cumulative_return.png" alt="Dataset">

We will continue to use previous python script, step2.py.

Open `step2.py`{{open}}  in the editor.

<pre class="file" data-filename="step2.py" data-target="append">

df["cum_daily_return"] = (1 + df['simple_return']).cumprod()
print("Look for Cummulative daily return columns")
print(df.head())
print(df.tail())

</pre>

the `tail()` method is similar to the `head()` method, but outputs the last 5 rows instead of the first 5. Run the script and notice the cumulative values in  the first 5 rows vs. the last 5 rows.

```
python step2.py

```{{execute}}