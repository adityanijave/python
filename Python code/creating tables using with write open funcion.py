# creating tables using with write open funcion:


# for i in range(1,6):
#     opening_file = open("tables"+str(i)+".txt","w")
#     for j in range(1,11):
#         tables = opening_file.write(str(i)+"X"+str(j)+"="+str(i*j)+"\n")
#     opening_file.close()




######################              another way                   #######################



for i in range(1,6):
    with open("table"+str(i)+".txt","w") as table:
            table.write("this text is result of , creating tables using with write open funcion\n\n")
for i in range(1,6):
    with open("table"+str(i)+".txt","a") as table:
            for j in range(1,11):
                table.write(str(i)+"X"+str(j)+"="+str(i*j)+"\n")
       