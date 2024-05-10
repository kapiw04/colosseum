from market_environment import load_data, Markets, SIMULATION_LENGTH, names
from model import get_predictions
import pandas as pd

stocks = load_data()

market = Markets(stocks)
market.random_time()
predictions = get_predictions(market.get_current_states())

for _ in range(SIMULATION_LENGTH):
  market.step()
  states = market.get_current_states()
  current_states = [state.iloc[-1] for state in states]
  current_predictions = [prediction.iloc[-1] for prediction in predictions]

  for i, stock in enumerate(names):
    print(
      f'diff for {stock}: {current_states[i]["y"] - current_predictions[i]["yhat"]}')
