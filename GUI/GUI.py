import tkinter as tk

import matplotlib

matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.backends._backend_tk 
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style




LARGE_FONT=("Verdana",12)
style.use("ggplot")
f=Figure(figsize=(5,5),dpi=100)
a=f.add_subplot(111)



class BinanceGUIapp(tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args,**kwargs)
        container=tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (StartPage, PageOne,PageTwo, PageThree):
            frame= F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame= self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button=tk.Button(self, text="Visit Page 1",command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2=tk.Button(self,text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3=tk.Button(self,text="Graficos", command=lambda: controller.show_frame(PageThree))
        button3.pack()

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        print("hola")
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Pagina 1",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1=tk.Button(self,text="Volver a HOME", 
        command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2=tk.Button(self,text="Pagina 2", 
        command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Pagina 2",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1=tk.Button(self,text="Volver a HOME", 
        command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2=tk.Button(self,text="Pagina Uno", 
        command=lambda: controller.show_frame(PageOne))
        button2.pack()

class PageThree(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Graficos",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1=tk.Button(self,text="Volver a HOME", 
        command=lambda: controller.show_frame(StartPage))
        button1.pack()


        canvas=FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        #toolbar=NavigationToolbar2TkAgg(canvas,self)
        #toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app=BinanceGUIapp()
app.mainloop()