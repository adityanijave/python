import random
computer = random.randint(0, 10)

while True:
    user = int(input("enter your number : "))
    if computer == user :
        print("s")
    else :
        print("d")