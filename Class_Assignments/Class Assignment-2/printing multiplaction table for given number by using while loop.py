# problem :
''' create a python program to print multiplaction table for given number by using while loop'''

# soln:

number = int(input("Enter the number for table :"))
i = 1

while i < 11 :
    print(str(number)+"X"+str(i)+"="+str(number*i))
    i = i +1