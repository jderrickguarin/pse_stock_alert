import requests
import json
#from bs4 import BeautifulSoup
import smtplib
import time
import datetime
import tickerparser

STOCK = 'AXLM'
DATE = tickerparser.getDate('prevd')
#DATE = '04-02-2020'
STOCK_DATE_PRICE = tickerparser.getURL(STOCK, DATE)

def check_price():
    data = tickerparser.getData(STOCK_DATE_PRICE)

    print(data, type(data))
    
    try:
        lastClosingPrice = data['close']
        return float(lastClosingPrice)
    except:
        return 'No data found'

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('psestockalert@gmail.com', 'ksadagmffdgoibbn')

    if check_price() == 'No data found':
        print('\nNo mail sent')
    else:
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
    
    #server.quit()

send_mail()
#print(DATE)
