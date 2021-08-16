# sum of natural numbers : 
    
    
number = int(input("Enter the number : \n"))
sum = 0
for value in range(0,number+1):
    sum = sum + value
print("Sum of the number is : \n"+ str(sum))