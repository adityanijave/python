class operations:
    def __init__(self, a=0, b=0):
        self.a = int(input("enter number 1 : "))
        self.b = int(input("enter number 2 : "))
        print(f"\nValues are stored in a and b as {self.a} and {self.b} respectively")

    def addition(self):
        print(f"\nThe addition of given value {self.a} and {self.b} is {self.a + self.b}")

    def subtraction(self):
        print(f"\nThe subtraction of given value {self.a} and {self.b} is {self.a - self.b}")

    def multiplication(self):
        print(f"\nThe multiplication of given value {self.a} and {self.b} is {self.a * self.b}")


user_want = input("Enter sign to perform operations like +,-,* : ")

# onjectname = classname()
operation = operations()

if user_want == "+":
    operation.addition()

if user_want == "-":
    operation.subtraction()

if user_want == "*":
    operation.multiplication()
