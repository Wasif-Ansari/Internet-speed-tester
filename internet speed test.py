
from tkinter import *
import speedtest


sp = Tk() 
sp.title(" INTERNET SPEED TEST ") #name
sp.geometry("500x650") #size
sp.config(bg = "blue") #background using config

lab = Label(sp,text = "Internet Speed Test", font = ("Time New Roman",30,"bold","italic"),bg = "blue",fg = "White")
lab.place(x = 60 , y=40 , height=50 ,width=380)



sp.mainloop() 