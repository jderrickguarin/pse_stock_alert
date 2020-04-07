import requests
import datetime
import json

PSEAPI_URL = 'http://pseapi.com/api/Stock/'

def get_date(param):
    rawdate = datetime.datetime.now()
    m = rawdate.strftime("%m")
    d = rawdate.strftime("%d")
    y = rawdate.strftime("%Y")
    currentDate = f"{m}-{d}-{y}"
    ytdDate = f"01-01-{y}"
    yoyDate = f"{m}-{d}-{int(y)-1}"
    previousDay = f"{m}-{int(d)-1}-{y}"

    # Accepted parameters: curr, fstday, lstyr, prevd, all
    try:
        if param == 'curr':
            return currentDate
        elif param == 'fstday':
            return ytdDate
        elif param == 'lstyr':
            return yoyDate
        elif param == 'prevd':
            return previousDay
        elif param == 'all':
            return {'curr':currentDate, 'fstday':ytdDate, 'lstyr':yoyDate, 'prevd':previousDay}
    except:
        print("You entered the wrong parameter. Accepted parameters: curr, fstday, lstyr, prevd, all")
        return None

def get_data(URL):
    # Strictly get from PSE API
    try:
        with requests.get(URL) as response:
            try:
                response.raise_for_status()
                page = requests.get(URL)
            except requests.exceptions.HTTPError:
                print('No data found. Either no trading or wrong ticker.')
                page = None
    except requests.exceptions.ConnectionError:
        print('Check your connection')
        page = None

    if page != None:
        data = page.json()
    else:
        data = None

    print(data, type(data))
    return data

def get_URL(ticker, date):
    try:
        return f"{PSEAPI_URL}{ticker}/{date}"
    except TypeError:
        return "Check getDate argument"

def get_prev_day_price(ticker, date):
    return PSEAPI_URL + ticker

def get_yoy_price(ticker):
    return

def get_ytd_price(ticker):
    return


