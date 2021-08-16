#problem :
'''create a python program to find armstrong number form 1 to n'''

#soln:
n = int(input("enter the number :"))
a = 100
while a < n :
    b = a // 100
    c = a % 100
    d = c // 10
    e = c % 10
    f = b**3+d**3+e**3

    if a == f:
        print(a)
    a = a + 1


