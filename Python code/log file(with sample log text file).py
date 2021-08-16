#problem :
''' write a program that mining a log fille and find 
    "python" word is present in that or not and also find on which 
    lin is it
'''

#soln:
con = True
i = 1
with open("sample log.txt") as file :
    while con:
        con = file.readline().lower()
        if "python" in con:
            print("its is there ! ")
            print("on line no is :",i,"\n")
        i = i+1