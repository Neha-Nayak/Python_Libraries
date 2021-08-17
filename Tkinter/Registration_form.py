from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Registration Form")


def printt():
    print("Welcome to Tkinter")


def exit1():
    exit()


label1 = Label(window, text="Registration Form", relief="solid", width=20, font=("arial", 19, "bold"))
label1.place(x=90, y=53)
label2 = Label(window, text="First Name", width=20, font=("arial", 10, "bold"))
label2.place(x=80, y=130)
label3 = Label(window, text="Last Name", width=20, font=("arial", 10, "bold"))
label3.place(x=80, y=180)

b1 = Button(window, text="Login", width=12, bg='brown', fg='white', command=printt)
b1.place(x=150, y=380)
b2 = Button(window, text="Quit", width=12, bg='brown', fg='white', command=exit1)
b2.place(x=280, y=380)
window.mainloop()
