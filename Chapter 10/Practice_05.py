class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getStatus(self):
        print("*****")
        print(f"The name of the train is {self.name}")
        print(f"The number of seats availble are {self.name}")
        print("*****")
    
    def fareInfo(self):
        print(f"The price of the ticket is Rs {self.fare}")
        
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, this train is already full! Better luck next time!")
    def cancelTicket(self):
        self.seats = self.seats + 1   
        
intercity = Train("Intercity Expresss : 104005", 90, 2)

intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.cancelTicket()
intercity.bookTicket()
intercity.getStatus()
