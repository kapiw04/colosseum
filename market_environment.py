import pandas as pd
import random
from typing import List
from dataclasses import dataclass

SIMULATION_LENGTH = 101

df = pd.read_csv('data/dane_close.csv', sep=';')
names = df.columns[2:]
stocks_mapping = {name: i for i, name in enumerate(names)}


class Markets:
  def __init__(self, stocks: List[pd.DataFrame]):
    self.stocks: List[pd.DataFrame] = stocks  # list of stocks' dataframes
    self.index: int = 0  # current "time"
    self.length: int = len(stocks[0])  # length of the data

  def reset(self) -> None:
    self.index = 0

  def step(self) -> None:
    self.index += 1
    if self.index >= self.length:
      self.index = 0

  def get_current_state(self) -> List[pd.DataFrame]:
    return [stock.iloc[self.index] for stock in self.stocks]

  def get_current_state_of_stock(self, stock_name: str) -> pd.DataFrame:
    return self.stocks[stocks_mapping[stock_name]].iloc[self.index]

  def random_time(self) -> None:
    self.index = random.randint(0, self.length - SIMULATION_LENGTH)


@dataclass
class Stock:
  data: pd.DataFrame
  index: int
  length: int


def load_data() -> List[pd.DataFrame]:
  close = pd.read_csv('data/dane_close.csv', sep=';')
  open = pd.read_csv('data/dane_open.csv', sep=';')
  high = pd.read_csv('data/dane_high.csv', sep=';')
  low = pd.read_csv('data/dane_low.csv', sep=';')
  vol = pd.read_csv('data/dane_vol.csv', sep=';')

  stocks = []
  for stock in close.columns[2:]:
    data = pd.concat([close[stock], open[stock], high[stock],
                      low[stock], vol[stock]], axis=1)
    data.columns = ['close', 'open', 'high', 'low', 'vol']
    stocks.append(data)

  return stocks
