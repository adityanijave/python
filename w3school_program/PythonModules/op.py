import calculater
user = input("enter operator +,-,* :")
n1 = int(input("enter number 1 : "))
n2 = int(input("enter number 2 : "))

if user == "+":
    print(calculater.add(n1, n2))
elif user == "-":
    print(calculater.sub(n1, n2))
elif user == "*":
    print(calculater.multi(n1, n2))
