# gamescore by using read write def if elif : with  gamescore.txt
    

user_score = (input("Enter your score in Game  :\n"))
def game():
    return user_score
with open("gamescore.txt") as reading_gamescore :
    reading_gamescore =reading_gamescore.read()
if user_score =="":
    with open("gamescore","w") as writing_updated_gamescore:
        print("hight gamescore is :",reading_gamescore)
elif int(user_score) > int(reading_gamescore):
    with open("gamescore.txt","w") as new_gamescore :
        new_gamescore = new_gamescore.write(user_score)
        print("new high score is updated :",user_score)
elif int(user_score) <int(reading_gamescore):
        print("last high score is better than  :",user_score)
        print("high score is :",reading_gamescore)





























