# exam code solution :


n1 = int(input())
n2 = int(input())

if (n1 or n2) >= 21 and (n1 != n2):
    print(-1)
elif (n1 == n2) or (n1 or n2 >= 21):
    print(-2)
