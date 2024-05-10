from market_environment import load_data, Markets, SIMULATION_LENGTH
from model import get_predictions

stocks = load_data()

market = Markets(stocks)
market.random_time()
predictions = get_predictions(market.get_current_states())

for i in range(SIMULATION_LENGTH):
  market.step()
  state = market.get_current_states()
  print("Predictions: ", predictions[market.index + i])
  print("Real values: ", state[-1])
  break
