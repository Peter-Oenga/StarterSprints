from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Mr. President")

img1 = ImageTk.PhotoImage(Image.open("images/mrPresident.jpeg"))
#img2 = ImageTk.PhotoImage(Image.open("images/ME1.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("images/ME2.jpeg"))
img4 = ImageTk.PhotoImage(Image.open("images/ME3.jpeg"))
image_list = [img1, img3, img4]
status = Label(root, text="image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)

def back(image_number):
    global my_label
    global back_button
    global forward_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    forward_button = Button(root, text=">>", command=forward(image_number - 1))
    back_button = Button(root, text="<<", command=back(image_number - 1))

    if image_number == 1:
        back_button = Button(root, text="<<", state=DISABLED)

    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    status = Label(root, text="image" + str(image_number) + "of" + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forward(image_number):
    global my_label
    global back_button
    global forward_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    forward_button = Button(root, text=">>", command=lambda: forward(image_number + 1))
    back_button = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        forward_button = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    status = Label(root, text="image" + str(image_number) + "of" + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



back_button = Button(root, text="<<", command=back)
exit_button = Button(root, text="Exit", command=root.quit)
forward_button = Button(root, text=">>", command=lambda: forward(2))

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()