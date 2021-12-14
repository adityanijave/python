a = {"apple", "banana", "cherry"}
print(a)
print(len(a))
print()
a.add("orange")
print(a)
print(len(a))
print()
b = ("aapple", "bbanana", "ccherry")
a.update(b)
print(a)
print(len(a))
print()


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
print(type(thisset))
print(type(mylist))
print(len(thisset))