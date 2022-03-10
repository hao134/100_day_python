import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=120)


mileentry = tkinter.Entry(width = 10)
mileentry.grid(column=1,row=0)

Miles = tkinter.Label(text="Miles",font = ("Arial", 18, "italic"))
Miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to", font=("Arial",18))
is_equal_to.grid(column=0,row=1)

km_value = tkinter.Label(text = "0")
km_value.grid(column= 1, row = 1)

Km = tkinter.Label(text="Km",font = ("Arial", 18, "italic"))
Km.grid(column=2, row=1)

def button_event():
    km_value["text"] = round(float(mileentry.get()) * 1.609344,2)

Calculator_button = tkinter.Button(text="Calculator", command = button_event)
Calculator_button.grid(column=1, row=2)







window.mainloop()