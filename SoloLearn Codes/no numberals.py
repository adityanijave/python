# user = input("enter : ")
# usersplit = user.split(" ")
# str = 0
# for usersplit[str] in usersplit:
#     if usersplit[str]=="1":
#         usersplit[str]="one"
#     if usersplit[str]=="2":
#         usersplit[str]="two"
#     if usersplit[str]=="3":
#         usersplit[str]="three"
#     if usersplit[str]=="4":
#         usersplit[str]="four"
#     if usersplit[str]=="5":
#         usersplit[str]="five"
#     if usersplit[str]=="6":
#         usersplit[str]="six"
#     if usersplit[str]=="7":
#         usersplit[str]="seven"
#     if usersplit[str]=="8":
#         usersplit[str]="eight"
#     if usersplit[str]=="9":
#         usersplit[str]="nine"
#     if usersplit[str]=="0":
#         usersplit[str]="zero"
#     str += 1
# newstring = ""
# for word in usersplit:
#     newstring = newstring+word+" "
# print(newstring)
#


# a = input("enter :")
# if "1"in a:
#     b = a.replace("1","one")
# if "2" in b:
#     c = b.replace("2","two")
# if "3" in c :
#     d = c.replace("3","three")
# if "4" in d:
#     e = d.replace("4","four")
# if "5" in e :
#     f = e.replace("5","five")
# if "6" in f :
#     g = f.replace("6","six")
# if "7" in g:
#     h = g.replace("7","seven")
# if "8" in h:
#     i = h.replace("8","eight")
# if "9" in i :
#     j = i.replace("9","nine")
# if "0" in j :
#     finalconstractstris = j.replace("0","zero")
# print(finalconstractstris)

a = input("enter :")
b = a.replace("0","zero").replace("1","one").replace("2","two").replace("3","three").replace("4","four").replace("5","five").replace("6","six").replace("7","seven").replace("8","eight").replace("9","nine")
print(b)
