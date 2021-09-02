s = input("enter str : ")
ss = s.split(" ")

for sss in ss:
    d = ss.count(sss)
    print(f"the count of '{sss}' in '{s}' is : {d}")