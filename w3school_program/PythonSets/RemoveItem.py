set1 = {"apple", "banana", "cherry", "adi", "ruhi", "sam"}

set1.remove("cherry")
print(set1)
# set1.remove("yash")                                    #remove gives an error if item not present in the set
# print(set1)

set1.discard("sam")
print(set1)
set1.discard("gopal")  # discard will not give you error even item is not present in the set
print(set1)


set1.pop()
print(set1)

set1.clear()
print(set1)

del set1
print(set1)