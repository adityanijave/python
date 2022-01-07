# A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function.

def myFunction():
    x = 9
    print(f"The value of x is {x}")


myFunction()