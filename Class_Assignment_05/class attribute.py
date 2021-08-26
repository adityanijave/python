class dog:
    leg = 4
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def bark(self):
        print("woof!!!")
fido = dog("fido","brown")
print(fido.color)
print(fido.leg)
print(dog.leg)