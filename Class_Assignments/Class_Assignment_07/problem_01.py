'''
#  Write a Python program to get a string from a
#  given string where all occurrences of its first char
#  have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$$'
'''



word = input("enter the str : ")
new_word = ""
l = []

for i in word:
    if i in l :
        r = i.replace(i,"$")
        ll = l.append(r)
    else:
        ll = l.append(i)

for lll in l :
    new_word += lll
print(new_word)
























# for chr in word:
#     if chr in new_word:
#         r = word.replace(chr,"$")
#         new_word += r
#     else :
#         new_word += chr
#
# print(new_word)
