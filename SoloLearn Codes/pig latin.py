import re
s1 = input("Enter string:")
s1=s1.lower()
s2 = re.sub(r'[^\w\s]', '', s1)
print(s2)
temp=[]
arr = s2.split(" ")
for x in arr:
    print(x)
    temp.append(x[1:]+x[0]+'ay')
s3=""
for x in temp:
    s3+=" "+x
s3=s3.strip()
print(s3)