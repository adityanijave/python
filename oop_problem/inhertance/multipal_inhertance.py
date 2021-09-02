class student:
    def student_info(self):
        self.name = input(f"Enter student name : ")
        self.id = int(input(f"Enter id of student : "))

    def show_student_info(self):
        print(f"Student name : {self.name}\nStudent id : {self.id}")

class marks:
    def student_marks(self):
        self.math = int(input(f"Enter your math marks : "))
        self.science = int(input(f"Enter your science marks : "))

    def show_student_marks(self):
        print(f"Math Marks : {self.math}  &  Science Marks : {self.science}")

class result(student,marks):
    def overview(self):
        self.student_info()
        self.student_marks()

    def show_overview(self):
        self.show_student_info()
        self.show_student_marks()

# object name = class name()
st = result()
st.overview()
st.show_overview()