import ta
import pandas as pd

from ta.momentum import RSIIndicator, KAMAIndicator, PercentagePriceOscillator, WilliamsRIndicator
from ta.volume import OnBalanceVolumeIndicator, AccDistIndexIndicator
from ta.volatility import BollingerBands
from ta.trend import EMAIndicator, MACD, PSARIndicator, CCIIndicator, IchimokuIndicator, AroonIndicator

def cols_to_series(df):
    s_open = df['open']
    s_close = df['close']
    s_high = df['high']
    s_low = df['low']
    s_vol = df['vol']

    return s_open, s_close, s_high, s_low, s_vol

class Indicators():
    def cols_to_series(self):
        self.sopen = self.df['open']
        self.sclose = self.df['close']
        self.shigh = self.df['high']
        self.slow = self.df['low']
        self.svol = self.df['vol']

    def initIndicators(self):
        # momentum indicators
        self.KAMA = KAMAIndicator(self.sclose)
        self.RSII = RSIIndicator(self.sclose)
        self.PPO = PercentagePriceOscillator(self.sclose)
        self.WR = WilliamsRIndicator(self.shigh, self.slow, self.sclose)

        # volume indicators
        self.OBV = OnBalanceVolumeIndicator(self.sclose, self.svol)
        self.ADII = AccDistIndexIndicator(self.shigh, self.slow, self.sclose, self.svol)

        # volatility indicators
        self.BB = BollingerBands(self.sclose)

        # trend indicators
        self.EMA = EMAIndicator(self.sclose)
        self.MACDI = MACD(self.sclose)
        self.PSAR = PSARIndicator(self.shigh, self.slow, self.sclose)
        self.CCI = CCIIndicator(self.shigh, self.slow, self.sclose)
        self.ICHI = IchimokuIndicator(self.shigh, self.slow)
        self.AROON = AroonIndicator(self.shigh, self.slow)

    def getIndicators(self):
        self.kama = self.KAMA.kama()
        self.rsii = self.RSII.rsi()
        self.ppo = self.PPO.ppo()
        self.wr = self.WR.williams_r()

        self.obv = self.OBV.on_balance_volume()
        self.adii = self.ADII.acc_dist_index()

        self.bb_hband = self.BB.bollinger_hband()
        self.bb_lband = self.BB.bollinger_lband()
        self.bb_mband = self.BB.bollinger_mavg()

        self.ema = self.EMA.ema_indicator()
        self.macd = self.MACDI.macd()
        self.psar = self.PSAR.psar()
        self.cci = self.CCI.cci()
        self.ichi = self.ICHI.ichimoku_base_line()
        self.aroon = self.AROON.aroon_indicator()

    def addColumns(self):
        self.df = self.df.assign(kama=self.kama)
        self.df = self.df.assign(rsi=self.rsii)
        self.df = self.df.assign(ppo=self.ppo)
        self.df = self.df.assign(williams_r=self.wr)
        self.df = self.df.assign(obv=self.obv)
        self.df = self.df.assign(adi=self.adii)
        self.df = self.df.assign(bb_hband=self.bb_hband)
        self.df = self.df.assign(bb_lband=self.bb_lband)
        self.df = self.df.assign(bb_mband=self.bb_mband)
        self.df = self.df.assign(ema=self.ema)
        self.df = self.df.assign(macd=self.macd)
        self.df = self.df.assign(psar=self.psar)
        self.df = self.df.assign(cci=self.cci)
        self.df = self.df.assign(ichi=self.ichi)
        self.df = self.df.assign(aroon=self.aroon)
        
        return self.df

    def engineerData(self, filepath):
        df = pd.read_csv(filepath, sep=';')

        self.df = df

        self.cols_to_series()
        
        self.initIndicators()
        self.getIndicators()

        self.df = self.addColumns()

        return self.df 

filepath = "data/sampleALE.csv"

indicators = Indicators()
df = indicators.engineerData(filepath)