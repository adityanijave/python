import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
print(x.count("ai"))
