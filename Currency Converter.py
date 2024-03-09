#using CurrencyConverter lib
#from currency_converter import CurrencyConverter
#using forex-python lib
from forex_python.converter import CurrencyRates
import tkinter as tk

#a= CurrencyConverter()
a= CurrencyRates()
window = tk.Tk()
window.title("Currency Converter")
window.geometry("450x350")

def convert():
    amount = float(entry_1.get())
    currency_1 = entry_2.get().upper()
    currency_2 = entry_3.get().upper()
    #using CurrencyConverter lib
    #data = a.convert(amount,currency_1,currency_2)
    #using forex-python lib
    data = a.convert(currency_1,currency_2,amount)
    lebel_5 = tk.Label(window,text=f"converted currency is: {data:.02f}",font=("Roboto",15)).place(x=100,y=250)



label_1 = tk.Label(window, text="Currency Converter", font =("Ink Free",24),fg="black").pack(side=tk.TOP)
label_2 = tk.Label(window,text="enter ammount hare: ",font =("Roboto bold",11),fg="black").place(x=10,y=45)
entry_1 = tk.Entry(window)
lebel_3 = tk.Label(window, text="enter currency: ",font =("Roboto bold",11),fg="black").place(x=10,y=85)
entry_2 = tk.Entry(window)
lebel_4 = tk.Label(window, text="enter req currency: ",font =("Roboto bold",11),fg="black").place(x=10,y=120)
entry_3 = tk.Entry(window)

button = tk.Button(window, text="convert",font=("Roboto",15),command=convert).place(x=150,y = 200 )
entry_1.place(x= 200, y=50)
entry_2.place(x= 200, y=90)
entry_3.place(x= 200, y=125)




window.mainloop()




#a = CurrencyConverter
