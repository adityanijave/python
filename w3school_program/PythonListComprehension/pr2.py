List = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = [x for x in List if (len(x)/2 != 0)]
print(newList)