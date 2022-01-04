class Data:
    def __init__(self):
        self.fn = input("enter first name : ")
        self.ln = input("enter surname : ")
        self.ci = input("enter city name : ")
        self.st = input("enter state name : ")
        self.co = input("enter country name : ")
        print("init function called successfully")

    def callingEverthing(self):
        print(f"full name = {self.fn + ' '+ self.ln} from {self.ci +  self.st +  self.co}")


case1 = Data()
case1.callingEverthing()
