# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and
# a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

sample_data = input("enter data :")
updated_data = sample_data.split(",")
print(f"List : {updated_data}\nTuple : {tuple(updated_data)}")











