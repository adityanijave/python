class My_exception(Exception):
    def __init__(self, msg):
        self.msg = msg

user_entered_number  = int(input("Enter the number divisible by 5 : "))

try :
    if user_entered_number % 5 != 0:
        error = My_exception("The number you entered is not divisible by 5")
        raise error
    print("The number you entered is divisible by 5!")

except  My_exception as e:
    print(e)