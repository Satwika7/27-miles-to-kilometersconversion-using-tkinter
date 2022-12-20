from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=120)
window.config(padx=20,pady=20)
def calculate():
    val = float(input.get())*1.609
    label_0.config(text=val)

button = Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)

label = Label(text="is equal to")
label.grid(column=0,row=1)

mileslabel = Label(text="Miles")
mileslabel.grid(column=2,row=0)

kmlabel = Label(text="Km")
kmlabel.grid(column=2,row=1)

label_0 = Label(text="0")
label_0.grid(column=1,row=1)



input = Entry()
input.grid(column=1,row=0)
input.config(width=7)
input.insert(END,"0")
window.mainloop()
