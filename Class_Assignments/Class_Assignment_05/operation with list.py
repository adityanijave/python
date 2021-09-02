# write a programme to count the number of string where the string length is two or more
c =0
list = ["a","abc","aba","1221"]
for x in list:
    if len(x) >=2:
        c +=1
print(c)