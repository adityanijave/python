a = int(input("enter the number : "))
c = 0
while a> 0 :
    b = a % 10
    c = c + b
    a = a//10
print(c)