class Bikeshop:
    def __init__(self, stock):
        self.stock = stock
    def displaybike(self):
        print("Total bikes",self.stock)
    def rentforbike(self,q):
        if q<=0:
            print("Enter the positive value or greater than zero")
        elif q>self.stock:
            print("Enter the value less than stock under 100")
        else:
            self.stock = self.stock-q
            print("Total bikes",self.stock)


while True:
    obj=Bikeshop(100)
    uc=int(input('''
    1. Display
    2. Rent a Bike
    3. Exit
                    '''))
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("Enter the Quantity"))
        obj.rentforbike(n)
    else:
        break
