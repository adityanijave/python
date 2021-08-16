#problem:
'''creat one file then make it's copy file in txt mode'''

#slon:

with open("main.txt") as main :
    read_main = main.read()
with open("copy of main","w") as copy_main:
    copying = copy_main.write(read_main)
    print(copy_main)
    print(copying)