mylist = [1,2,90,23,55,89]
mylistmax = mylist[0]
for number in mylist:
    if number<mylistmax:
        mylistmax = number
print(f"The max number in a list is {mylistmax}")