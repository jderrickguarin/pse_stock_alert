import smtplib
import time
import datetime
import tickerparser
import file_reader

DATE = '04-02-2020'
#DATE = tickerparser.get_date('prevd')
STOCKS = file_reader.get_tickers()
STOCKS_URL = [tickerparser.get_URL(stock, DATE) for stock in STOCKS]
TICKER_TO_URL = dict(zip(STOCKS, STOCKS_URL))

def check_price():
    for ticker, stockdata in TICKER_TO_URL.items():
        data = tickerparser.get_data(stockdata)
        print(data, type(data))
    
        try:
            lastClosingPrice = data['close']
            yield ticker, float(lastClosingPrice)
        except:
            yield ticker, 'No data found'

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('psestockalert@gmail.com', 'ksadagmffdgoibbn')

    stocks_to_send = {}
    subject = 'Daily PSE Stocks Watchlist'
    body = ''
    picks = check_price()
    for pick in picks:

        if pick == 'No data found':
            print(f'\nNo data from {pick[0]}')
        else:
            price = str(pick[1])
            stocks_to_send[pick[0]] = price

            body += f'Closing price for ${pick[0]} on {DATE}: Php {price}\n'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'psestockalert@gmail.com',
        'derrickguarin@gmail.com',
        msg
        )

    print(stocks_to_send)
    print('\nEmail sent!') 
    
    #server.quit()

send_mail()


#print(DATE)
#print(STOCKS)
#print(TICKER_TO_URL)
