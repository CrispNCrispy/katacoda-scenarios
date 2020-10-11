Now that we covered few basic terminologies and computations, it's time to build the our moving average crossover strategy now! The most common applications of moving averages are to identify trend direction and to determine support and resistance levels. 

We shall be applying two strategies.
1. Price crossover, which is when the price crosses above or below a moving average to signal a potential change in trend. We will use an exponential weighted moving average for this. 
2. Another strategy is to apply two moving averages to a chart: one longer and one shorter. When the shorter-term MA crosses above the longer-term MA, it's a buy signal, as it indicates that the trend is shifting up. This is known as a "golden cross." Meanwhile, when the shorter-term MA crosses below the longer-term MA, it's a sell signal, as it indicates that the trend is shifting down. This is known as a "dead/death cross."

For the first step, we will import our libraries, read our data, compute simple moving average for two windows (short term of 50 and long term of 120) and compute exponential moving average with alpha of 0.1. We will create a separate dataframe to store these values. At the same time, for both the strategies, we will initialize a 'signals' column and a 'positions' column. We shall explain what these two columns are in subsequent steps. This should serve as a recap from the previous scenarios.

Setup a new python script:
```
touch step1.py
```{{execute}}

Open `step1.py`{{open}}  in the editor.

<pre class="file" data-filename="step4.py" data-target="append">
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =  pd.read_csv("https://raw.githubusercontent.com/dswh/python_fundamentals/master/images/apple_stock_eod_prices.csv",
                parse_dates=True, header=0, index_col=0)

# Initialize the short and long windows
short_window = 50
long_window = 120

# Initialize alpha
alpha = 0.1

# Create a new dataframe called signals with indices taken from our original dataframe.
signals = pd.DataFrame(index=df.index)

print(signals)

</pre>


Run the script to output an empty dataframe with the same index values (same dates) as in data we read via pf.read_csv()

```
python step1.py

```{{execute}}

Let's now create the columns in our new dataframe.