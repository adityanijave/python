chr = input("enter chr :\n")
if 65 <= ord(chr) <= 122 :
    print("it is an alphabte!")
elif  48 <= ord(chr) <= 57 :
    print("it is an digit!")
else :
    print("sepcial symbol!")
