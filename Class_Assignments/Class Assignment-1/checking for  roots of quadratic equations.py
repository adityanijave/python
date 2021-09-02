a = float(input("enter the coff. of X^2 :\n"))
b = float(input("enyer the coff. of X :\n"))
c = float(input("enter the coff. of constant :\n"))

print("\nequation is form as : " + str(a)+"X^2"+str(b)+"X"+str(c)+" = 0")

if a == 0 :
    print("\nquadrtic equation is not valid ")
    print("coff. of X^2 is ""zero""")
    
else:
    print("\nvalue of X1 is : ", -(((b)+((b**2)-(4*a*c))**(0.5))/(2*a)))
    print("vlaue of X2 is : ", -(((b)-((b**2)-(4*a*c))**(0.5))/(2*a)))