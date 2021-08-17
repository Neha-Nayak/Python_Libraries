# importing libraries
import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
# initialisation
window = Tk()
window.geometry("500x500")
window.title("Registration Form")

# icon image
img = Image.open('D:\Coders_ club\Python_\Tkinter\icon.png')
re_img = img.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(re_img)

lab = Label(image=photo)
lab.place(x=190, y=10)

# function
def printt():
    first = fn.get()
    sec = ln.get()
    dob1 = dob.get()
    var1 = var.get()
    print(f"Your Full Name is {first} {sec}")
    print(f"Your Date Of Birth is {dob1}")
    print(f"You study in {var1}")
def exit1():
    exit()

def abt():
    tkinter.messagebox.showinfo("Welcome", "this is a demo")
fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()
def second_win():
    window2=Tk()
    window2.geometry('250x200')
    label_2 = Label(window2, text="Registration completed", relief='solid', font=("arial",'12','bold'))
    label_2.place(x=30, y=70)
    b_2 = Button(window2, text="OK", width=12, bg='brown', fg='white', command=exit1)
    b_2.place(x=80, y=110)
# Menu
menu = Menu(window)
window.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label='Exit', command=exit1)
subm2 = Menu(menu)
menu.add_cascade(label="Options", menu=subm2)
subm2.add_command(label='About', command=abt)
# Labels and Entry widgets
label0 = Label(window, text="Registration Form", relief="solid", width=20, font=("arial", 19, "bold"))
label0.place(x=90, y=120)

label1 = Label(window, text="First Name", width=20, font=("arial", 10, "bold"))
label1.place(x=80, y=200)

entry_1 = Entry(window, textvar=fn)
entry_1.place(x=210, y=200)

label2 = Label(window, text="Last Name", width=20, font=("arial", 10, "bold"))
label2.place(x=80, y=240)

entry_2 = Entry(window, textvar=ln)
entry_2.place(x=210, y=240)

label3 = Label(window, text="DOB", width=20, font=("arial", 10, "bold"))
label3.place(x=80, y=280)

entry_3 = Entry(window, textvar=dob)
entry_3.place(x=210, y=280)

label4 = Label(window, text="College", width=20, font=("arial", 10, "bold"))
label4.place(x=80, y=320)

# ComboBox with a drop-down list
list1 = ['JIT', 'JSS', 'RV', 'BMS', 'RNS', 'DSU', 'CU', 'BNM']
droplist = OptionMenu(window, var, *list1)
var.set("Select College")
droplist.config(width=15)
droplist.place(x=210, y=320)

# Buttons
b1 = Button(window, text="Login", width=12, bg='brown', fg='white', command=printt)
b1.place(x=150, y=380)
b2 = Button(window, text="Quit", width=12, bg='brown', fg='white', command=exit1)
b2.place(x=280, y=380)
b3 = Button(window, text="GOTO", width=12, bg='brown', fg='white', command=second_win)
b3.place(x=220, y=420)

window.mainloop()
