from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, "stockapp/stockpage.html",  {"title": "Stocks"})

def getStock(request):
    if request.method == "POST":
        ticker = request.POST["stockTicker"]
    return redirect("/")
