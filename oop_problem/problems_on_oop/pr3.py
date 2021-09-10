# statement :
'''
Create a class with a class attribute a ; Create an object from it and set a directly using object a =o.
Does this changes the class attribute?
'''

# code :
class names:
    name = "aditya"

n = names()
# print(n.name)
n.name = "adi"

print(names.name)
print(n.name)


### ans is : NO ; it does not changes class attribute!
# # to changes the class attribute we have to use following syntax :
#
# names.name = "adi"
# print(names.name)