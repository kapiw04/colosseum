import pandas as pd
from engineer_data import Indicators

close = pd.read_csv('data/dane_close.csv', sep=';')
open = pd.read_csv('data/dane_open.csv', sep=';')
high = pd.read_csv('data/dane_high.csv', sep=';')
low = pd.read_csv('data/dane_low.csv', sep=';')
vol = pd.read_csv('data/dane_vol.csv', sep=';')

indicators = Indicators()

for stock in close.columns[2:]:
  data = pd.DataFrame(close[stock])

  data["data"] = pd.to_datetime(close["data"], format='%Y%m%d')
  data["czas"] = pd.to_datetime(close["czas"], format='%H%M%S').dt.time

  data["ds"] = data["data"].astype(str) + " " + data["czas"].astype(str)
  print(data["data"].astype(str) + " " + data["czas"].astype(str))
  path = f'data/stocks/{stock}.csv'

  data.drop(columns=["data", "czas"], inplace=True)
  # change column name
  data.columns = ['y', 'ds']
  # data = indicators.engineerData(path)

  data.to_csv(path, index=False, sep=';')
