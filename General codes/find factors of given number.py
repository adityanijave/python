# problem :
''' create a python program to find factors of given number  '''

# soln:

number = int(input("Enter number :"))
fs = []
i = 1

for i in range(i, number):
    if number % i == 0:
        fs.append(i)
    i += 1
for f in fs:
    print(f)