# Write a Python program to find common items from two lists.

required_list1 = [1,2,3,4,5,6]
required_list2 = [5,6,7,8,9,0]
required_set1 = set(required_list1)
required_set2 = set(required_list2)

print(f'The common object in both list which are {required_list1} & {required_list2} is {required_set1.intersection(required_set2)}')