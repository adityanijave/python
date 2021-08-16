import os

with open("demoo.txt") as file :
    con = file.read()
with open("Demo.txt","w") as file :
    file.write(con)
    
os.remove("demoo.txt")