class PersonalInfo:
    def __init__(self, name="NA"):
        self.name = name

    def callingName(self):
        print(f"{self.name}")


# name = "adi"

name1 = PersonalInfo()

name1.callingName()
