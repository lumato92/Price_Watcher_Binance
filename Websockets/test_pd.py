import pandas as pd 
import numpy as np

import json
'''
datos=[]
data=pd.DataFrame(datos)

while True:
    with open("BTCUSDT.json") as json_file:
        datos=json.load(json_file)
    data1=pd.DataFrame(datos)

    print(data1.tail())
'''   

COTIZACION=["BTCUSDT","LTCUSDT",'ETHUSDT']
data=[]
for ticker in COTIZACION:
    with open(ticker+".json")as file:
        dato=json.load(file)
        data.append(dato['p'])
print(data)  
