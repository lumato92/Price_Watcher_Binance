import pandas as pd 
import numpy as np
import json
import time

from Websockets.price_stream import *


import matplotlib.pyplot as plt 

def graph():
    '''
    with open("BTCUSDT1.json") as json_file:
        data=json.load(json_file)
    
    datos=pd.DataFrame(data)

    #datos["datestamp"]=np.array(datos["time"]).astype("datetime64[s]")
    #datos.to_datetime(datos['time']).apply(lambda x:x.date())
    #datos["time"]=[datetime.fromtimestamp(x)for x in datos["time"]]
    datos['time']=pd.to_datetime(datos["time"],unit='ms')
    print(datos['time'])
    #fechas=(datos["datestamp"]).tolist()

    plt.plot(datos["time"],datos["price"])
    plt.ylabel("BTC Price")
    plt.show()

    #print(datos.describe())
    '''

def show_json():
    try:
        with open("ticker.json") as json_file:
            data=json.load(json_file)
            print("Precio :", data['p'])
    except:
        pass    
    



if __name__=="__main__":

    price_stream("ETHBTC")