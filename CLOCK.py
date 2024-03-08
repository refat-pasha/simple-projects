from tkinter import *
from time import *

#basic clock
def update():
    time_string = strftime("%I:%M:%S %p")
    time_lable.config(text=time_string)

    day_string = strftime("%A")
    day_lable.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_lable.config(text=date_string)

    window.after(1000,update)



window = Tk()
time_lable = Label(window,font = ("Ink Free",25 ))
time_lable.pack()

day_lable = Label(window,font = ("Ink Free",35 ),fg="white",bg="black")
#the day i program this was friday so i make the background black and font color white
day_lable.pack()

date_lable = Label(window,font = ("Ink Free",30 ))
date_lable.pack()

update()
window.mainloop()









