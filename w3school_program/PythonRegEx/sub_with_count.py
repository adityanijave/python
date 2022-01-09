import re

string = '''my self aditya arun nijave
currently im living in pune for edu.
string = my self aditya arun nijave
currently im living in pune for edu.
string = my self aditya arun nijave
currently im living in pune for edu.
'''

sub_string = re.sub("im", "aditya", string, 2)
print(sub_string)
