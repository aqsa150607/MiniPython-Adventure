import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Countdown Timer")
root.geometry("800x800")
root.configure(bg="lightblue")
f = ("Times Roman", 10, "bold")


def countdown(n):
    if n < 0:
        return
    lab_msg.config(text=n)
    root.after(1000, lambda: countdown(n - 1))


def display():
    try:
        start = int(ent_num.get())
        countdown(start)
    except Exception as e:
        lab_msg.config(text=f"Issue is → {e}")


def on_stop():
    result = messagebox.askyesno("Confirm", "Do you really want to stop :( ? ")
    if result:
        root.destroy()


def on_closing():
    result = messagebox.askokcancel("Quit", "Are You sure to QUIT 😒: ")
    if result:
        root.destroy()


Lab1 = Label(root, text="Enter the Number to start Countdown From:", font=f)
ent_num = Entry(root, background="pink", font=f)
ok_but = Button(root, text="Display", bg="green", command=display)
stop_but = Button(root, text="Stop", bg="red", command=on_stop)
closing_butt = Button(root, text="Close Window ", command=on_closing)
lab_msg = Label(root, font=("Times New Roman", 20, "bold"), bg="lightblue")

Lab1.place(x=50, y=100)
ent_num.place(x=350, y=100)
ok_but.place(x=50, y=200)
stop_but.place(x=150, y=200)
lab_msg.place(x=50, y=250)
closing_butt.place(x=50, y=350)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
