'''
Can you change the self parameter inside a class to something else (Say "Aditya").
try changing self to "fname" or "Aditya" and see the effects
'''

#code:
class Name:
    def __init__(fname,name):
        fname.name = name

    def show(fname):
        print(f"My name is {fname.name}")

self = Name("Aditya")
self.show()

# it run without error because it is just a parameter .
# we can change it but for conveniences we use "self" parameter!