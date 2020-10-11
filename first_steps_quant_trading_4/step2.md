We will now be adding the following columns to the new dataframe for the first strategy:

1. `ema_signal` - We will initialize this to zeros. In step 3, we shall alter it in such a way that whenever the exponential moving average crosses the price, the signal values will be 1 instead of 0.
2. `ema` - Compute the exponential moving average for an alpha value of 0.1.
3. `ema_positions` - We will initialize this to zeros. In step 3, after altering the 'ema_signal' column, we will subtract the 'ema_signal' value of the previous row from the current row. This will result in a value of +1 everytime the exponential moving average crosses above the price, -1 everytime the exponential moving average crosses below the price and 0 everywhere else. We will then use the +1's and -1's in out plot to understand buy and sell signals.

Open `step1.py`{{open}}  in the editor.

<pre class="file" data-filename="step4.py" data-target="append">
# Initialize to 0s
signals['ema_signal'] = 0.0

# Create exponential moving average values for an alpha value
signals['ema'] =  df['Close'].ewm(alpha=alpha, adjust=False).mean()

# Initialize to 0s
signals['ema_positions'] = 0.0
</pre>

We will now be adding the following columns to the new dataframe for the second strategy:

1. `sma_signal` - We will initialize this to zeros. In step 4, we shall alter it in such a way that whenever the short moving average crosses the long moving average, the signal values will be 1 instead of 0.
2. `short_mavg` - Compute the moving average values for a window of 50 days.
3. `long_mavg` - Compute the moving average values for a window of 120 days.
4. `sma_positions` - We will initialize this to zeros. In step 4, after altering the 'sma_signal' column, we will subtract the 'sma_signal' value of the previous row from the current row. This will result in a value of +1 everytime the short moving average crosses above the long moving average, -1 everytime the short moving average crosses below the long moving average and 0 everywhere else. We will then use the +1's and -1's in out plot to understand buy and sell signals.

<pre class="file" data-filename="step4.py" data-target="append">
# Initialize to 0s
signals['sma_signal'] = 0.0



# Create short simple moving average over the short window. We use the following arguments for the 'rolling' method

# min_periods = 1 - Minimum number of observations in window required to have a value (otherwise result is NA).  

# center = False, so that the labels are not set at the center of the window (default value is actually False, 
# so even if we did not use this argument, that would be alright).   
signals['short_mavg'] =  df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()



# Create long simple moving average over the long window. We use the following arguments for the 'rolling' method

# min_periods = 1 - Minimum number of observations in window required to have a value (otherwise result is NA).  

# center = False, so that the labels are not set at the center of the window (default value is actually False, 
# so even if we did not use this argument, that would be alright).  
signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()



# Initialize to 0s
signals['sma_positions'] = 0.0

print(signals)
</pre>


Run the script to output the dataframe filled with the 7 new columns.

```
python step1.py

```{{execute}}