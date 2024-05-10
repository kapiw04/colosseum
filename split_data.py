import pandas as pd

close = pd.read_csv('data/dane_close.csv', sep=';')
open = pd.read_csv('data/dane_open.csv', sep=';')
high = pd.read_csv('data/dane_high.csv', sep=';')
low = pd.read_csv('data/dane_low.csv', sep=';')
vol = pd.read_csv('data/dane_vol.csv', sep=';')

for stock in close.columns[2:]:
    data = pd.concat([close[stock], open[stock], high[stock],
                      low[stock], vol[stock]], axis=1)
    data.columns = ['close', 'open', 'high', 'low', 'vol']
    data.to_csv(f'data/stocks/{stock}.csv', index=False, sep=';')
