'''
    Helper file to get stock information for a given stock
    using the yfinance API.
'''

import yfinance as yf

def getCurrentPrice(stock):
    today = stock.history(period='1d')
    return today['Close'][0]

def getVolume(stock):
    return stock.info["volume"]

def getMarketCap(stock):
    return stock.info["marketCap"]

def getLogo(stock):
    return stock.info["logo_url"]

def getName(stock):
    return stock.info["longName"]

def getStockData(ticker):
    stock = yf.Ticker(ticker)
    data = {}
    data["price"] = getCurrentPrice(stock)
    data["volume"] = getVolume(stock)
    data["marketcap"] = getMarketCap(stock)
    data["logolink"] = getLogo(stock)
    data["name"] = getName(stock)
    return data

