from tkinter import *
import tkinter.messagebox as mbox

#Instantiate tkinter
root = Tk()

#All main window values
root.title("Playaround")
root.resizable(width=False, height=False)


#
first_number_label = Label(root, text="First number: ")
first_number_label.grid(column=0, row = 0, sticky=W)

first_number_type = IntVar()
first_number_input = Entry(root, textvariable=first_number_type)
first_number_input.grid(column=1, row =0, sticky=W)

second_number_label = Label(root, text="Second number: ")
second_number_label.grid(column=0, row=1, sticky=W)

second_number_type = IntVar()
second_number_input = Entry(root, textvariable=second_number_type)
second_number_input.grid(column=1, row = 1, pady = 10)

result_label = Label(root, text="Result: ")
result_label.grid(column=0, row=4, sticky=W, pady = 20)

result = Label(root, text="")
result.grid(column=1, row = 4, sticky = W, pady = 20)


def define_action(action):
    global result
    global first_number_input
    global second_number_input
    number_1 = IntVar()
    number_2 = IntVar()
    number_1.set(first_number_input.get())
    number_2.set(second_number_input.get())
    if(action == "ADD"):
        final_result = number_1.get() + number_2.get() #ADD
    elif(action == "SUBSTRACT"):
        final_result = number_1.get() - number_2.get() #SUBSTRACT
    elif(action == "MULTIPLY"):
        final_result = number_1.get() * number_2.get() #MULTIPLY
    elif(action == "DIVIDE" and not number_2.get() == 0):
        final_result = number_1.get() / number_2.get() #DIVIDE
    elif((action == "DIVIDE" or action == "MODULO") and number_2.get() == 0):
        mbox.showinfo("ERROR!", "Cannot divide by 0!") #DIVIDING BY 0
    elif(action == "MODULO"):
        final_result = number_1.get() % number_2.get() #MODULO

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

    

add_button = Button(root, command = add_listener, text="+", height=1, width=1)
add_button.grid(row=2, column=0, sticky = E)

substract_button = Button(root, command = substract_listener, text="-", height=1, width=1)
substract_button.grid(row=2, column=1, sticky = W)

multiply_button = Button(root, command = multiply_listener, text="*", height=1, width=1)
multiply_button.grid(row=2, column=1, sticky=W, padx=16)

divide_button = Button(root, command = divide_listener, text="/", height=1, width=1)
divide_button.grid(row=3, column=0,sticky = E)

modulo_button = Button(root, command = modulo_listener, text="%", height=1, width=1)
modulo_button.grid(row=3, column=1, sticky=W)

root.grid_columnconfigure(100, weight=1)
root.grid_rowconfigure(2, weight=1)


#Run mainloop
root.mainloop()



    