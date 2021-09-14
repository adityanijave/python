'''
to read length of data inside the "text.txt" file
'''

file = open("text.txt","r")
reading_file_data_length = len(file.read())
print(reading_file_data_length)
file.close()
file = open("text.txt","r")
file.close()