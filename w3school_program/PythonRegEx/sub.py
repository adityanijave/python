import re

string = '''my self aditya arun nijave
currently im living in pune for edu.
string = my self aditya arun nijave
currently im living in pune for edu.
string = my self aditya arun nijave
currently im living in pune for edu.
'''

sub_string = re.sub("edu.", "edu\n*********************", string)
print(sub_string)
