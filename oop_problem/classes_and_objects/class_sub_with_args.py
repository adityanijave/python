class subtractions:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(f"values are stored as a = {self.a} and b = {self.b}.")

    def subtraction(self):
        print(f"The subtraction is {self.a} amd {self.b} is {self.a-self.b}.")

# objectname = classname()
operation = subtractions(200,20)
operation.subtraction()


