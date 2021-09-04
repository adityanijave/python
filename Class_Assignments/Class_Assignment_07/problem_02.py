''''#  Write a Python program to get a string from a
#  given string where all occurrences of its first char
#  have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
'''

s = input("Enter the word !!!!!! : ")
r = s[0]
m = ""
n = ""
l = []
for i in s:
    if i == r:
        j = i.replace(i,"$")
        n = n+j
    else:
        n+=i
for  i in n :
    l.append(i)
l[0] = r
for i in l :
    m +=i
print(m)