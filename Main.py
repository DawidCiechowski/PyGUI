from tkinter import *
import tkinter.messagebox as mbox

#Instantiate tkinter
root = Tk()

#All main window values
root.title("Playaround")
root.resizable(width=False, height=False)
root.maxsize(500, 250)
root.minsize(500, 250)


#
first_number_label = Label(root, text="First number: ")
first_number_label.grid(column=0, row = 0)

first_number_type = IntVar()
first_number_input = Entry(root, textvariable=first_number_type)
first_number_input.grid(column=1, row =0)

second_number_label = Label(root, text="Second number: ")
second_number_label.grid(column=0, row=1, pady=10)

second_number_type = IntVar()
second_number_input = Entry(root, textvariable=second_number_type)
second_number_input.grid(column=1, row = 1, pady = 10)

result_label = Label(root, text="Result: ")
result_label.grid(column=0, row=3, sticky=W)

result = Label(root, text="")
result.grid(column=1, row = 3, sticky = W)


def define_action(action):
    global result
    global first_number_input
    global second_number_input
    number_1 = IntVar()
    number_2 = IntVar()
    number_1.set(first_number_input.get())
    number_2.set(second_number_input.get())
    if(action == "ADD"):
        final_result = number_1.get() + number_2.get()
    elif(action == "SUBSTRACT"):
        final_result = number_1.get() - number_2.get()
    elif(action == "MULTIPLY"):
        final_result = number_1.get() * number_2.get()
    elif(action == "DIVIDE" and not number_2.get() == 0):
        final_result = number_1.get() / number_2.get()
    elif(action == "DIVIDE" and number_2.get() == 0):
        mbox.showinfo("ERROR!", "Cannot divide by 0!")
    elif(action == "MODULO"):
        final_result = number_1.get() % number_2.get()

    result.configure(text=final_result)

def add_listener():
    define_action("ADD")

def substract_listener():
    define_action("SUBSTRACT")

def multiply_listener():
    define_action("MULTIPLY")

def divide_listener():
    define_action("DIVIDE")

def modulo_listener():
    define_action("MODULO")

    

add_button = Button(root, command = add_listener, text="+")
add_button.grid(column=0, row=2, sticky = W)

substract_button = Button(root, command = substract_listener, text="-")
substract_button.grid(column=0, row=2)

multiply_button = Button(root, command = multiply_listener, text="*")
multiply_button.grid(column=0, row=2, sticky = E)

divide_button = Button(root, command = divide_listener, text="/")
divide_button.grid(column=1, row=2, pady = 0)

modulo_button = Button(root, command = modulo_listener, text="%")
modulo_button.grid(column=1, row=2, sticky = E)


#Run mainloop
root.mainloop()



    