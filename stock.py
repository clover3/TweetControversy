import pandas_datareader.data as web
import datetime

def get_data(company_code):
    # We will look at stock prices over the past year, starting at January 1, 2016
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime(2018, 7, 1)

    # Let's get Apple stock data; Apple's ticker symbol is AAPL
    # First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
    data = web.DataReader(company_code, "yahoo", start, end)

    #data = quandl.get("EOD/{}".format(company_code), start_date="2018-04-01", end_date="2018-07-01", api_key="3pfStYJTLzDAaPx4P59b")
    return data

