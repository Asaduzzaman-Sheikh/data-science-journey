class Student:
    
    # CLASS VARIABLE
    total_students = 0
    def __init__(self, name, id, department, cgpa):
        self.name = name
        self.id = id
        self.department = department
        self.cgpa = cgpa
        Student.total_students += 1
        
        # print("✅ Student object created successfully.")
        # print(f"Total students: {Student.total_students}")
        # print()
    
    def display_info(self):
        print("Student Information:")
        print("--------------------------------------------------------")
        print(f"| Name: {self.name}")
        print(f"| ID: {self.id}")
        print(f"| Department: {self.department}")
        print(f"| CGPA: {self.cgpa}")
        print("--------------------------------------------------------")
        print()

    # METHOD TO UPDATE CGPA
    def update_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa
        print(f"CGPA updated to: {self.cgpa} for student {self.name}")
        print()
        
    # METHOD TO GET STUDENT INFO AS DICTIONARY
    def get_info_dict(self):
        return f"🎓 {self.name} (ID: {self.id} | Department: {self.department} | CGPA: {self.cgpa})"
        
# s = Student("John Doe", "CSE101", "Computer Science & Engineering", 3.5)
# s.display_info()

# s.update_cgpa(3.7)
# s.display_info()
