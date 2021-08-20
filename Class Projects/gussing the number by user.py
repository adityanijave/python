import random
c = 1
while True:
    computer = random.randint(0, 10)
    user = int(input("enter your guessed number from 0 to 10 : "))

    if computer == user :
        print(f"congo! \nComputer choose number : {computer} \nyou guess the number : {user}")
        break
    else :
        print(f"try again \nComputer choose number : {computer} \nyou guess the number : {user}")
        c+=1
print(f"Total try is {c}")
