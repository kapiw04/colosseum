import pandas as pd
from prophet import Prophet


df = pd.read_csv('data/dane_close.csv', sep=';')
stocks = df.columns[2:]
stocks_mapping = {name: i for i, name in enumerate(stocks)}

for stock in stocks:
  m = Prophet()
  data = pd.read_csv(f'data/stocks/{stock}.csv', sep=';')
  m.fit(data)
  future = m.make_future_dataframe(periods=101)

  forecast = m.predict(future)

  forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(
    f'data/forecasts/{stock}_forecast.csv', index=False, sep=';')
