#count funtion use :

  
number1 = int(input("Enter number 1 :\n"))
number2 = int(input("Enter number 2 :\n"))
number3 = int(input("Enter number 3 :\n"))
number4 = int(input("Enter number 4 :\n"))

numberwanttocount = int(input("Enter that number which you want to count : \n"))
tp = (number1,number2,number3,number4)

print("Count of that number is : " , tp.count(numberwanttocount))