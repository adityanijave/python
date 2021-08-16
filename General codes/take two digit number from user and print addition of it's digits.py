#take two digit number from user and print addition of it's digits  :
    
number_taking_two_digit_from_user = int(input("Enter two digit number :\n"))
for_first_digit = number_taking_two_digit_from_user//10
print("\nThis is the value of first digit   :\n"+str(for_first_digit))
for_secound_digit = number_taking_two_digit_from_user%10
print("This is the value of secound digit :\n"+str(for_secound_digit))
sum_of_two_digit = for_first_digit + for_secound_digit
print("\nSum of their digit is : \n"+str(sum_of_two_digit))


