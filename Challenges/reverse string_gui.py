#importing Libraries
from tkinter import *
import random, string
import pyperclip

###initialize window
root =Tk()
root.geometry("600x400")
#root.resizable(0,0)
root.title("String Reverse")

#heading
# heading = Label(root, text = 'String Reverse' , font ='arial 15 bold').pack()
Label(root, text ='String Reverse - Polymeras', font ='arial 15 bold').pack(side = BOTTOM)
Label(root, text = 'TEXT TO REVERSE', font = 'arial 10 bold', bg="Orangered1").pack()

Msg = StringVar
e = Entry(root, textvariable=Msg, width = 100, bg="White")
e.pack()


#####define functions

def reverse():
    global antwort 
    reverse_text = e.get()
    print(reverse_text)
    antwort = reverse_string(reverse_text).capitalize()
    my_label = Label(root, text=antwort, font ='arial 15 bold', bg="White")
    my_label.pack()

def reverse_string(text):
    if len(text) <= 1:
        return text
    first_char = text[0]
    remaining = text[1:]
    return reverse_string(remaining) + first_char


###buttons
Button(root, text = "GENERATE REVERSE" , command = reverse ).pack(pady= 5)

########function to copy
def Copy_password():
    pyperclip.copy(antwort)
    Button(root, text = "Text ist Copiert!", bg="Green").pack()

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)


# loop to run program
root.mainloop()