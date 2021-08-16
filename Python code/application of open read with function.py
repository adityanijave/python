# application of open read with function : with poem.txt



# poem = open("poem.txt","r")
# reading_poem = poem.read().lower()
# if "twinkle" in reading_poem :
#     print("It is there !")
# else :
#     print("not there!")
# poem.close()



with open("poem.txt") as reading_poem :
    reading_poem = reading_poem.read().lower()
    if "twinkle" in reading_poem :
        print("It is there !")
    else :
        print("not there!")