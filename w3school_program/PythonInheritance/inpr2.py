class Parent:
    def father(self):
        self.fn = input("enter father name : ")

    def surname(self):
        self.sn = input("enter your surname : ")

    def printFathername(self):
        print(f"{self.fn}")

    def printSurname(self):
        print(f"{self.sn}")


class Child_01():
    def child1name(self):
        self.cn1 = input("enter 1st child name : ")

    def callingFullname(self):
        print(f"{self.cn1} {self.fn} {self.sn}")


class Child_02():
    def child2name(self):
        self.cn2 = input("enter 2st child name : ")

    def callingFullname(self):
        print(f"{self.cn2} {self.fn} {self.sn}")


class Fam(Parent, Child_01, Child_02):
    def family(self):
        print(f"{self.cn1} and {self.cn2} both are children of {self.fn} {self.sn}")


# fam1 = Child_01()
# fam1.child1name()
# fam1.father()
# fam1.surname()
# fam1.callingFullname()
#
# fam2 = Child_02()
# fam2.child2name()
# fam2.father()
# fam2.surname()
# fam2.callingFullname()

fam3 = Fam()
fam3.child1name()
fam3.child2name()
fam3.father()
fam3.surname()
fam3.family()