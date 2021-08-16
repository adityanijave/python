#problem :
'''a file contains a word "Donkey" multiple times. 
you need to write a program which repalces this
wprd with "######" by updating the same file'''




#sol :

with open("donkey.txt","r") as file_of_donkey :
    file_of_donkey_reading = file_of_donkey.read().lower()
    if "donkey" in file_of_donkey_reading :
        repacling_word = file_of_donkey_reading.replace("donkey", "#######")   
with open("donkey.txt","w") as file_of_donkey :
    file_of_donkey_reading = file_of_donkey.write(repacling_word)

        