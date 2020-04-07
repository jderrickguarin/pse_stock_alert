import csv

# Get tickers of stocks monitored from text file
def get_tickers(filepath = 'picks/stock_picks.txt'):
    tickers = []
    with open(filepath, 'r') as stockPicks:
        for line in stockPicks:
            tickers.append(line.rstrip('\n'))
    return tickers

# Log daily alerts to a csv file
def to_log(ticker, price, pdate, logdate, logtime, alertType = None, filepath = 'log/userlog.csv'):
    with open(filepath, mode='r') as logFile:
        log_writer = csv.writer(logFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        
        log_writer.writerow([ticker, price, pdate, logdate, logtime, alertType])
