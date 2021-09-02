#problem :
''' create a python program to print the sum of all even number from 1 to n by using for loop  '''

#soln:

n = int(input("Enter the number : "))
evensum = 0
for i in range(2*n,1,-2):
    evensum += i
    print(i)
print("evensum : ",evensum)