#problem :
'''
checking where given number is armstrong number is or not :
'''

#soln:

number = int(input("Enter the number :\n"))
a = number // 100
b = number  % 100
c  = b // 10
d = b % 10
e = (a**2)+(c**2)+(d**2)
if number == a :
    print("Given number is an ARMSTRONG NUMBER")
else :
    pass