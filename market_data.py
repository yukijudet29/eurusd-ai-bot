import requests
import pandas as pd
from config import API_KEY


def get_market_data():

    url = f"https://api.twelvedata.com/time_series?symbol=EUR/USD&interval=15min&apikey={API_KEY}&outputsize=200"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data['values'])

    df = df.iloc[::-1]

    df['close'] = df['close'].astype(float)

    return df