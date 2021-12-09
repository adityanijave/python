import random
c = 1
while True:
    computer = random.randint(0, 10)

    user = (input("enter your guessed number from 0 to 10 : "))
    if user.isdigit():
        if computer == int(user) :
            print(f"congo! you won \nComputer choose number : {computer} \nyou guess the number : {user}")
            break
        elif computer != int(user) :
            print(f"you lose, try again \nComputer choose number : {computer} \nyou guess the number : {user}\n")
            c+=1
    else:
        print('please enter valid entry!\n')
print(f"Total try is {c}"