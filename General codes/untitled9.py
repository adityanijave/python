l = ["harry","adi","soham","ruhi","shubha", "abc"]
print(type(l))
print(l)

for name in l :
    if name.startswith('s') :
        print("ram ram ! " , name)
    elif name.startswith('r'):
        print(name," 143")
    elif name.startswith("a"):
        print("its abc waala name")
    else : 
       print("hey!" , name)
    