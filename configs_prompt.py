from tkinter import *

window = Tk()
window.title("Choose folders and structure")
window.minsize(width=500, height=200)
window.config(pady=30, padx=30)

# Get origin folder
origin_folder = Entry(width=15)
origin_folder.insert(END, string="Origin Folder")
origin_folder.pack()

# Get destination folder
destination_folder = Entry(width=15)
destination_folder.insert(END, string="Destination Folder")
destination_folder.pack()

#Labels
structure_options = Label(text="Structure:")
structure_options.pack()

#Radiobutton
def structure_choice():
    return radio_state.get()
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="1 - YYYY-MM-DD", value=1, variable=radio_state, command=structure_choice)
radiobutton2 = Radiobutton(text="2 - MM-DD", value=2, variable=radio_state, command=structure_choice)
radiobutton3 = Radiobutton(text="3 - YYYY/MM/DD", value=3, variable=radio_state, command=structure_choice)
radiobutton4 = Radiobutton(text="4 - YYYYMMDD", value=4, variable=radio_state, command=structure_choice)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

# Error
error = Label(text="")
error.pack()


#Buttons
def action():
    if radio_state.get() == 0:
        error.config(text="Choose a structure")
    else:
        print(radio_state.get())
        error.config(text="")
        print(destination_folder.get())
        print(origin_folder.get())

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

window.mainloop()