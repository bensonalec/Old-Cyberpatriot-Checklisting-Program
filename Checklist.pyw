from tkinter import *
from oop import *
root = Tk()
background = PhotoImage(file="back1.png")
backgroundLabel = Label(root, image=background)
backgroundLabel.place(x=0, y=0)
users(root)
programs(root)
files(root)
log(root)
checklist(root)
root.resizable(width=FALSE, height=FALSE)
root.minsize(width=1050,height=700)
root.mainloop()

