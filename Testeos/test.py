from GUI.Legacy.api_keys import API_KEY, API_SECRET

from binance.client import Client
from binance.websockets import BinanceSocketManager
import time
import csv
import json

client= Client(API_KEY, API_SECRET)
'''
prices=client.get_all_tickers()


print(prices)

'''

def write_csv(datos):
    with open("data.csv", 'w') as f:
        w=csv.DictWriter(f,datos.keys())
        w.writerow(datos)
    return

# start aggregated trade websocket for BNBBTC
def process_message(msg):
    global data
    print("message type: {}".format(msg['e']))
    data=msg
    with open("ticker.json",'w') as json_file:
        json.dump(data,json_file)
    
    #write_csv(msg)
        
        
       

        # do somethin


def data_stream(ticker):
    bm = BinanceSocketManager(client)
   
    bm.start_aggtrade_socket(ticker, process_message)
    bm.start()
    
    #bm.close()
    #print("FIN")
    return
# -----Info de cuenta------
# #print(client.get_account())

#----------Status de cuenta

print(client.get_account_status())  


#------------Info balance total en referencia a un valor

#print(client.get_asset_balance("XRP"))

#----------Info todos los Trades
#print(client.get_my_trades(symbol="LTCUSDT"))

if __name__ == "__main__":
    global data
    
    client= Client(API_KEY, API_SECRET)
    data_stream("LTCUSDT")
