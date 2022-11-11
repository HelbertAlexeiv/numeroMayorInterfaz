from tkinter import *
from tkinter import messagebox
root = Tk()
root.resizable(False, False)
number1 = StringVar()
number2 = StringVar()
def biggerNumber():
    if int(number1.get()) > int(number2.get()):
        messagebox.showinfo("Mayor", "El numero mayor es " + str(number1.get()))
        number1.set("")
        number2.set("")

    else:
        messagebox.showinfo("Mayor", "El numero mayor es " + str(number2.get()))
        number1.set("")
        number2.set("")

#--------Frame de datos
dataFrame = Frame(root)
dataFrame.config(bd=20, relief="raised")
number1Label = Label(dataFrame, text="Ingrese un numero:", font=("Times new roman", 15))
number1Entry = Entry(dataFrame, textvariable=number1, font=("Times new roman", 15))
number2Label = Label(dataFrame, text="Ingrese un numero:", font=("Times new roman", 15))
number2Entry = Entry(dataFrame, textvariable=number2, font=("Times new roman", 15))

number1Label.grid(row=0, column=0)
number1Entry.grid(row=0, column=1)
number2Label.grid(row=1, column=0)
number2Entry.grid(row=1, column=1)

#--------Frame de procesos
processFrame = Frame(root, bd=10)
calculateButton = Button(processFrame, text="Mayor", font=("Times new roman", 15), command=biggerNumber)

calculateButton.grid(row=0, column=0)

processFrame.grid(row=1, column=0)
dataFrame.grid(row=0, column=0)

root.mainloop()
