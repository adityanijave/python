# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

sample_list = [11, 33, 50]
required_string = ""

for i in sample_list :
    k = str(i)
    for j in k :
        required_string += j

converting_str_to_int = int(required_string)
print(converting_str_to_int)