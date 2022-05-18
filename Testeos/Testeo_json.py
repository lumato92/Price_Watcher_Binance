from GUI.Legacy.api_keys import API_KEY, API_SECRET
import time

from Testeos.binance_api import API

import json

def precios_10s(**kwargs):

    data=API(API_KEY,API_SECRET)
    
    print(data.ticker_price(**kwargs))
    time.sleep(10)

if __name__=="__main__":

    #datos=API(API_KEY,API_SECRET)
    '''
    data=datos.ticker_price(symbol="BTCUSDT")
    with open("data.json",'w')as json_file:
        json.dump(data,json_file)
    '''
    #Data=datos.last_trades(symbol="BTCUSDT")
    #with open("BTCUSDT1.json",'w')as json_file:
    #    json.dump(data,json_file)
    
while True:
    precios_10s(symbol="LTCUSDT")


