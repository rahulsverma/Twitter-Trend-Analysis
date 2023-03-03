from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import Country as ct
import sys


root = Tk()
root.title('Top Trending')
root.geometry('400x600')


def SC():
    if TID.get()=="":
        messagebox.showerror("Error", "Search field is required!!")
    else:
        ct.cst(TID.get())


TID = StringVar()
CountryID = Label(root, text = 'Country')
Textbox1 = Entry(root,bd = 2, textvariable = TID)
Search = Button(root, text = "Search", bd= 2, command = SC)










CountryID.place(x=85, y=200)
Textbox1.place(x=150, y =200)
Search.place(x=150, y=300, height = 35, width = 100)






root.mainloop()