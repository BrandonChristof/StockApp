from django.shortcuts import render, redirect
from django.http import HttpResponse
from stockapp.stockmarket import getStockData

def index(request):
    data = {}
    if request.method == "POST":
        ticker = request.POST["stockTicker"]
        data = getStockData(ticker)
        print(data)
        return render(request, "stockapp/stockpage.html", {"data": data})
    
    return render(request, "base.html",  {"title": "Stocks"})


def getStock(request):
    if request.method == "POST":
        ticker = request.POST["stockTicker"]
        data = getStockData(ticker)
        print(data)
    return render(request, "stockapp/stockpage.html",  {"title": "Stocks"})
