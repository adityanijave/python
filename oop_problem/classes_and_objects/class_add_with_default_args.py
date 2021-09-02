class operations:
    def __init__(self,x=0,y=0):
        self.y = y
        self.x = x
        print(f"The values are stored x and y as {self.x} ,{self.y} respectively")

    def addition(self):
        print(f"The addition of {self.x } and {self.y} is {self.x + self.y}")

    def subtraction(self):
        print(f"The value of subtraction of {self.x} amd {self.y} is {self.x - self.y}")

# objectname = classname()
ops = operations()
ops.addition()
ops.subtraction()