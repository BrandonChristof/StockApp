from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "stockapp/stockpage.html",  {"title": "Stocks"})
