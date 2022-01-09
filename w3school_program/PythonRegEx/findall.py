import re

string = '''my self aditya arun nijave
currently im living in pune for edu.
'''

finding_i = re.findall("i", string)

print(f"The 'i' in string is {finding_i}")
print(f"The number of time 'i' in string is {len(finding_i)}")
