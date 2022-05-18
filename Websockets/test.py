from price_stream import *
from show_price import *
import time


price_stream("XRPUSDT")
price_stream("BTCUSDT")

while True:
    show_json("XRPUSDT")
    time.sleep(1)
    show_json("BTCUSDT")