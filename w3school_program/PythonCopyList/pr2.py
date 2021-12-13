# using 'assignment (=) operator which also copying the all changes.......from main list

# copying list
list1 = ["a", "b", "c", "d", "x"]
list2 = list1
list2.append("z")
# print(list2)
list1.append("abracadabra")
print(list1)
print(list2)
