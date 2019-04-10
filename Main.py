from tkinter import *
import tkinter.messagebox

#Instantiate tkinter
root = Tk()

root.title("Playaround")

#Add top and bottom frames to the window
top_frame = Frame(root, width=250)
top_frame.pack()

bottom_frame = Frame(root, width = 300)
bottom_frame.pack(side = BOTTOM)

#Instantiate the label and change colour variables
l = Label(root, text="Colour: blue", fg="black", bg = "blue")
change_colour = True

#Button listener. Change the colour of label's bg, depending on the 'change_colour' value
def buttonClick():
    global l
    global change_colour
    if(change_colour == True):
        l.configure(text="Colour: red", bg = "red")
        change_colour = False
    else:
        l.configure(text="Colour: blue", bg = "blue")
        change_colour = True

#Instanitate the button with listener
button_1 = Button(root, command = buttonClick, text="Click", fg="blue")

#Pack everything
l.pack(fill = X)


button_1.pack()

#Run mainloop
root.mainloop()



    