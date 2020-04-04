import requests
import json
from bs4 import BeautifulSoup
import smtplib
from time import time, ctime
import datetime
import tickerparser

STOCK = 'AXLM'
DATE = '04-03-2020'
STOCK_DATE_PRICE = tickerparser.getURL(STOCK, DATE)

def check_price():
    page = requests.get(STOCK_DATE_PRICE)    
    data = page.json()

    print(data, type(data))
    
    lastClosingPrice = data['close']
    
    print(float(lastClosingPrice))
    return float(lastClosingPrice)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('psestockalert@gmail.com', 'ksadagmffdgoibbn')

    price = str(check_price())
    subject = ('$' + STOCK)
    body = 'Closing price for '+ DATE + ': Php ' + price 

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'psestockalert@gmail.com',
        'derrickguarin@gmail.com',
        msg
        )

    print(price)
    print('\nEmail sent!') 

#check_price()
send_mail()

#closePrice = requests.get(STOCK_DATE_PRICE)
#y2dPrice = requests.get()