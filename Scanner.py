import time
from strategy import ThreeCandleStrategy
from iq_connection import IQConnection

ASSETS = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "AUDUSD",
    "USDCAD",
    "EURJPY",
    "GBPJPY",
    "NZDUSD",
]

strategy = ThreeCandleStrategy()
iq = IQConnection()

iq.connect()

def scan():
    while True:
        for asset in ASSETS:
            candles = iq.get_candles(asset=asset)

            signal = strategy.analyze(candles)

            if signal:
                print(
                    f"[{asset}] "
                    f"{signal['signal']} "
                    f"{signal['time']}"
                )

        time.sleep(1)
