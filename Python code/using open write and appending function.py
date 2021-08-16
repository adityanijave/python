#using open write and appending function : with demo2.txt



demo1_file = open("demo2.txt","w")
demo1_file.write("this is nice  !")
demo1_file.write("this is not nice  !")
print(demo1_file)
demo1_file.close()




# demo1_file = open("demo2.txt","a")
# demo1_file.write("\ngood very good")
# print(demo1_file)
# demo1_file.close()