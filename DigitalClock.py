from tkinter import *
import time

def updateClock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + am_or_pm
    label.config(text=time_text)
    root.after(1000, updateClock)  #1000 in milliseconds

root = Tk()
root.title("Digital Clock")
# root.geometry("600x600")
root.config(bg='red')
label = Label(root, text='00:00:00', font="Helvetica 32 bold" )
# label.place(x= 140, y=140, height=40, width=200)
# label.config()
label.pack() #THIS FUNCTION AUTOMATICALLY SET THE WINDOW SIZE ACCORDING TO THE TEXT SIZE
updateClock()



# Label.place(x)
root.mainloop()