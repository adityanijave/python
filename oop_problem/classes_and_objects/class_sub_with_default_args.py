class subtraction:
    def __init__(self,x=0,y=0):
        self.a = x
        self.b = y
        print(f"Default values are stored {self.a} and {self.b} for a and b respectively")

    def sub(self):
        print(f"The values of subtraction of {self.a } and {self.b} is {self.a -self.b}")

# objectname = classname()
case = subtraction()
case.sub()
