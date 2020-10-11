Asset prices keep changing over time and so does their statistics i.e. their mean and variance. The stock pricing data is actually time series data which means that we have data points recorded at regular intervals(trading days in this case). 

As learnt in the previous scenario, the [loading data scenario](https://www.katacoda.com/orm-harshit-tyagi/scenarios/first_steps_quant_trading_1), the stock pricing data is time series data and thus by nature of time series data, we observe trends and seaonality in the prices. 

We transform these fluctuating prices into stationary returns to be able to manipulate the prices with statistical modeling.

Following are the common types of returns:

1. **Simple Return**: it's the weighted sum of the returns of the individual assets in the portfolio. Simple returns are defined as:

<img src="/orm-harshit-tyagi/scenarios/first_steps_quant_trading_2/assets/simple_return.png" alt="Dataset">

![](/harshit-tyagi/first_steps_quant_trading_2/assets/simple_return.png)


2. **Log Return**: for a given month, it is the sum of the log returns of the days within that month. These are defined as:

<img src="/orm-harshit-tyagi/scenarios/quant_trading_1/assets/log_return.png" alt="Dataset">

![](/harshit-tyagi/quant_trading_1/assets/log_return.png)

In the next few steps we shall be using certain functions to obtain both these return vales using the data we already have. It is interesting how we can easily obtain each return value with a single line of code!