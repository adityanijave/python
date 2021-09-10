# statement :
'''
Write a class calculator capable of finding square, cube, square root and cube root of number.
'''


# code :
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The Square of {self.number} is {self.number ** 2}")

    def squareRoot(self):
        print(f"The Square Root of {self.number} is {self.number ** 0.5}")

    def cube(self):
        print(F"The Cube of {self.number} is {self.number ** 3}")

    def cubeRoot(self):
        print(f"The Cube Root of {self.number} is {self.number ** (1 / 3)}")


number1 = Calculator(8)
number1.square()
number1.squareRoot()
number1.cube()
number1.cubeRoot()
