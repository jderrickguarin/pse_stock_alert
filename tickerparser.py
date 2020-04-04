import time
import requests

PSEAPI_URL = 'http://pseapi.com/api/Stock/'

def getData(URL):
    # Strictly get from PSE API
    return requests.get(URL)

def getURL(ticker, date):
    return PSEAPI_URL + ticker + '/' +  date

def getLastClosingPrice(ticker, date):
    return PSEAPI_URL + ticker

def getYoYPrice(ticker):
    return

def getYTDPrice(ticker):
    return

print(getURL('JFC','03-15-2017'))

