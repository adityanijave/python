class student:
    def __init__(self):
        self.name = input("enter student name : ")
        self.id = input("enter the id :")

    # def show_nameandid(self):
    #     print(f"name of student : {self.name} \nid of student : {self.id}")

class mark(student):
    def student_mark(self):
        self.m1 = int(input("Enter the marks 1 : "))
        self.m2 = int(input("Enter the marks 2 : "))

    def show_m1andm2(self):
        print(f"name of student : {self.name}\nid of student ; {self.id}"
              f"\n{self.name} having m1 marks : {self.m1}\n{self.name} having m2 marks : {self.m2}")

# on = cn()
ob = mark()
# ob.show_nameandid()
ob.student_mark()
ob.show_m1andm2()