with open("text2.txt","r") as fp:
    reading_data_of_file = fp.read()

with open("text3_for_copy_file_using_write_mode","w") as fp:
    fp.write(reading_data_of_file)
