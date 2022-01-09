'''
finally : if there is error in code and u still want to give the output
'''

try:
    print(a)
except ZeroDivisionError:
    print("error from division")
except:
    print("not defined")
finally:
    print(5+5)
