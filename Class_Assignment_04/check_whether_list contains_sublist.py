# Write a Python program to check whether a list contains a sublist.


# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
original_list = [1,3,4,5,6,7]
# original_list = [1,2,4,5,6,[1,2,3,4,5,6,7,8,9,0]]


required_set = set()
for i in original_list:
    if type(i) is list :
        required_set.add("yes it's having sublist")
if "yes it's having sublist" in required_set:
    print(f'Given list containing sublist init {original_list}')
else:
    print(f"Given list doesn't containing sublist init {original_list}")