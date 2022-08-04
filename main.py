import datetime
import time
from ArkFiles import ArkFiles
from currency import Currency
from stock import Stock
from price import Price
from financialStatements import FinancialStatements
from newsfeed import NewsFeed
from strategies import Strategy
import technicalPlot as TechnicalPlot
import backtestPlot as BacktestPlot


class Main:

    #******************** ARK files ********************#
    ark_files = ArkFiles()
    ark_files.download_csv_files()
    time.sleep(12)
    ark_files.move_files()
    ark_files.rename_files()


    #******************** stock list ********************#
    stock = Stock()
    yf_list = stock.convert_stock_list(col='ticker_yf', date='2022-07-18')
    av_list = stock.convert_stock_list(col='ticker_av', date='2022-07-18')
    stock_list = stock.convert_stock_list(col='ticker', date='2022-07-18')


    #******************** currency ********************#
    fx = Currency()
    fx.download_exchange_rate()
    print(fx.get_currency_list())


    #******************** technical analysis ********************#
    price = Price()
    price.download_adj_price(yf_list, from_date='2016-07-01')
    for i, ticker in enumerate(yf_list):
        print(i+1, ticker)
        price.calculate_ma(ticker=ticker, st=50, lt=200)
        price.calculate_macd(ticker=ticker, st=12, lt=26, signal=9)
        price.calculate_rsi(ticker=ticker, rsi=14, rsi_lt=42)
        price.calculate_roc(ticker=ticker, roc=9, roc_lt=50)
        price.calculate_rv(ticker=ticker, vol=63)
        price.calculate_atr(ticker=ticker, atr=14)
    

    #******************** technical plot ********************#
    strategy = Strategy()
    strategy.calculate_profit(yf_list)
    TechnicalPlot
    BacktestPlot



    #******************** fundamental analysis ********************#
    price.download_raw_price(av_list)
    price.preprocess_raw_price_files(av_list)
    fin_stmt = FinancialStatements(ticker_list=av_list)
    fin_stmt.download_fin_stmt()
    fin_stmt.preprocess_stmt_files()
    

    #******************** stock news ********************#
    newsfeed = NewsFeed(from_date='2022-07-13', from_index=None, to_index=99, stock_list=stock_list)
    newsfeed.scan_news()

    pass


if __name__ == "__main__":
    Main()