import student
class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        # print(f"✅ Student {student.name} added to {self.name} department.")
        # print()
        
    def view_all_students(self):
        if not self.students:
            print(f"No students in {self.name} Department.")
            print()
            return
        print("********************************************************************")
        print(f"Students in {self.name} Department:")
        print()
        for student in self.students:
            student.display_info()
            print()
    
    def find_student_by_id(self, student_id):
        if not self.students:
            print(f"No students in {self.name} Department.")
            print()
            return
        for student in self.students:
            if student.id == student_id:
                return student
        return None
