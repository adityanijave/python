
# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi
def area_of_circle(radius):
    print(f"Area of Circle having radius {radius} is {pi*radius*radius}")
radius = float(input("Enter the radius of circle: "))
area_of_circle(radius)