import json as j

a = j.dumps({"name": "John", "age": 30})
print(f"type : {type(a)} and a = {a}")
print()

b = j.dumps(["apple", "bananas"])
print(f"type : {type(b)} and b = {b}")
print()

c = j.dumps(("apple", "bananas"))
print(f"type : {type(c)} and c = {c}")
print()

d = j.dumps("hello")
print(f"type : {type(d)} and a = {d}")
print()

e = j.dumps(42)
print(f"type : {type(e)} and a = {e}")
print()

f = j.dumps(31.76)
print(f"type : {type(f)} and a = {f}")
print()

g = j.dumps(True)
print(f"type : {type(g)} and a = {g}")
print()

h = j.dumps(False)
print(f"type : {type(h)} and a = {h}")
print()

i = j.dumps(None)
print(f"type : {type(i)} and a = {i}")
