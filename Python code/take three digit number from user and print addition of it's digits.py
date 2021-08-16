# take three digit number from user and print addition of it's digits:

number_taking_three_digit_from_user = int(input("Enter three digit number :\n"))
for_first_digit = number_taking_three_digit_from_user //100 
print("\nThis is the value of first digit : \n"+str(for_first_digit ))
c = number_taking_three_digit_from_user %100 
for_secound_digit = c//10 
print("This is the value of secound digit : \n"+str( for_secound_digit ))
for_third_digit = c%10  
print("This is the value of secound digit : \n" + str(for_third_digit ))
print("\nSum of the three digit are :\n" +str(for_first_digit + for_secound_digit + for_third_digit ))