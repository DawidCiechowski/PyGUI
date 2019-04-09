from tkinter import *
import tkinter.messagebox

root = Tk()



top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

l = Label(root, text="This is a piece of text", fg="black", bg="red")


def buttonClick():
    global l
    l = Label(root, text="This is a piece of text", fg="black", bg="blue")

button_1 = Button(root, command = buttonClick, text="This is just gay", fg="blue")


l.pack()


button_1.pack(fill=X)


root.mainloop()

"""
    b = True
    l = Label(root, text = "This is a piece of text", fg = "black", bg = "blue")

    def buttonCLick(self):
        global b
        global l
        if(b == True):
            l = Label(root, text = "This is a piece of text", fg = "black", bg = "red")
            b = False
        else:
            l = Label(root, text = "This is a piece of text", fg = "black", bg = "blue")
            b = True

    def instantiate_variables(self):
        top_frame = Frame(root)
        top_frame.pack()
        bottom_frame = Frame(root)
        bottom_frame.pack()
        button_1 = Button(root, command = buttonClick, text="Click!", fg="blue")
        button_1.pack()
        l.pack()

    
    def run(self):
        root.mainloop()

c = cs()

c.instantiate_variables()
c.run()
"""



    