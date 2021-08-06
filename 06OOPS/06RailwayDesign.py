# fareInfo
# bookTicket
# cancelTicket
# getStatus

'''1 2 3 4 5'''

class Train:
    def __init__(self,name,fare,seats):
        self.tname=name
        self.tfare=fare
        self.tseats=seats
        self.nseats=list(range(1,seats+1))

    
    def getStatus(self):
        print("******STATUS*****")
        print(f"The name of train is: {self.tname}")
        print(f"Total seats: {self.tseats}")
        print(f"Seats available: {self.nseats}")
        print("**********************")
    
    def fareInfo(self):
        print(f"Price of one ticket is :{self.tfare}")
    
    def bookTicket(self):
        if len(self.nseats)>0:
            ticket=self.nseats.pop(0)
            return ticket
        else:
            print(f"No seat available")

    def cancelTicket(self,ticketNo):
        if ticketNo>self.tseats:
            print("Enter a valid seat no")
        else:
            if ticketNo not in self.nseats:
                self.nseats.append(ticketNo)
                print("Ticket cancelled successfully")
            else:
                print("Enter a valid ticket number")


t1=Train('Rajdhani Express',45,5)
t1.getStatus()
t1.fareInfo()

print(t1.bookTicket())
print(t1.bookTicket())
t1.getStatus()
t1.cancelTicket(1)
t1.getStatus()