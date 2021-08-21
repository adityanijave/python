#
# 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

sample_file_name = input("Enter the file name : ")
finding_index = sample_file_name.index(".") + 1
extension = sample_file_name[finding_index:]
print(extension)