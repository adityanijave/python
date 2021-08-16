#list.copy

l = [10,20 ,30]
m = l.copy()

print("list l is ",l)
print("list m is ",m,"\n")


print("id of list l is :",id(l))
print("id of list m is :",id(m),"\n")


print("item in both list is same" if l == m else "item in both list is different")
print("mem loction of both list is same" if id(l)==id(m) else "mem loction of both list is different")