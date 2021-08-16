#game:
import random
def game_play():
    if  user_turn == computer_turn :
        print("\nMatch draw!")
    if user_turn == "r" and computer_turn == "p":
        print("\nYou Win!")   
    if user_turn == "r" and computer_turn == "s":
        print("\nYou Win!")
    if user_turn =="p" and computer_turn == "r":
        print("\nYou Win!")
    if user_turn =="p" and computer_turn == "s":
        print("\nYou lose!")
    if user_turn =="s" and computer_turn == "r":
        print("\nYou lose!")
    if user_turn =="s" and computer_turn == "p":
        print("\nYou Win!")
    print("\ncomputer choose :"+str(computer_turn))
    print("user choose     :"+str(user_turn))
    print("Thanks for playing with Computer :)")        
def rules_of_game():
    return '''Rules Of The Game Are :
\nFor Rock  enter         : r
For Paper enter         : p
For Scissors enter      : s '''
print("\nLet's Play!\n")
print(rules_of_game())
computer = random.randint(1, 3)
if computer == 1:
    computer_turn = "r"
elif computer == 2:
    computer_turn = "p"
elif computer == 3:
    computer_turn = "s"
print("\ncomputer's turn is going on , please wait a moment till computer response!")
print("Computer responded !")
print("\nNow,",end="")
user_turn  = str( input("Enter you response :\n"))
game_play()






















