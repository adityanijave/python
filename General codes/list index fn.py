#list.index:
    
l = [1,2,3,4,5,6,7,8,9,0,11]
print("list is : ",l,"\n")
    
    
print("=========== getting index============")
print("index of 11 is :",l.index(11),"\n")

print("=========== removing element at given index ============")
l.pop(10)
print("list after removing element at given index : ",l,"\n")

print("=========== removing  element from list ============")
l.remove(0)
print("list after removing '0' element from list l :",l,"\n")

print("=========== adding  element in list ============")
l.append(10)
print("after adding element in lsit : ",l ,"\n")

print("=========== adding  element in list at given index ============")
l.insert(0,0)
print("list after adding element at given index :",l)