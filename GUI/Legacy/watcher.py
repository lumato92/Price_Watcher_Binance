import json
import time
import tkinter as tk
from tkinter import *

DIRECTORY="/home/lucas/Desktop/BInance/GUI/"
'''
Muestra las cotizaciones de 3 cryptomonedas refrescandolas automaticamente

Se necesita iniciar el websocket por lo que hay que ejecutar primero price_stream.py

'''
class Watcher:
    def __init__(self, master):
        

        self.prices=[]
        self.prices=self.read_json()
        self.LTC_price=IntVar()
        self.read_json()
        self.home=master
        self.home.title("Price Watcher")
        self.home.geometry("500x400")

        self.price1Label=Label(self.home,text="BTC/USDT")
        self.price1Label.grid(row=1, column=0)
        self.price2Label=Label(self.home,text="LTC/USDT")
        self.price2Label.grid(row=2, column=0)
        self.price3Label=Label(self.home,text="ETH/USDT")
        self.price3Label.grid(row=3, column=0)
        self.price1Entry=Entry(self.home,textvariable="")
        self.price1Entry.grid(row=1, column=1)
        self.price2Entry=Entry(self.home,textvariable="")
        self.price2Entry.grid(row=2, column=1)
        self.price3Entry=Entry(self.home,textvariable="")
        self.price3Entry.grid(row=3, column=1)



    
    
    def read_json(self):
        
        COTIZACION=["BTCUSDT","LTCUSDT",'ETHUSDT']
        data=[]
        try:
            for ticker in COTIZACION:
                with open(DIRECTORY+ticker+".json")as file:
                    dato=json.load(file)
                    data.append(dato['p'])
            
            return data
        except:
            return 



def refresh():
    
    main_win.prices=main_win.read_json()
    try:
        main_win.price1Entry.config(textvariable=StringVar(value=main_win.prices[0]))  
        main_win.price2Entry.config(textvariable=StringVar(value=main_win.prices[1])) 
        main_win.price3Entry.config(textvariable=StringVar(value=main_win.prices[2])) 
    except:
        print("error")
        pass
    root.after(500,refresh)    

if __name__ == "__main__":
    root=tk.Tk()
    main_win=Watcher(root)

    root.after(0,refresh)
    root.mainloop()
   