# #defing the function :     
# def maximum_number(number1,number2,number3):
#     if (number1>number2):
#         if (number1>number3):
#             return number1
#         else :
#             return number3
#     else :
#         if number2>number3:
#             return number2
#         else : 
#             return number3

# #taking input from user :
# n1 = int(input("Enter the number :\n"))
# n2 = int(input("Enter the number :\n"))
# n3 = int(input("Enter the number :\n"))

# #calling the function :
# m = maximum_number(n1,n2,n3)

# #getting output :     
# print("\nGreater number is  :\n"+str(m))




#####################              another way                   #######################




#defing the function : 
def maximum_number(number1,number2,number3):
    if number1>number2 :
        greater_number_among_number1_and_number2 = number1
    else :
        greater_number_among_number1_and_number2 = number2
    if greater_number_among_number1_and_number2 > number3:
        print("\nGreater number is :\n"+str(greater_number_among_number1_and_number2))
    else :
       print("\nGreater number is :\n"+str(number3))
       
#taking input from user :
number1 = int(input("Enter your first  number :\n"))
number2 = int(input("Enter your secound number :\n"))
number3 = int(input("Enter your third number :\n"))

#calling the function :
maximum_number(number1, number2, number3)
