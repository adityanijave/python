import json

pythonData = {"Name": "Aditya_Nijave",
              "Age": 19,
              "Everything is good": (False, True)}

print(f"pythonData : {pythonData} and type : {type(pythonData)}")
print()

JSON_data = json.dumps(pythonData)
print(f"JSON data : {JSON_data} and type : {type(JSON_data)}")
