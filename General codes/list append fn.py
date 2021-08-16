#list.append


l = [1,2,3,4,5,6,7,8,9,0]
print("list l is :",l)

l.append(10)
print("updated list = ",l)



m = int(input(("enter number : ")))
l.append(m)
print("updated list = ",l,"\n")


ll = [10,20]
l.append(ll)
print("list within list : ",l)



lz = [1,2,3,4,5,6,7,8,9,0,[10,20]]
print("getting value from nested list :", lz[10][1])