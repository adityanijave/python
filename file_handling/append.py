file1 = open("text2.txt","r")
reading =  file1.read()

file2 = open("text4_for_appending_some_data","a")
file2.write(reading)

file2.close()
file1.close()