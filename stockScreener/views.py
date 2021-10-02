from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def getPC(soup, pc):
    # Get pros and cons of a company
    # input => string "pros", "cons"
    cons = soup.find("div",{"class", pc})
    cons = list(cons.children)[3]
    cons = cons.stripped_strings
    companyCons = []
    for item in cons:
        companyCons.append(item)
    return companyCons




#  ----- Pages --------------------------------

def index(request):
    return render(request, 'index.html')

def display(request):
    stockName = request.GET.get('inStock', 'default')
    # print(stockName)
    r = requests.get("https://www.screener.in/company/" + stockName + "/")
    soup = BeautifulSoup(r.content, 'html.parser')
    pros = getPC(soup, "pros")
    cons = getPC(soup, "cons")
    
    params = {"stockName":stockName, "pros":pros, "cons":cons}

    return render(request, 'display.html', params)



