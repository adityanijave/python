import re

string = '''my self aditya arun nijave
currently im living in pune for edu.
'''

search_aditya = re.search("aditya", string)

if search_aditya is not None :
    print("we get a match")
else:
    print("not find any match")
