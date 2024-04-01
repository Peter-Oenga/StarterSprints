from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Mr. President")

#r = IntVar()
#r.set("2")

MODES = [
    ("peter", "peter"),
    ("James", "Karanja"),
    ("Jacob", "Juma"),
]

name = StringVar
name.set("James", "Karanja")

for first_name, surname in MODES:
    Radiobutton(root, text=first_name, variable=name, value=surname).pack()



def clicked(value):

    my_label = Label(root, text=name.get(value))
    my_label.pack()


Radiobutton(root, text="option 1", variable=name, value=1, command=lambda: clicked(name.get())).pack()
Radiobutton(root, text="Option 2", variable=name, value=2, command=lambda: clicked(name.get())).pack()

myButton = Button(root, text="Click here", command=lambda: clicked(r.get()))
myButton.pack()

my_label = Label(root, text=r.get())
my_label.pack()

root.mainloop()
