import sys
from tkinter import *

root = Tk()

t1 = Text(root)
t1.pack()

class PrintToT1(object):
     def write(self, s):
         t1.insert(END, s)

sys.stdout = PrintToT1()
print ('Hello, world!')
print ("Isn't this fun!")

mainloop()