# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

n = input("Enter the value of 'n' : ")
calculating_required_value = int(n) + int(str(n)+str(n)) + int(str(n)+str(n)+str(n))
print(f"The value of n+nn+nnn for given n = {n} is {calculating_required_value}")