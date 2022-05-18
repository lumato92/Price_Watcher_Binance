import tkinter as tk
from tkinter import *
import os
from price_stream import *



LARGE_FONT=("Verdana",12)

COTIZACION=["BTCUSDT","LTCUSDT"]

class PriceWatcher(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        root=tk.Tk()
        root.title("Price")
        container=tk.Frame(self,width=300, height=300)
        #container.title("Price Watcher")
 
        container.pack(side="top",fill='both',expand=True)

        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0,weight=1)

        self.frames={}
        frame=Prices(container,self)
        self.frames[Prices]=frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.place()
        self.show_frame(Prices)


    def show_frame(self,cont):
        frame= self.frames[cont]
        frame.tkraise()
    def read_json(self):
        with open ('BTCUSDT.json') as file:
            dato=json.load(file)

        return dato
    def startOperation(self):
        os.system("cd /home/lucas/Desktop/BInance/GUI")
        os.system("python3 /home/lucas/Desktop/BInance/GUI/price_stream.py")


class Prices(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, width=300, height=300)

        button=tk.Button(self, text="Obtener Cotizacion", command=controller.startOperation)
        button.grid(column=0 ,row=2)
        label=tk.Label(self, text="Cotizacion", font=LARGE_FONT)
        self.dato=[]
        self.dato=controller.read_json()

        #label.pack(pady=10,padx=10)
        label.grid(column=1,row=0)

        label2=tk.Label(self, text="BTCUSDT")
        label2.grid(column=0, row=1)

        price1=tk.Entry(self,textvariable=StringVar(value=self.dato['p']))
        price1.grid(column=1, row=1)

def read_json():
    with open ('BTCUSDT.json') as file:
        dato=json.load(file)

    return dato

if __name__=='__main__':

   

    root=Tk()

    root.title("Price Watcher")
    dato=read_json()
    print(dato['p'])
    #precio=StringVar(read_json())
    Title_label=Label(root , text=" Price Watcher ", font= LARGE_FONT).grid(column=0, row=0)
    BTC_label=Label(root,text="BITCOIN" ,font=LARGE_FONT).grid(column=0, row=1)
    BTC_entry=Entry(root,textvariable=IntVar(value=dato['p'])).grid(column=0, row=2)
    root.update()
    root.mainloop()
