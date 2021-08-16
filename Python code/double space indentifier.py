# double space indentifier 

# str = input("enter para : \n")
# if "  " in str : 
#     print(" it's contain double space")
# else :
#     print("it does not contain double space")




######################              another way                   #######################

# str = input("enter para : \n").find("  ")
# # str.find("  ")
# print("its is there")

######################              another way                   #######################

str = input("enter para : \n")
if "  " in str :
    str = str.replace("  ", " ")
    print("it's contain double space which is repalced with single space")
    # print(str)
else :
    print("it does not contain double space")
    # print(str)
print(str)