class operations:
    def __init__(self,x = 0,y = 0 ):
        self.a = x
        self.b = y
        print(f"The default values of a and  b are {self.a}  and {self.b} respectively ")

    def addition(self):
        print(f"The values of addition for {self.a} and {self.b} is {self.a+self.b}")

    def subtraction(self):
        print(f"THe values of subtraction for {self.a} amd {self.b} is {self.a-self.b}")

# objectname =classname()
for_obj1 = operations()
for_obj1.addition()

for_obj2 = operations(x=1,y=2)
for_obj2.subtraction()