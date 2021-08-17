from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

label1 = Label(window, text="Welcome to Tkinter", fg='black', bg='grey', relief="solid", font=("algerian", 12, "bold"))
# label1.place(x=80, y=130)
label1.pack(fill=BOTH, pady=2, padx=2)
#label1.pack()
button1 = Button(window, text="Hello", fg='white', bg='black', relief=RIDGE, font=("algerian", 12, "bold"))
button1.place(x=120, y=130)       # Relief options : GROOVE, RIDGE, SUNKEN, RAISED
window.mainloop()