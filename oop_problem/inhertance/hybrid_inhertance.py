class Student:
    def student_Info(self):
        self.name = input("Enter Name : ")
        self.id = int(input("Enter id : "))

    def Show_student_Info(self):
        print(f"Student name : {self.name} \nStudent id : {self.id}")

class Marks(Student):
    def student_Marks(self):
      self.m1 = int(input(f"Enter m1 marks : "))
      self.m2 = int(input(f"Enter m2 marks : "))

    def Show_student_Marks(self):
        print(f"M1 marks : {self.m1} & M2 marks : {self.m2}")

class Sport:
    def student_Grade(self):
        self.grade = input("Enter Grade : ")

    def Show_student_Grade(self):
        print(f"With Grade : {self.grade}")

class Result(Marks,Sport):
    def student(self):
        self.student_Info()
        self.student_Marks()
        self.student_Grade()

    def Show_student(self):
        self.Show_student_Info()
        self.Show_student_Marks()
        self.Show_student_Grade()

student_1 = Result()
student_1.student()
student_1.Show_student()