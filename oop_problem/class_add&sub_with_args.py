class operations:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(f"The values of a and b are stored as {self.a} and {self.b} respectively")
    def addition(self):
        print(f"The addition of {self.a} and {self.b} is {self.a + self.b}")
    def subtraction(self):
        print(f"The subtraction of {self.a } amd {self.b} is {self.a - self.b}")

# objectname = classname()
operations = operations(20,10)
operations.addition()
operations.subtraction()

