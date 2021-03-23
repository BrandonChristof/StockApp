'''
    Helper file to get stock information for a given stock using the yfinance API.
'''

import yfinance as yf
import plotly.express as px
import plotly.offline

dataPoints = ["volume",
              "averageVolume",
              "twoHundredDayAverage",
              "pegRatio",
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

def getCurrentPrice(stock):
    today = stock.history(period='1d')
    return round(today['Close'][0], 2)

#Creates and returns a plotly graph of a given stocks max price history
def getGraph(stock):
    hist = stock.history(period="max")
    hist = hist.reset_index()
    hist["Price"] = hist["Open"].astype('float64')
    title = stock.info["longName"].upper() + str(" Price History")
    fig = px.line(hist, x="Date", y="Price", title=title)
    graph = plotly.offline.plot(fig, auto_open = False, output_type="div")
    return graph

#Returns a dictionary of information of each component in dataPoints
def getDataDict(stock):
    data = {}
    try:
        data["price"] = getCurrentPrice(stock)
    except:
        return None
    for d in dataPoints:
        try:
            if stock.info[d]:
                temp = round(stock.info[d], 2)
                data[d] = "{:,}".format(temp)
            else:
                data[d] = "---"
        except:
            data[d] = stock.info[d]
    return data

def getStockData(ticker):
    stock = yf.Ticker(ticker)
    dataDict = getDataDict(stock)
    
    if dataDict:
        graph = getGraph(stock)
    else:
        return None, None

    return dataDict, graph
    
