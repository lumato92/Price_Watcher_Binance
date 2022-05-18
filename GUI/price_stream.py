#from api_keys import API_KEY, API_SECRET

from binance.client import Client
from binance.websockets import BinanceSocketManager
import time
import json
API_KEY="RY4gb2a33jYQjoVilZnZbUjHsZGCt2QDQOSm80XXSDp6J2uUIM2fpLrR2ScmbL0c"

API_SECRET="s5WTOO7gXTov9YNFFNjPLTc3tjXifHQ1KelwAW5tnYNZkOfQWvY8Sax1uTjostDh"

COTIZACION=["BTCUSDT","LTCUSDT",'ETHUSDT','XRPUSDT']

client= Client(API_KEY, API_SECRET)
def process_message(msg):
        
    #print("message type: {}".format(msg['e']))
    data=msg
    with open(data['s']+'.json','w') as json_file:
        json.dump(data,json_file)

def price_stream(ticker):
    bm = BinanceSocketManager(client)
   
    bm.start_aggtrade_socket(ticker, process_message)
    bm.start()


def start_websocket(*args):
    print("Conectando Websocket ...")
    try:
        for ticker in COTIZACION:
            price_stream(ticker)
    except:
        pass
    print("Inicializacion Completa")
    
if __name__=="__main__":
    start_websocket(COTIZACION)



