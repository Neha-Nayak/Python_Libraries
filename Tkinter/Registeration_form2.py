# importing libraries
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

fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()

def exit1():
    exit()

# Labels and Entry widgets
label0 = Label(window, text="Registration Form", relief="solid", width=20, font=("arial", 19, "bold"))
label0.place(x=90, y=120)

label1 = Label(window, text="First Name", width=20, font=("arial", 10, "bold"))
label1.place(x=80, y=200)

entry_1 = Entry(window, textvar=fn)
entry_1.place(x=210, y=200)

label2 = Label(window, text="Last Name", width=20, font=("arial", 10, "bold"))
label2.place(x=80, y=260)

entry_2 = Entry(window, textvar=ln)
entry_2.place(x=210, y=260)

label3 = Label(window, text="DOB", width=20, font=("arial", 10, "bold"))
label3.place(x=80, y=320)

entry_3 = Entry(window, textvar=dob)
entry_3.place(x=210, y=320)

label4 = Label(window, text="College", width=20, font=("arial", 10, "bold"))
label4.place(x=80, y=380)

# ComboBox with a drop-down list
list1 = ['JIT', 'JSS', 'RV', 'BMS', 'RNS', 'DSU', 'CU', 'BNM']
droplist = OptionMenu(window, var, *list1)
var.set("Select College")
droplist.config(width=15)
droplist.place(x=210, y=380)

# Buttons
b1 = Button(window, text="Login", width=12, bg='brown', fg='white', command=printt)
b1.place(x=150, y=440)
b2 = Button(window, text="Quit", width=12, bg='brown', fg='white', command=exit1)
b2.place(x=280, y=440)

window.mainloop()
