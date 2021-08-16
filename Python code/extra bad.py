#problem :
''' a txt file is contining multiple bad words which is given below in form if list , 
you have to detect the bad words and replace them by "##$$##" and update the same file .

list_of_bad_words = ["pagal", "yeda", "animal" ,"donkey"]'''



#soln:
bad_words = ["pagal", "yeda", "animal" ,"donkey"]

with open("extra bad.txt") as bad_words_file :
    para = bad_words_file.read() 
for words in bad_words:
    para = para.replace(words, "##$$##")
with open("extra bad.txt","w") as bad_words_file :
    bad_words_file.write(para)