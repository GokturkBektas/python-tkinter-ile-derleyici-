import tkinter as tk
from tkinter import *
import sys
import io

def kod():

    stringio = io.StringIO()
    sys.stdout = stringio
    girilenkod = girdi.get(1.0,END)
    exec(girilenkod)
    yakalanan_cikti = sys.stdout.getvalue()
    cikti.insert(1.0,yakalanan_cikti)
    cikti.pack()

def delete():
    girdi.delete(1.0,END)
    cikti.delete(1.0,END)
    cikti.pack()


pencere = tk.Tk()
pencere.geometry("700x600")
pencere.title("Derleyici")
girdi = tk.Text(pencere,width=100,height=20)
girdi.pack(pady=10)
buton1 = tk.Button(text="Derle",command=kod)
buton1.pack(pady=0)
buton2 = tk.Button(text="Sil",command=delete)
buton2.pack(pady=0)
cikti=tk.Text(pencere,width=100,height=20)
cikti.pack(pady=10)

pencere.mainloop()