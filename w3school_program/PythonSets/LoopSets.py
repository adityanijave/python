requiredSet = {1, 3, 5, "Adi", "Ruhi", True, False}

requiredIntlist = []
requiredStrlist = []
requiredBoollist = []
requiredUnidentifeditemList = []

for i in requiredSet:
    if type(i) == int:
        requiredIntlist.append(i)
    elif type(i) == str:
        requiredStrlist.append(i)
    elif type(i) == bool:
        requiredBoollist.append(i)
    else:
        requiredUnidentifeditemList.append(i)

print(requiredIntlist)
print(requiredStrlist)
print(requiredBoollist)
print(requiredUnidentifeditemList)
