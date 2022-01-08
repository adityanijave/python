import json

# some JSON

JSON_data = '{"Name" : "Aditya_Nijave", "Age" : 19}'
print(f"JSON data type : {type(JSON_data)} \nJSON data : {JSON_data}")
# print(JSON_data["Name"])

print()

python_data = json.loads(JSON_data)
print(f"Python data type : {type(python_data)} \nPython data : {python_data}")
print(python_data["Name"])
