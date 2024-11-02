class bike_shop:
    def __init__(self,stock):
        self.stock = stock

    def rentForBike(self,quantity):
        if quantity <=0:
            print(f"Enter the positive value or greater than zero!")
        elif quantity> self.stock:
            print(f"Enter the value(less than stock)")
        else:
            self.stock = self.stock - quantity
            print(f"Total Prices : {quantity*100}")
            print(f"Total Bikes : {self.stock}")

    def displayBike(self):
        print(f"Total Bikes available  : {self.stock}")


obj = bike_shop(100)
while True:

    user_choice = int(input('''
        1. Rent a Bike 
        2. Display Stocks
        3. Exit
    '''))
    if user_choice == 1:
        n = int(input("Enter quantity:------"))
        obj.rentForBike(n)

    elif user_choice == 2:
        obj.displayBike()

    else:
        break
