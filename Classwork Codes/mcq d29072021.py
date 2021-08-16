#problem 1 :
print("============problem 1================")
for i in range(10,14):
    for j in range(2,i):
        if i%j == 1 :
            print(i)
            break
        
        
        
#problem 2 :
print("============problem 2================")
for i in range(0,2,-1):
    print("hello")


#problem 3:
print("============problem 3================")
x = "abcdef"
i = "i"
while i in x :
    print(i,end=" ")