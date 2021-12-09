import random

elements = [3, 2, 5]
length_of_elements = len(elements)
print(f"Length of elements is {length_of_elements}")
factorial = 1
for i in range(length_of_elements, 1,-1):
    factorial *= i
print(f"The value of {length_of_elements}! is {factorial}")

