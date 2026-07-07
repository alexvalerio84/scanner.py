import time
from strategy import ThreeCandleStrategy
from iq_connection import IQConnection
from config import ASSETS, TIMEFRAME, SCAN_INTERVAL

strategy = ThreeCandleStrategy()
iq = IQConnection()

class Scanner:

    def __init__(self):
        self.last_signals = {}

    def start(self):

        iq.connect()

        while True:

            for asset in ASSETS:

                candles = iq.get_candles(
                    asset=asset,
                    timeframe=TIMEFRAME
                )

                signal = strategy.analyze(candles)

                if signal:

                    key = f"{asset}-{signal['signal']}"

                    if self.last_signals.get(asset) != key:

                        self.last_signals[asset] = key

                        print(
                            f"🔔 {asset} -> {signal['signal']}"
                        )

            time.sleep(SCAN_INTERVAL)
