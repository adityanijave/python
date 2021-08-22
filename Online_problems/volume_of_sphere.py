# 15. Write a Python program to get the volume of a sphere with radius 6.
# Click me to see the sample solution

from math import pi
radius = int(input("enter the radius of sphere : "))
calculating_volume_of_sphere = (4/3)*pi*(radius**3)
print(f"Volume of sphere of radius {radius} is {calculating_volume_of_sphere} unit^3")