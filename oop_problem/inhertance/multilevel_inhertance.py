class Student:
    def student_Info(self):
        self.name = input(f"Enter Student Name :")
        self.id = int(input(f"Enter Student id : "))

    def show_Student_info(self):
        print(f"Name Of Student : {self.name} \nId Of Student : {self.id}")

class Marks(Student):
    def Student_marks(self):
        self.math = int(input(f"Enter Marks of Math : "))
        self.science = int(input(f"Enter Marks of Science : "))

    def show_Student_marks(self):
        print(f"Math Marks : {self.math} & Science Marks : {self.science}")

class Result(Marks):
    def data_Overview(self):
        self.student_Info()
        self.Student_marks()

    def Show_data_Overview(self):
        self.show_Student_info()
        self.show_Student_marks()

# objectname = classname()
student_1 = Result()
student_1.data_Overview()
student_1.Show_data_Overview()