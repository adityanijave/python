set1 = {1, "adi", 3}
set2 = {2, "ruhi", 3}

# by using : union
set3 = set1.union(set2)
print(set3)

# by using : update
set1.update(set2)
# print(set1)


# by using : intersection_update
set1.intersection_update(set2)
print(set1)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)