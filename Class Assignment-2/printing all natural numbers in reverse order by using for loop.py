#problem :
'''      Create a python program to print all natural numbers in reverse order by using for  loop '''

#soln:
    
number = int(input("Enter the last number of natural number :"))

for _ in range(number,0,-1):
    print(_)