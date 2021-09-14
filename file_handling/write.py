file1 = open("text2.txt","r")
reading_data_of_file = file1.read()

file2 = open("text3_for_copy_file_using_write_mode","w")
file2.write(reading_data_of_file)

file1.close()
file2.close()