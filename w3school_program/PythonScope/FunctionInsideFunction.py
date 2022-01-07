# Function Inside Function
# A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function.


def outerFunction():
    x = 9
    # print(f"The value of x is called by outer function")

    def innerFunction():
        print(f"The value of x is called by inner function")

    innerFunction()


outerFunction()
