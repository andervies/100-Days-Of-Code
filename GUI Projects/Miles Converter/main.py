import tkinter
# from tkinter import *
#
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
#


# def button_got_clicked():
#     my_label["text"] = input.get()
#
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.grid(column=1, row=1)
#
# button = tkinter.Button(text="Click Me", command=button_got_clicked)
# button.grid(column=2, row=2)
#
# new_button = tkinter.Button(text="New Button", command=button_got_clicked)
# new_button.grid(column=3, row=1)
#
# input = tkinter.Entry(width=10)
# input.grid(column=20,row=4)

def convert():
    output = float(miles_input.get()) * 1.609
    converted_label.config(text=output)


window = tkinter.Tk()
window.title("Miles to Kilometer Converter")

equal = tkinter.Label()
equal.config(text="is equal to")
equal.grid(column=0, row=1, padx=10, pady=10)


miles_input = tkinter.Entry(width=7, )
miles_input.grid(column=1, row=0, padx=10, pady=10)

miles_label = tkinter.Label(text="miles")
miles_label.grid(column=2, row=0, padx=10, pady=10)

km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1, padx=10, pady=10)

converted_label = tkinter.Label(text="0")
converted_label.grid(column=1, row=1, padx=10, pady=10)

calculate_button = tkinter.Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
