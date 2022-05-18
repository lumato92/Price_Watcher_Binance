import json
import time
import tkinter as tk
from tkinter import *
from telegram import telegram_bot
from price_stream import start_websocket, COTIZACION
import os
import threading

DIRECTORY="/home/lucas/Desktop/BInance/GUI/"
'''
Muestra las cotizaciones de 3 cryptomonedas refrescandolas automaticamente

Se necesita iniciar el websocket por lo que hay que ejecutar primero price_stream.py

'''
class Watcher:
    def __init__(self, master):
        self.alertas=False
        self.alertBTC=IntVar()
        self.alertLTC=IntVar()
        self.alertETH=IntVar()
        self.prices=[]
        self.prices=self.read_json()
        self.LTC_price=IntVar()
        self.read_json()

        self.home=master
        self.home.title("Price Watcher")
        self.home.geometry("500x400")



        self.titleLabel=Label(self.home,text=" Crypto Price Watcher " ,font=("Helvetica",16)).grid(pady=10, row=0,column=0, columnspan=4)
        self.price1Label=Label(self.home,text="BTC/USDT")
        self.price1Label.grid(row=1, column=0)
        self.alert1=Label(self.home, text="ALERT ")
        self.alert1.grid(row=1, column=2)
        self.price2Label=Label(self.home,text="LTC/USDT")
        self.price2Label.grid(row=2, column=0)
        self.alert2=Label(self.home, text="ALERT ").grid(row=2, column=2)
        self.price3Label=Label(self.home,text="ETH/USDT")
        self.price3Label.grid(row=3, column=0)
        self.alert1=Label(self.home, text="ALERT ").grid(row=3, column=2)
        self.price1Entry=Entry(self.home,textvariable="")
        self.price1Entry.grid(row=1, column=1)
        self.price2Entry=Entry(self.home,textvariable="")
        self.price2Entry.grid(row=2, column=1)
        self.price3Entry=Entry(self.home,textvariable="")
        self.price3Entry.grid(row=3, column=1)


        self.alert1Entry=Entry(self.home, textvariable=self.alertBTC)
        self.alert1Entry.grid(row=1 , column=3)
        self.alert2Entry=Entry(self.home, textvariable=self.alertLTC)
        self.alert2Entry.grid(row=2 , column=3)
        self.alert3Entry=Entry(self.home, textvariable=self.alertETH)
        self.alert3Entry.grid(row=3 , column=3)


        self.alert1Boton=Button(self.home, text="Set", command=self.set_alert)
        self.alert1Boton.grid(row=1, column=4)

        self.alert2Boton=Button(self.home, text="Set", command=self.set_alert)
        self.alert2Boton.grid(row=2, column=4)

        self.alert3Boton=Button(self.home, text="Set", command=self.set_alert)
        self.alert3Boton.grid(row=3, column=4)
    
#--------Boton Start Websocket-------

        self.WebsocketButton=Button(self.home, text="Start Websocket", command=self.start_websocket)
        self.WebsocketButton.grid(row=4, column=0, columnspan=2)

    def start_websocket(self):
        #start_websocket(COTIZACION)
        self.WebsocketButton.config(bg="Green")
        threading.Thread.start(os.system("python3 price_stream.py"))
        print("OK")
    
    def set_alert(self):
        self.alertas=True



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

def alerts(precios):
    try:
        if main_win.alertas:
            if main_win.alertBTC.get()< float(precios[0]):
                telegram_bot("BTC ALERT PRICE:"+str(main_win.alertBTC.get()))
        
                main_win.alertas=False
                
            if main_win.alertLTC.get()< float(precios[1]):
                #print("El precio llego a ",main_win.alertLTC.get())
                pass
            if main_win.alertETH.get()< float(precios[2]):
                #print("El precio llego a ",main_win.alertETH.get())
                pass
        else:
            pass
    except:
        pass

def refresh():
    main_win.prices=main_win.read_json()
    
    alerts(main_win.prices)

    try:
        main_win.price1Entry.config(textvariable=StringVar(value=main_win.prices[0]))  
        main_win.price2Entry.config(textvariable=StringVar(value=main_win.prices[1])) 
        main_win.price3Entry.config(textvariable=StringVar(value=main_win.prices[2])) 
    except:
        print("error")
        pass
    root.after(500,refresh)    

if __name__ == "__main__":
    alert_BTC=True
    root=tk.Tk()
    main_win=Watcher(root)
   

    root.after(0,refresh)
    root.mainloop()
   