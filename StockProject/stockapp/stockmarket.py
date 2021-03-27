'''
    Helper file to get stock information for a given stock using the yfinance API.
'''

import yfinance as yf
import plotly.express as px
import plotly.offline

#Dictionary Headers called from the yfinance API
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

#Creates and returns a plotly graph of the max price history of a given stock
def getGraph(stock):
    hist = stock.history(period="max")
    hist = hist.reset_index()
    hist["Price"] = hist["Open"].astype('float64')
    title = stock.info["longName"].upper() + str(" Price History")
    fig = px.line(hist, x="Date", y="Price", title=title)
    graph = plotly.offline.plot(fig, auto_open = False, output_type="div")
    return graph

#Returns price change between previous close and current price
def getDollarChange(data):
    return round(float(data["price"]) - float(data["previousClose"]), 2)

#Returns percentage change between previous close and current price
def getPercentChange(data):
    return round((float(data["dollarChange"]) / float(data["previousClose"]))*100, 2)
    

#Returns a dictionary of information of each component in the dataPoints list
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
                data[d] = "{:,}".format(temp) #Adds commas for large numbers
            else:
                data[d] = "---"
        except:
            try:
                data[d] = stock.info[d]
            except:
                data[d] = "N/A"

    data["dollarChange"] = getDollarChange(data)
    data["percentChange"] = getPercentChange(data)
    return data

def getStockData(ticker):
    stock = yf.Ticker(ticker)
    dataDict = getDataDict(stock)
    
    if dataDict:
        graph = getGraph(stock)
    else:
        return None, None

    return dataDict, graph
    
