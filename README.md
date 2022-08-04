# Stock-Selection-Model

*Investment firms strive to find the holy grail to capture alpha in the markets. In this project, we will create simple strategies using technical analysis on the public stock markets, and we will backtest the efficacy of these methods.*

## 1. Data

We will use the stocks in ARK Invest's portfolios to perform technical analysis as a starting point. But any stocks can be added to or removed from the watchlist.

## 2. Data Wrangling

There are multiple tasks in this step, including
- creating a ticker glossary in either hashtable or dataframe type, which will be used as a reference to download data from different sources for differernt purposes, e.g., stock price, financial statements, news;
- finding different currencies used in the stock price, and downloading exchange rates to convert price into the same currencies for portfolio management purposes - we use USD in this case;
- finding the percentage allocation invested in the portfolios;
- creating a stock list for the following analysis.

## 3. Data Preprocessing

Having downloaded the stock price, we calculate different indicators, including but not limited to moving averages, MACD, relative strength index, rate of change, relative volume, average true range, etc.

## 4. Data Visualization

The chart below shows where the individual stock stands with respect to different indicators. More indicators can be added, and the input of the indicators can be adjusted if needed, making the investment thesis totally customizable.

![technical_analysis_tsla_2yr](https://github.com/hoytlui/Stock-Selection-Model/blob/main/Images/technical_analysis_TSLA_2y.png)

## 5. Backtesting

Our backtesting tactic divides the stock performance into 10 tiers:
- Gain: 0-5%, 5-10%, 10-20%, 20-50%, >50%
- Loss: 0-5%, 5-10%, 10-20%, 20-50%, 50-100%

![backtesting](https://github.com/hoytlui/Stock-Selection-Model/blob/main/Images/backtest.png)


## 6. Takeaways

The profit and loss chart in the backtesting step shows how each strategy work in different time period. The visualization makes it clear that the strategy used in this test does not perform too well from Mar 2021 onward due to bear market, which tells us that the strategy can be further modified.

## 7. Further Work

- Parameters/Input can be adjusted in the functions, which will be easier for profit optimization.
- Fundamental analysis can be combined to enhance decision making, e.g., how financially healthy is the companies, which leads to decide how much capital to allocate for that particular stock.
- Machine learning on stock news can be added to analyze market sentiment and predict stock price movement.
