class dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def bark(self):
        print("woof!!!")
fido = dog("fido","brown")
print(fido.name)
print(fido.color)
fido.bark()