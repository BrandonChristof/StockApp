from django.shortcuts import render, redirect
from django.http import HttpResponse
from stockapp.stockmarket import getStockData

def index(request):
    if request.method == "POST":
        ticker = request.POST["stockTicker"]
        data, graph_div = getStockData(ticker)
        if data:
            return render(request, "stockapp/stockpage.html", {"data": data, "graph_div": graph_div})
    return render(request, "base.html",  {"title": "Stocks"})

