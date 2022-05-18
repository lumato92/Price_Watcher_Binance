from time import time
from GUI.Legacy.api_keys import API_KEY, API_SECRET

import csv
from binance.client import Client
from binance.websockets import BinanceSocketManager


import pandas as import pd


#csv writer controls
#columns = ['e','E','s','a','p','q','f','l','T','m','M'] # add whatever JSON keys you want
#out = csv.DictWriter(open('DataBase.csv', 'w'),columns)
def set_column_name():
    fieldnames=['Type','Time(Unix)','Symbol','Trade Id','Price','Quantity','First Tradeid','Last TradeID','Trade Time','Buyer is Maker','M']
    f=open('test.csv','w')
    write=csv.DictWriter(f,fieldnames)
    write.writeheader()
 

#callback function
def get_live_data_trade(symbol):

    set_column_name()
    columns = ['e','E','s','a','p','q','f','l','T','m','M'] # add whatever JSON keys you want
    out = csv.DictWriter(open(symbol+'.csv', 'w'),columns)

    global bm
    client = Client(api_key =API_KEY, api_secret = API_SECRET)
    bm = BinanceSocketManager(client)
    bm.start_aggtrade_socket(symbol, out.writerow)
    bm.start()
    
#start writing to csv
#initiate()





if __name__=="__main__":
    get_live_data_trade("LTCUSDT")
    print("hola")


