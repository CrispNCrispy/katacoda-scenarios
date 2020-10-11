Before we dive deep into quantitative trading, we should have the required data that we want to work with. In this scenario, we'll focus on the entire process of collecting high-quality data from different sources and load them into pandas dataframes.

Some of the important sources of data you can explore:
* Yahoo Finance
* Quandl
* Intrinio

We are only going to cover Yahoo finance and pandas-datareader in this scenario. You can check out the documentation of the other two. It's pretty simple and straight forward. 

So, let's set up our environment first.

Let's first exit the python shell to execute installation command in the terminal:
```
exit()
```{{execute}}

The next step is to install the required libraries that will facilitate data from yahoo finance and FRED (Federal Reserve Economic Data).

```
pip install yfinance pandas-datareader
```{{execute}}

And our environment is all set up and we are ready to start gathering data now.
