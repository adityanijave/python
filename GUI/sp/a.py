First_Number = 2
Common_Difference = 5
Total_Number_Of_Terms = 7

required_variable_value = 0
ap_list = []
square_ap_list = []

while len(ap_list) != 7:
    Appending_Number = ap_list.append(First_Number)
    Appending_Square_Number = square_ap_list.append(First_Number*First_Number)
    First_Number += 5

for i in square_ap_list:
    required_variable_value += i

print(ap_list)
print(square_ap_list)
print(required_variable_value)