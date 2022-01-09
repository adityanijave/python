try:
    print(999/0)
except ZeroDivisionError:
    print("can not divided by zero to any number")
except:
    print("something else")