# Write a Python program to flatten a shallow list.
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# output
# [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
requird_list = []
d = ""
for sublist in original_list:
    for element in sublist:
        d = d+str(element)
for i in d :
            ddd = requird_list.append(i)

print(requird_list)
