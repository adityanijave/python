import datetime

current = datetime.datetime.now()
print(f"Date : {current.date()}", f"{current.strftime('%A')}")
print(f"Time : {current.strftime('%I') + ':' + current.strftime('%M') + ' ' + current.strftime('%p')}")

