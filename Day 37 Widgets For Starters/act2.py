from tkinter import *
from datetime import date 

root = TK()
root.title('Getting Started With Widgets')
root.geometry('400x300')

lbl = Label(text= "Hey There!", fg = "white", bg= "#072F5F", height = 1 , width = 300)

name_lbl = Label(text="Full Na me", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message 
    message = "welcome to the application!\nToday's date is:"
    greet = "Hello " +name+"\n"
    text_box.insert(End, greet)
    text_box.insert(End,message )
    text_box.insert(End,date.today() )
text_box = Text(height = 3)
btn = Button (text = "Begin")