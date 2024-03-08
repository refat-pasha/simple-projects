from tkinter import *
from time import *

#basic clock
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

def on_resize(event):
    # Update font size based on window width
    font_size = max(50, int(event.width / 10))
    time_label.config(font=("Ink Free", font_size))



window = Tk()
window.geometry("400x300")
window.title('CLOCK')

time_label = Label(window,font = ("Ink Free",25 ))
#time_label.pack(anchor='w')
time_label.pack(expand=True, fill="both")

day_label = Label(window,font = ("Ink Free",35 ),fg="white",bg="black")
#the day i program this was friday so i make the background black and font color white
day_label.pack(anchor='e')

date_label = Label(window,font = ("Ink Free",30 ))
date_label.pack(anchor='e')


window.bind("<Configure>", on_resize)


update()
window.mainloop()









