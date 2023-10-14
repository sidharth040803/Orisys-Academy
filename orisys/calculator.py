#Question 2 
 import tkinter 
 from tkinter import * 
 window=tkinter.Tk()#create window 
 window.title("Calculator")#title 
 window.geometry("500x400") 
 window.configure(bg=("black")) 
  
 expression="" 
  
 def press(num):#fn when we press the buttons 
     global expression 
     expression = expression + str(num) 
     equation.set(expression)#updates the expression 
  
 def equalpress():#fn when we press = 
     try: 
         global expression 
         total = str(eval(expression)) 
         equation.set(total) 
         expression = "" 
     except: 
         equation.set("error") 
         expression = "" 
  
 def clear():#fn when we press c 
     global expression 
     expression = "" 
     equation.set("") 
  
 equation = tkinter.StringVar() 
 expression_field = Entry(window, textvariable=equation) 
 expression_field.grid(row=1, column=0, padx=20) 
  
 label1=tkinter.Label(window, text="MY CALCULATOR", font=("Arial",15), bg="black", fg="white") 
 label1.grid(row=0, column=0, padx=20) 
  
 button1 = Button(window, text = "1", width=5, bg="white", command=lambda: press(1))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button1.grid(row=1, column=1, pady=10) 
  
 button2 = Button(window, text = "2", width=5, bg="white", command=lambda: press(2))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button2.grid(row=1, column=2, padx=5, pady=10) 
  
 button3 = Button(window, text = "3", width=5, bg="white", command=lambda: press(3))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button3.grid(row=1, column=3, padx=5, pady=10) 
  
 button4 = Button(window, text = "4", width=5, bg="white", command=lambda: press(4))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button4.grid(row=2, column=1, pady=10) 
  
 button5 = Button(window, text = "5", width=5, bg="white", command=lambda: press(5))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button5.grid(row=2, column=2, padx=5, pady=10) 
  
 button6 = Button(window, text = "6", width=5, bg="white", command=lambda: press(6))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button6.grid(row=2, column=3, padx=5, pady=10) 
  
 button7 = Button(window, text = "7", width=5, bg="white", command=lambda: press(7))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button7.grid(row=3, column=1, pady=10) 
  
 button8 = Button(window, text = "8", width=5, bg="white", command=lambda: press(8))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button8.grid(row=3, column=2, padx=5, pady=10) 
  
 button9 = Button(window, text = "9", width=5, bg="white", command=lambda: press(9))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button9.grid(row=3, column=3, padx=5, pady=10) 
  
 button10 = Button(window, text = "0", width=5, bg="white", command=lambda: press(0))#creates button - if command=print_hello() is given it shows output without clicking the button 
 button10.grid(row=4, column=2, pady=10) 
  
 decimal = Button(window, text = ".", width=5, bg="white", command=lambda: press('.'))#creates button - if command=print_hello() is given it shows output without clicking the button 
 decimal.grid(row=4, column=1, padx=5, pady=10) 
  
 equal = Button(window, text = "=", width=5, bg="white", command=equalpress)#creates button - if command=print_hello() is given it shows output without clicking the button 
 equal.grid(row=4, column=3, padx=5, pady=10) 
  
 plus = Button(window, text = "+", width=5, bg="white", command=lambda: press("+"))#creates button - if command=print_hello() is given it shows output without clicking the button 
 plus.grid(row=1, column=4, padx=5, pady=10) 
  
 minus = Button(window, text = "-", width=5, bg="white", command=lambda: press("-"))#creates button - if command=print_hello() is given it shows output without clicking the button 
 minus.grid(row=2, column=4, padx=5, pady=10) 
  
 mul = Button(window, text = "", width=5, bg="white", command=lambda: press(""))#creates button - if command=print_hello() is given it shows output without clicking the button 
 mul.grid(row=3, column=4, padx=5, pady=10) 
  
 div = Button(window, text = "/", width=5, bg="white", command=lambda: press("/"))#creates button - if command=print_hello() is given it shows output without clicking the button 
 div.grid(row=4, column=4, padx=5, pady=10) 
  
 clear = Button(window, text = "C", width=5, bg="white", command=clear)#creates button - if command=print_hello() is given it shows output without clicking the button 
 clear.grid(row=5, column=2, padx=5, pady=10) 
  
  
 window.mainloop(