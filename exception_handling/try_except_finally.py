a = int(input("enter the num 1 : "))
b = int(input("enter the num 2 : "))

try:
    c = a/b
    print(f"The Division is {c}")

except ZeroDivisionError as e :
    print(f"Can't divide by zero!")

finally:
    print("code run without system error!")