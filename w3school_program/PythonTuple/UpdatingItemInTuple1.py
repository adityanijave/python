thistuple = ("apple", "banana", "cherry", "apple", "cherry")

thistuple2 = list(thistuple)
thistuple2.append("aditya")
print(thistuple2, "type : ",type(thistuple2))

thistuple = tuple(thistuple2)
print(thistuple, "type : ",type(thistuple))
