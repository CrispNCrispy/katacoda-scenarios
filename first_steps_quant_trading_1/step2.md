With the environment all set now, let's load the end-of-day stock pricing data. For this entire series, we'll be working with the Apple stock prices from 2011-2020.

Let's create a file where the code will reside:

```
touch step2.py
```{{execute}}

To start off, open the newly created file by clicking: `step2.py`{{open}}

Now, import the required libraries:

<pre class="file" data-filename="step2.py" data-target="append">

import pandas as pd
import yfinance as yf

</pre>

To download the data from Yahoo Finance, you need to pass the stock symbol(AAPL in our case), starting date, ending date, and progress to set the progress bar visibility:

<pre class="file" data-filename="step2.py" data-target="append">

df_apple = yf.download('AAPL', 
                       start='2011-01-01', 
                       end='2020-09-30',
                       progress=False)

</pre>

This will give us the data in a pandas dataframe which we can inspect using:


<pre class="file" data-filename="step2.py" data-target="append">

print(df_apple.head())

</pre>

```
python step2.py

```{{execute}}

We have the Apple EOD stock pricing data in a DataFrame containing daily Open, High, Low, and Close (OHLC) prices, as well as the adjusted close price and volume.

Let's now look at another possible method of downloading the historical stock pricing data.