import tkinter 
 from tkinter import * 
 window=tkinter.Tk() 
 window.title("Greet") 
 window.geometry("400x400") 
  
 label1=tkinter.Label(window,text="Hello, World!") 
 label1.config(font =("Courier",15)) 
 label1.config(bg =("#7AC5CD")) 
 label1.pack() 
  
 window.mainloop()