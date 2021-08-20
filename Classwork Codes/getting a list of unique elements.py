list_contining_duplicate_element = [1,2,3,1,1,2,5,6,8,2]
list_contining_unique_element = []
for element in list_contining_duplicate_element:
    if element not in list_contining_unique_element:
        list_contining_unique_element.append(element)
print(f"The new list is {list_contining_unique_element}")