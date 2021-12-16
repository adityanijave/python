    
physics =int( input(" enter the marks of physics : \n"))
chemistry = int(input(" enter the marks of chemistry : \n"))
biology =int( input(" enter the marks of biology : \n"))
mathematics =int (input(" enter the marks of mathematics : \n"))
computer =int (input(" enter the marks of computer : \n"))
percentage = (physics+ chemistry+ biology + mathematics + computer )/5
if percentage >= 90 :
    print("class A")
elif percentage >=80 : 
    print(" class B")
elif  percentage >=70 : 
    print("class C")
elif percentage >= 60 :
    print("class D")
elif percentage >= 40 :
    print("class E")
elif percentage <40 :
    print("class F")