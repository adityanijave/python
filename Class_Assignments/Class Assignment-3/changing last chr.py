i = input("enter string of two word : ")
j = i.split(" ")
a = j[0][-1]
ar = j[0].replace(a, "")
b = j[-1][-1]
br = j[-1].replace(b, "")
bra = br + a
arb = ar + b
l = bra + " " +arb
print("output string :",l)