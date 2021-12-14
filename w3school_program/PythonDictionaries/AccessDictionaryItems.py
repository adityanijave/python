thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
modelName = thisdict["model"]
print(modelName)


print(type(modelName))
print(len(modelName))
print()

brandName = thisdict["brand"]

print(brandName)
print(type(brandName))
print(len(brandName))
print()

year = thisdict["year"]
print(year)
print(type(year))
print()

print(thisdict.get("model"), thisdict.get("brand"), thisdict.get(year))
print(thisdict.keys(), thisdict.values(), thisdict)
print()

print(thisdict.items())
