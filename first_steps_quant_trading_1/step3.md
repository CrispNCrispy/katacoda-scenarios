Another way we can download the same data is using the `pandas-datareader` library that we installed.

In fact, pandas-datareader provides functions to extract data from various Internet sources in a pandas dataframe. Currently, the following sources are supported by them:

* Tiingo
* IEX
* Alpha Vantage
* Enigma
* Quandl
* St.Louis FED (FRED)
* Kenneth French’s data library
* World Bank
* OECD
* Eurostat
* Thrift Savings Plan
* Nasdaq Trader symbol definitions
* Stooq
* MOEX
* Naver Finance

For this example, let's try to extract data from Quandl. 

Let's create another file:
```
touch step3.py
```{{execute}}

Make sure you have `step3.py`{{open}} opened in the editor.

Similar to what we did in the previous step, here's how we'll download data here:

<pre class="file" data-filename="step3.py" data-target="append">

import pandas_datareader.data as pdr

df_apple = pdr.DataReader('AAPL',
                       'quandl',
                       '2011-01-01', 
                       '2020-09-30',
                       api_key='yuqp72Y_-GpAsrjQEXfL')

</pre>

This will give us the data in a pandas dataframe which we can inspect using:

<pre class="file" data-filename="step3.py" data-target="append">
# First five rows
print(df_apple.head())

# Information about the dataframe
print(df_apple.info())

</pre>

We have the same Apple stock prices for the same time period with same columns(features).


```
python step3.py

```{{execute}}

Note: Incase if an error arises with `pdr.DataReader` due to the `api_key` argument, please create an account on quandl to obtain your own personal API key.
