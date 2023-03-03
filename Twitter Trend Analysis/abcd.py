from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import Test as tst


root = Tk()
root.title('Twitter Analysis')
root.geometry('600x600')

Canvas = Canvas(root, width = 600, height = 1200)
image = ImageTk.PhotoImage(Image.open("D:\Twitter Trend Analysis\Twitter Trend Analysis\Twitter.jpg"))
Canvas.create_image(0,0, anchor = CENTER, image = image)
Canvas.pack()



Description = Label(root, font = ("Arial", 32,), bd = 0, bg = 'cyan', fg = 'White', width = 0, height = 0, text = 'Twitter Trend Analysis')
SearchLabel = Label(root, text = 'Enter the Hashtag')
Search1 = Button(root, text = "Search", bd= 2,)
Searchbox1 = Entry(root, bd = 4, width = 40,)
UserLabel = Label(root, text = 'Enter the user to be searched', wraplength = 104)
Searchbox2 = Entry(root, bd = 4, width = 40,)
Search2 = Button(root, text = "Search", bd= 2,)









Description.place(x=100, y=50)
SearchLabel.place(x=90, y=150)
Search1.place(x=460, y=150, height = 23, width = 55)
Searchbox1.place(x=200, y=150)
UserLabel.place(x=90,y=200)
Searchbox2.place(x=200, y=200)
Search2.place(x=460, y=200, height = 23, width = 55)
























root.mainloop()