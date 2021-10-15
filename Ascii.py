# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:10:27 2021

@author: DELL
"""

from tkinter import *
root=Tk()
root.title("Ascii")
root.geometry("400x400")

entry_word=Entry(root)
entry_word.place(relx=0.5, rely=0.4, anchor=CENTER)
print(100)
label=Label(root, text="Ascii number of the word is: ")
def Ascii_converter():
    input_word=entry_word.get()
    for letter in input_word:
        label["text"]+=str(ord(letter))+" "
        
btn=Button(root, text="Show name in Ascii", command=Ascii_converter)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
label.place(relx=0.5, rely=0.5, anchor=CENTER)












root.mainloop()