'''Write a Python program to get a single string
from two given strings, separated by a space and swap
the first two characters of each string.

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz''
'''

p = input("Enter two words : ").split(" ")
# p = "abc xyz".split(" ")
q = p[::-1]
r = q[0][-1]
s = q[-1][-1]

t = q[0]
u = []
for i in t:
    u.append(i)
u[-1] = s
a = ""
for i in u:
    a+=i


v = q[-1]
w = []
for i in v:
    w.append(i)
w[-1] = r
b = ""
for i in w:
    b += i

uu = []
uu.append(a)
uu.append(b)
us = ""
for i in uu:
    us = us+" "+i
print(us.replace(" ","",1))
