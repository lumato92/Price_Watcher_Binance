from tkinter import *
import json



def read_json():
    with open("/home/lucas/Desktop/BInance/GUI/BTCUSDT.json")as file:
        dato=json.load(file)
        print(dato)
    return dato 

def refrescar():
    data=read_json()
    entry.config(textvariable=StringVar(value=data['p']))
    root.after(500,refrescar)

root=Tk()
root.title("TEST REFRESH")
root.geometry("300x200")

label=Label(root, text="BTC")
label.pack()
entry=Entry(root, textvariable=StringVar(value="HOLA"))
entry.pack()
boton=Button(root, text="refresh", command=refrescar)
boton.pack()
root.after(0,refrescar)
root.mainloop()