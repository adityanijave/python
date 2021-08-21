# . Write a Python program to get the frequency of the elements in a list.



given_list = [1,2,2,3,3,3]
required_list_for_ele =[]
required_list_for_ele_fre = []
for ele in given_list:
    a = given_list.count(ele)
    required_list_for_ele.append(ele)
    required_list_for_ele_fre.append(a)
z = zip(required_list_for_ele,required_list_for_ele_fre)
dict = dict(z)
print(dict)
