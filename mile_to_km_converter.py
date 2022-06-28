#Mile to km converter

from curses import KEY_MESSAGE
from tkinter import * #import every class in tkinter

window = Tk()
window.title("Mile to km converter")
window.minsize(width = 500, height=300)
window.config(padx=20, pady=20)

#Entry
input = Entry(width = 10)
input.grid(column=1, row=0)

#Label
my_label = Label(text="Miles", font = ("Arial"))
my_label.grid(column=2, row=0)
my_label.config(padx=20, pady=20)

my_label2 = Label(text="is equal to", font = ("Arial"))
my_label2.grid(column=0, row=1)
my_label2.config(padx=20, pady=20)

my_label3 = Label(text="km", font = ("Arial"))
my_label3.grid(column=2, row=1)
my_label3.config(padx=20, pady=20)

my_label4 = Label(text="0", font = ("Arial"))
my_label4.grid(column=1, row=1)
my_label4.config(padx=20, pady=20)


#Button

def button_clicked():
    mile = input.get()
    km = float(mile)*1.60934

    my_label4.config(text=km)

button = Button(text = "Calculate", command = button_clicked)
button.grid(column=1, row=2)


window.mainloop()

