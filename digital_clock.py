import tkinter
from tkinter import *
from time import strftime
window=tkinter.Tk()
window.title("Digital Clock")
window.configure(bg="black")
window.geometry("600x200")
clock=Label(window,font="sans-serif 44 bold",fg="yellow",bg="black")
clock.pack(anchor='ne',expand="yes",fill="both")
#expand="yes" means that we can resize the gui window bothwise i.e verticall,horizontally and diagonally
#fill="both" means that when we expand the window size then it fills the background both vertically and horizontally with color

def time():
    string=strftime("%H:%M:%S %p")    #it gives a string format of type HOURS:MINUTES:SECONDS AM/PM
    clock.config(text=string)
    clock.after(10,time) #gives a delay of 10 milisec i.e to change the value of seconds after every 10 ms
time()
window.mainloop()

