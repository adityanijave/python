class PersonInfo:
    def __init__(self, name, age, area, school):
        self.name = name
        self.age = int(age)
        self.area = area
        self.school = school


persona1 = PersonInfo("aditya", "19", "pune", "mcoe")

print(f"the name of student is {persona1.name} and their age is  {persona1.age}  and they live in {persona1.area} and they are from {persona1.school}")
