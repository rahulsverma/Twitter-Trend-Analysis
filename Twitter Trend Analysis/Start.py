from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import Test as tst
import Usersearch as us
import sys


root = Tk()
root.title('Login Page')
root.geometry('400x600')

global canvas
global Image
canvas = Canvas(root, width = 400, height = 600)
img = ImageTk.PhotoImage(Image.open("D:\Twitter Trend Analysis\Twitter Trend Analysis\Login.jpg"))
canvas.create_image(0,0, anchor = NW, image = img)
canvas.pack()

def login():
    if LID.get()=="" or PSD.get()=="":
        messagebox.showerror("Error", "All fields are required!!")
    elif LID.get()=="Admin" and PSD.get()=="Admin123":
        messagebox.showinfo("Successfull",f"Welcome {LID.get()}!")
        TA()
    else:
        messagebox.showerror("Error","Invalid Username or Password")

def searchfunc():
    if SID.get()=="":
        messagebox.showerror("Error", "Search field is required!!")
    else:
        tst.tta(SID.get())

def UserSearch():
    if UID.get()=="":
        messagebox.showerror("Error", "Search field is required!!")
    else:
        user = us.usf(UID.get())
        display(user)

        

UID = StringVar()
LID = StringVar()
PSD = StringVar()
SID = StringVar()
LoginID = Label(root, text = 'Login ID')
Password = Label(root, text = 'Password')
Textbox1 = Entry(root,bd = 2, textvariable = LID)
Textbox2 = Entry(root,bd = 2, show='*', textvariable = PSD)
Login = Button(root, text = "Login", bd= 2, command = login)
#searchkey= SID
#tst.tta(searchkey)


LoginID.place(x=85, y=200)
Password.place(x=85, y=250)
Textbox1.place(x=150, y =200)
Textbox2.place(x=150, y =250)
Login.place(x=150, y=300, height = 35, width = 100)


def display(user):
    top1 = Toplevel()
    top1.title('Result')
    top1.geometry('200x200')
    t1 = Text(top1)
    t1.pack()

    class PrintToT1(object):
        def write(self, s):
            t1.insert(END, s)

    sys.stdout = PrintToT1()
    user()

def TA():
    top = Toplevel()
    top.title('Twitter Analysis')
    top.geometry('600x600')

    global Canvas
    global image
    Canvas = Canvas(top, width = 600, height = 1200)
    image = ImageTk.PhotoImage(Image.open("D:\Twitter Trend Analysis\Twitter Trend Analysis\Twitter.jpg"))
    Canvas.create_image(0,0, anchor = CENTER, image = image)
    Canvas.pack()


    Description = Label(top, font = ("Arial", 32,), bd = 0, bg = 'cyan', fg = 'White', width = 0, height = 0, text = 'Twitter Trend Analysis')
    SearchLabel = Label(top, text = 'Enter the Hashtag')
    Search = Button(top, text = "Search", bd= 2, command = searchfunc)
    Searchbox = Entry(top, bd = 4, width = 40, textvariable = SID)
    UserLabel = Label(top, text = 'Enter the user to be searched', wraplength = 104)
    Searchbox2 = Entry(top, bd = 4, width = 40, textvariable = UID)
    Search2 = Button(top, text = "Search", bd= 2, command = UserSearch)






    Description.place(x=100, y=50)
    SearchLabel.place(x=90, y=150)
    Search.place(x=460, y=150, height = 23, width = 55)
    Searchbox.place(x=200, y=150)
    UserLabel.place(x=90,y=200)
    Searchbox2.place(x=200, y=200)
    Search2.place(x=460, y=200, height = 23, width = 55)



    
    
    

root.mainloop()
