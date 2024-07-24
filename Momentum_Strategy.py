import pandas as pd
from typing import List
import yfinance as yf

LOCAL_PATH = "C://Users//artur//OneDrive//analytics//resources//"
SP500_FILE = "S&P 500 Historical Components & Changes(12=30=2023).csv"
SP500_LAST_PRICES = "last sp500 prices"


def read_universe_data () -> pd. DataFrame :
    df = pd. read_csv (f"{ LOCAL_PATH } { SP500_FILE }", index_col ='date')
    return df

def fetch_universe_prices (tickers: List[str]) -> pd. DataFrame :
    print(tickers)
    prices = yf.download(tickers=tickers , start=None , end=None, 
                         ignore_tz =True )['AdjClose']
    return prices

def fetch_last_universe_prices (universe_data : pd. DataFrame
                                ) -> pd. DataFrame : 
        tickers = universe_data .iloc[-1, :].apply(lambda x: sorted(x.split(','))). to_list ()[0]
        prices = fetch_universe_prices (tickers=tickers)
        return prices
def save_prices_for_last_universe():
     universe_data = read_universe_data()
     prices = fetch_last_universe_prices(universe_data=universe_data)
     prices.index.name = 'date'
     prices.to_csv(f"{LOCAL_PATH}{SP500_LAST_PRICES}")

universe_data = read_universe_data()
print(universe_data)
