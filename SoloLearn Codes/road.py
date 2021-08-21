#problem :
'''Pig Latin

You have two friends who are speaking Pig Latin to each other!
Pig Latin is the same words in the same order except that you take the first letter of each word and put it on the end,
then you add 'ay' to the end of that.
("road" = "oadray")

Task
Your task is to take a sentence in English and turn it into the same sentence in Pig Latin!
Input Format
A string of the sentence in English that you need to translate into Pig Latin. (no punctuation or capitalization)
Output Format
A string of the same sentence in Pig Latin.
Sample Input
"nevermind youve got them"
Sample Output
"evermindnay ouveyay otgay hemtay"'''

#soln:

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

















