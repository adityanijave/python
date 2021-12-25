class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def callingName(self):
        print("Hello my name is " + self.name)

    def callingAge(self):
      print(f"and my age is {self.age}")


p1 = Person("John", 36)
p1.callingName()
p1.callingAge()
