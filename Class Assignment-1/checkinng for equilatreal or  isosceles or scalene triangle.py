angle1 = int(input("enter angle :\n"))
angle2 = int(input("enter angle :\n"))
angle3 = int(input("enter angle :\n"))
if angle1 == angle2 == angle3 :
    print("equilatreal triangle !")
elif  (angle1  == 90) or (angle2 == 90) or (angle3 == 90) :
    print("isosceles triangle!")
elif  angle1 != angle2 != angle3 :
    print("scalene triangle !")