import tkinter 
 import random 
 from tkinter import * 
 window=tkinter.Tk()#create window 
 window.title("Password Generator")#title 
 window.geometry("400x400") 
 window.configure(bg=("black")) 
  
 def gen(): 
     letters = [ 
     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
     'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
     'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 
     ] 
     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
  
     password_list = [] 
     nr_letters=int(element1.get()) 
     for char in range(0, nr_letters + 1): 
         password_list += random.choice(letters) 
  
     nr_symbols=int(element2.get()) 
     for char in range(0, nr_symbols + 1): 
         password_list += random.choice(symbols) 
  
     nr_numbers=int(element3.get()) 
     for char in range(0, nr_numbers): 
         password_list += random.choice(numbers) 
  
     random.shuffle(password_list) 
  
     password = "" 
     for char in password_list: 
         password += char 
  
     label6.config(text="Your newly generated password is :", fg="white", bg="black") 
     label5.config(text=password, fg="white",bg="black") 
  
 label1=tkinter.Label(window, text="Welcome to the PyPassword Generator!", bg="#FF7256") 
 label1.grid(row=0, column=0, padx=20) 
  
 label2=tkinter.Label(window, text="How many letters would you like in your password?", bg="black", fg="white") 
 label2.grid(row=1, column=0, padx=15, pady=5) 
  
 element1=tkinter.Entry()#create small entry field 
 element1.grid(row=2, column=0, padx=20, pady=5) 
  
 label3=tkinter.Label(window, text="How many symbols would you like?", bg="black", fg="white") 
 label3.grid(row=3, column=0, padx=15, pady=5) 
  
 element2=tkinter.Entry()#create small entry field 
 element2.grid(row=4, column=0, padx=20, pady=5) 
  
 label4=tkinter.Label(window, text="How many numbers would you like?", bg="black", fg="white") 
 label4.grid(row=5, column=0, padx=15, pady=5) 
  
 element3=tkinter.Entry()#create small entry field 
 element3.grid(row=6, column=0, padx=20, pady=5) 
  
 button1 = Button(window, text = "Generate password", command=gen, bg="#FF7256")#creates button - if command=print_hello() is given it shows output without clicking the button 
 button1.grid(row=7, column=0, pady=10) 
  
 label5=tkinter.Label(window, text="",bg="black") 
 label5.grid(row=9, column=0, padx=15, pady=3) 
  
 label6=tkinter.Label(window, text="", bg="black") 
 label6.grid(row=8, column=0, padx=15, pady=5) 
  
  
  
 window.mainloop()