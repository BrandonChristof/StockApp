'''
    Helper file to get stock information for a given stock
    using the yfinance API.
'''

dataPoints = ["volume",
              "dividendRate",
              "trailingPE",
              "trailingEps",
              "dayLow",
              "dayHigh",
              "fiftyTwoWeekHigh",
              "fiftyTwoWeekLow",
              "open",
              "previousClose",
              "marketCap",
              "logo_url",
              "website",
              "longName",
              "longBusinessSummary"]

import yfinance as yf

def getCurrentPrice(stock):
    today = stock.history(period='1d')
    return round(today['Close'][0], 2)

def getStockData(ticker):
    stock = yf.Ticker(ticker)
    data = {}
    data["price"] = getCurrentPrice(stock)
    for d in dataPoints:
        try:
            data[d] = stock.info[d]
        except:
            data[d] = "N/A"
    return data
