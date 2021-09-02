class Student:
    def studentData(self):
        self.name = input("Enter Student Name : ")
        self.id = input("Enter Student id : ")

    def Show_studentData(self):
        print(f"Student Name : {self.name}\nStudent Id : {self.id}")

class Fee(Student):
    def feeStatus(self):
        self.studentData()
        print("Completed or Incomplete ")

        self.status = input("Enter Fee Status : ")

    def Show_feeStatus(self):
        self.Show_studentData()
        print(f"Student FEE's Status : {self.status}")

class Marks(Student):
    def studentMarks(self):
        self.studentData()
        self.m1 = int(input(f"Enter m1 marks : "))
        self.m2 = int(input(F"Enter m2 marks : "))

    def Show_studentMarks(self):
        self.Show_studentData()
        print(f"M1 Marks : {self.m1} \nM2 Marks : {self.m2}")

class Sport(Student):
    def studentGrade(self):
        self.studentData()
        self.grade = input("Enter the Grade : ")

    def Show_studentGrade(self):
        self.Show_studentData()
        print(f"The Grade is : {self.grade}"
              )

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
student_1 = Fee()
student_1.feeStatus()
student_1.Show_feeStatus()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
student_2 = Marks()
student_2.studentMarks()
student_2.Show_studentMarks()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
student_3 = Sport()
student_3.studentGrade()
student_3.Show_studentGrade()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")