# using .copy (built-in function) to copy which does not take any changes form main list once we copy it .........

# copying list
list1 = ["a", "b", "c", "d", "x"]
# print(list1)
list2 = list1.copy()
list2.append("z")

list1.append("aditya")
print(list1)
print(list2)