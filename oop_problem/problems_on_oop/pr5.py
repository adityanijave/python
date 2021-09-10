# statement :
'''
Write a class train, which has method to book a ticket, get status(no. og seats) and get fare information of
trains running under indian railways
'''

# code :
class Train:
    def __init__(self, name , fare ,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def showStatus(self):
        print(f"Name of train is ''{self.name}''"
              f"\nFare is ''{self.fare}''"
              f"\ntotal seats in ''{self.name}'' is ''{self.seats}''")


traintype = Train("top1 : 1234",99,300)
traintype.showStatus()