#use of open read readline function : with demo1.txt

# demo_file = open("demo1.txt","r")
# read_demo_file = demo_file.read()
# print(read_demo_file)
# demo_file.close()


# demo_file = open("demo.txt")
# read_demo_file = demo_file.read()
# print(read_demo_file)
# demo_file.close()


# i =int (input("enter :\n"))
# demo_file = open("demo.txt")
# read_demo_file = demo_file.read(i)
# print(read_demo_file)
# demo_file.close()



demo_file = open("demo.txt")
read_demo_file = demo_file.readline()    #1st line
print(read_demo_file)
read_demo_file = demo_file.readline()    #2nd line
print(read_demo_file)
demo_file.close()






