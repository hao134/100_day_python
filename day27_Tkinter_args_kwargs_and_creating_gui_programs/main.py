import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx = 100, pady=100)

# Label

my_label = tkinter.Label(text = "I Am a Label", font = ("Arial", 24, "italic"))
my_label.pack(side= "left")


# same
my_label["text"] = "New Text"
my_label.config(text = "New Text")
my_label.grid(column = 0, row = 0)
my_label.config(padx=50, pady=50)

# Button

def button_clicked():
    print("I got clicked")

def change_text():
    my_label["text"] = "I changed"



# Entry

myentry = tkinter.Entry(width = 10)
myentry.grid(column=4,row=3)

def button_event():
    if myentry.get() != '':
        my_label["text"] = myentry.get()

button = tkinter.Button(text="Click me", command = button_event)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="new button")
new_button.grid(column = 2, row=0)





window.mainloop()
