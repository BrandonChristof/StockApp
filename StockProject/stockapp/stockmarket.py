'''
    Helper file to get stock information for a given stock
    using the yfinance API.
'''

dataPoints = ["volume",
              "marketCap",
              "logo_url",
              "longName"]

import yfinance as yf

def getCurrentPrice(stock):
    today = stock.history(period='1d')
    return today['Close'][0]

def getStockData(ticker):
    stock = yf.Ticker(ticker)
    data = {}
    data["price"] = getCurrentPrice(stock)
    for d in dataPoints:
        data[d] = stock.info[d]
    return data
