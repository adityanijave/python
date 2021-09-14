number = int(input("enter a number between 5 and 10 : "))
'''
syntax :
      assert condition , message 
'''

try:
    assert 5 <= number <= 10, "Number is not in between 5 and 10"
    print("Yes! The number you entered is correct .")
except AssertionError as e:
    print(e)
finally:
    print("code run without system error!")