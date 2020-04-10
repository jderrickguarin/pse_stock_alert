import pandas as pd
import requests
import datetime as dt
import json 

STOCK_URL = 'http://pseapi.com/api/Stock/'
MARKET_URL = 'http://pseapi.com/api/Market/'
SECTOR_URL = 'http://pseapi.com/api/Sector/'

# Transforms a date object to a string-typed date
def stringify(rawdate):
    m = rawdate.strftime("%m")
    d = rawdate.strftime("%d")
    y = rawdate.strftime("%Y")
    return f"{m}-{d}-{y}" 

# Transforms a string-typed date to date object
def objectify(strdate):
    lstdate = strdate.split('-')
    return dt.date(int(lstdate[2]),int(0),int(1))

# Returns URL from PSE API given the stock ticker and date
def get_stock_URL(ticker, date):
    try:
        return f"{STOCK_URL}{ticker}/{date}"
    except TypeError:
        print("Check ticker or date argument")
        return None

# Returns the JSON formatted date from supplied PSE API URL
def get_data(URL):
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

# Expects a date string of form "mm-dd-yyyy" and can return a tuple of date objects or strings
def get_dates(start, end = dt.date.today(), dateObject = False):
    if end == None:
        end = dt.date.today()

    if dateObject == True:
        if isinstance(start, str):
            fstart = objectify(start)
        else:
            fstart = start
        if end != dt.date.today():
            fend = objectify(end)
        else:
            fend = end
        return fstart, fend
    elif dateObject == False:
        if isinstance(start, str):
            fstart = start
        else:
            fstart = stringify(start)
        if end != dt.date.today():
            fend = end
        else:
            fend = stringify(end)

        return fstart, fend

# Returns a list of valid trading dates from start to end. Returns either DateTimeIndex or list of strings
def get_datelist(start, end=None, DateTimeIndex = False):
    date_extr = get_dates(start, end)
    nstart = date_extr[0]
    nend = date_extr[1]
    b_dates = pd.bdate_range(start = nstart, end = nend)
    if DateTimeIndex == True:
        return b_dates
    else:
        datelist = []
        for date in b_dates:
            datified = date.to_pydatetime()
            strdate = stringify(datified)
            datelist.append(strdate)
        return datelist

def generate_df(ticker, start, end=None):
    datelist = get_datelist(start, end)
    histprices_list = []
    for date in datelist:
        URL = get_stock_URL(ticker, date)
        data = get_data(URL)
        # histprices_df = histprices_df.append()
        if data != None:
            histprices_list.append(data)

    histprices_df = pd.DataFrame(histprices_list)
    return histprices_df

def generate_csv(ticker, start, end=None, fileName = 'data.csv'):
    
    # Do not just convert dataframe to csv, instead manually loop through all data and input as comma separated values
    pass

print(generate_df('JFC', '2-4-2020'))

# PSE API doesn't work properly now. Rewrite code to accomodate new api at http://phisix-api4.appspot.com/index.html
# Might try to create a Python module that scrapes data from PSE EDGE and returns data in csv or dataframe given a start and end date