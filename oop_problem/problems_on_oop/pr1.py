# statement :
'''
create a class programmer for storing information of few programmers working at microsoft
'''

# code :
class Programmers :
    com = "MICRO-SOFT"
    def __init__(self, name, department, product):    #constracter
        self.name = name
        self.department = department
        self.product = product

    def programmerInformation(self):
        print(f"Name of company is {self.com}."
              f"\nThe name of programmer is {self.name}."
              f"\nHis/Her Department is {self.department}."
              f"\nHis/Her working on {self.product} product.")

p1 = Programmers("Aditya", "Electrical", "Electric Bike")
p2 = Programmers("Rohini", "Electrical", "Electric Car")
p3 = Programmers("Akash", "Computer", "Data Science")

p1.programmerInformation()
p2.programmerInformation()
p3.programmerInformation()
