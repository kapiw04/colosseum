import pandas as pd
from prophet import Prophet
from typing import List


df = pd.read_csv('data/dane_close.csv', sep=';')
stocks = df.columns[2:5]
stocks_mapping = {name: i for i, name in enumerate(stocks)}


def get_predictions(stocks: List[pd.DataFrame]) -> List[pd.DataFrame]:
  predicions = []
  for stock in stocks:
    m = Prophet()
    m.fit(stock)
    future = m.make_future_dataframe(periods=93 * 7)

    forecast = m.predict(future)

    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    predicions.append(forecast)
