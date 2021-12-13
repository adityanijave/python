fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newFruitList = list()
# for fruit in fruits:
#     if fruit[0] == "a":
#         newFruitList.append(fruit)

# ############list comprehension ###############

newFruitList = [fruit for fruit in fruits if fruit[0] == "a"]
print(newFruitList)
