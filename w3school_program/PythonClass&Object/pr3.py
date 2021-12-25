class Lab:
    def __init__(self, Date, Section, Total, Active):
        self.Date, self.Section, self.Total, self.Active = Date, Section, Total, Active

    def callingDate(self):
        print(f"Date : {self.Date}")

    def callingSection(self):
        print(f"Section Name : {self.Section}")

    def callingPerformance(self):
        print(f"Total No Of Student In The {self.Section} : {self.Total}"
              f" From Them Active Student Are : {self.Active}"
              f" And Unactive Student Are : {self.Total - self.Active}")


user = int(input("Enter Number : "))
for i in range(0, user):
        Date, Section = input("Enter Today's Date : "), input("Enter Name Of Section : ")
        Total, Active = int(input("Enter Total No Of Student In Section : ")), int(input("Enter No Of Student Are "
                                                                                         "Active : "))
        case1 = Lab(Date, Section, Total, Active)
#                                              calling function
        case1.callingDate()
        case1.callingSection()
        case1.callingPerformance()
