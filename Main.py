from tkinter import *
import tkinter.messagebox

#Instantiate tkinter
root = Tk()

#Add top and bottom frames to the window
top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

#Instantiate the label and change colour variables
l = Label(root, text="This is a piece of text", fg="black", bg = "blue")
change_colour = True

#Button listener. Change the colour of label's bg, depending on the 'change_colour' value
def buttonClick():
    global l
    global change_colour
    if(change_colour == True):
        l.configure(bg = "red")
        change_colour = False
    else:
        l.configure(bg = "blue")
        change_colour = True

#Instanitate the button with listener
button_1 = Button(root, command = buttonClick, text="Click", fg="blue")

#Pack everything
l.pack()


button_1.pack(fill=X)

#Run mainloop
root.mainloop()



    