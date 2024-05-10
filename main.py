from market_environment import load_data, Markets, SIMULATION_LENGTH, names
from model import get_predictions
import pandas as pd

stocks = load_data()

market = Markets(stocks)
market.random_time()
predictions = get_predictions(market.get_current_states())

balance = 1000
owned_stocks = []


def max_profit(prices):
  """
  returns buy and sell days for max profit
  """
  n = len(prices)
  if n < 2:
    return 0, 0

  buy = 0
  sell = 1
  min_price = prices[0]
  max_profit = prices[sell] - prices[buy]

  for i in range(1, n):
    if prices[i] - min_price > max_profit:
      max_profit = prices[i] - min_price
      sell = i
    if prices[i] < min_price:
      min_price = prices[i]
      buy = i

  return buy, sell


for stock in names:
  stock_data = market.get_current_state_of_stock(stock)
  buy, sell = max_profit(stock_data['y'])
  if stock_data['y'].iloc[-1] > stock_data['y'].iloc[buy]:
    owned_stocks.append(stock)
    balance -= stock_data['y'].iloc[buy]
    balance += stock_data['y'].iloc[-1]

# sell all stocks
for stock in owned_stocks:
  stock_data = market.get_current_state_of_stock(stock)
  balance += stock_data['y'].iloc[-1]

print(balance)
