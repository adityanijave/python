fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newFruits1 = [fruit if fruit[0] == "a" else "not supporting" for fruit in fruits]
print("newFruits1 = " + str( newFruits1))

newFruits2 = [fruit if fruit[0] != "a" else "totally supporting to required condition avoiding this one" for fruit in fruits]
print("newFruits2 = " + str(newFruits2))