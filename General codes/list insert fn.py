#list.insert

l = [1,2,3,4]
print("list l is : " ,l,"\n")

l.insert(0, 0)
print("updated list l is :",l,"\n")

i = int(input("enter index : "))
j = int(input("enter object : "))
l.insert(i, j)
print("updated list l is :",l)