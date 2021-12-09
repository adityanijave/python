n = int(input("enter the (N) : "))
r = int(input("enter the (R) : "))
c = 0
for i in range(1,r+1) :
    while n != 0:
        c += 1
        n -= r
        if n < 0:
            break
print(c)