import pandas as pd
import yfinance as yf
yf.pdr_override()


def get_daily_data(pair, start_date, end_date):
    # Set the ticker as 'EURUSD=X'
    df = yf.download(f'{pair}=X', start=start_date, end=end_date)
    
    # Set the index to a datetime object
    # df.index = pd.to_datetime(df.index)
    
    return df


def get_small_frequencies(pair, period, interval):
    # pass the interval (1m, 1h, etc.) and period (1d, 2d, 10d)
    df = yf.download(f'{pair}=X', period= period, interval=interval)
    
    # Set the index to a datetime object
    # df.index = pd.to_datetime(df.index)
    
    return df
    