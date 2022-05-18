import json
import time
import os


COTIZACION=["BTCUSDT","LTCUSDT",'ETHUSDT','XRPUSDT']

def show_json(ticker):
    try:
        with open(ticker +".json") as json_file:
            data=json.load(json_file)
            print(data['s'],"Precio :", data['p'])
    except:
        pass    

if __name__ == "__main__":
    while True:
        for ticker in COTIZACION:
            show_json(ticker)
        
        os.system("clear")
        time.sleep(1)
        
    pass  