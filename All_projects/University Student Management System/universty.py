import department
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
    
    def add_department(self, department):
        self.departments.append(department)
        department.university = self
        # print(f"✅ Department {department.name} added to {self.name}.")
        # print()
        
    def search_student_by_id(self, student_id):
        for department in self.departments:
            student = department.find_student_by_id(student_id)
            if student:
                return student
        print(f"❌ No student found with ID: {student_id} in {self.name}.")
        print()
        

# CREATE UNIVERSITY INSTANCE
my_university = University("Northern University Bangladesh")

"""
    Adding initial departments to the university and students to departments.
"""

# ADD INITIAL DEPARTMENTS
cse_department = department.Department("Computer Science & Engineering")
my_university.add_department(cse_department)

# ADD ANOTHER DEPARTMENT
math_department = department.Department("Mathematics")
my_university.add_department(math_department)

# ADD ANOTHER DEPARTMENTS
eee_department = department.Department("Electrical & Electronics Engineering")
my_university.add_department(eee_department)

# ADD STUDENTS TO CSE DEPARTMENT
student1 = department.student.Student("Alice", "CSE123", "Computer Science & Engineering", 3.8)
cse_department.add_student(student1)

student2 = department.student.Student("Bob", "CSE456", "Computer Science & Engineering", 3.6)
cse_department.add_student(student2)

student3 = department.student.Student("Clara", "CSE789", "Computer Science & Engineering", 3.7)
cse_department.add_student(student3)




# ADD STUDENTS TO MATH DEPARTMENT
student4 = department.student.Student("David", "MTH789", "Mathematics", 3.9)
math_department.add_student(student4)

student5 = department.student.Student("Eva", "MTH456", "Mathematics", 3.7)
math_department.add_student(student5)

student6 = department.student.Student("Frank", "MTH123", "Mathematics", 3.5)
math_department.add_student(student6)





# ADD STUDENTS TO EEE DEPARTMENT
student7 = department.student.Student("Charlie", "EEE789", "Electrical & Electronics Engineering", 3.7)
eee_department.add_student(student7)

student8 = department.student.Student("Diana", "EEE456", "Electrical & Electronics Engineering", 3.8)
eee_department.add_student(student8)

student9 = department.student.Student("Ethan", "EEE111", "Electrical & Electronics Engineering", 3.9)
eee_department.add_student(student9)




# VERIFYING ADMIN SECURITY
admin_password = "admin123"
i = 1
while i <= 3:
    password = input("Enter admin password to access the system: ")
    if password == admin_password:
        print("✅ Access granted. Welcome, Admin!")
        print()
        break
    else:
        print("❌ Incorrect password. Please try again.")
        print()
    i += 1
if i > 3:
    print("❌ Too many incorrect attempts. Exiting the system.")
    exit()
    

# INTERACTIVE MENU
while True:
    print("=========== University Student Management System ===========")
    print("1. View All Departments")
    print("2. Add Student to Department")
    print("3. View All Students in a Department")
    print("4. Search Student by ID")
    print("5. Update Student CGPA by ID")
    print("6. Exit")

    user_input = input("Enter your choice (1-6): ")
    print()

    # VIEW ALL DEPARTMENTS
    if user_input == "1":
        print("============================================================")
        print(f"Departments in {my_university.name}:")
        for dept in my_university.departments:
            print(f" - {dept.name}")
        print("============================================================")
        print()
    
    # ADD STUDENT TO DEPARTMENT
    elif user_input == "2":
        dept_name = input("Enter department's full name: ").title()
        
        # CHECK IF DEPARTMENT EXISTS
        if dept_name not in [d.name for d in my_university.departments]:
            print(f"❌ Department {dept_name} does not exist.")
            print()
            continue
        
        student_name = input("Enter student's name: ").title()
        student_id = input("Enter student's ID: ").upper()
        student_department = dept_name
        student_cgpa = float(input("Enter student's CGPA: "))
        
        # ADDING STUDENT TO DEPARTMENT
        new_student = department.student.Student(student_name, student_id, student_department, student_cgpa)
        
        for dept in my_university.departments:
            if dept.name == dept_name:
                dept.add_student(new_student)
                # print(f"✅ Student {student_name} added to {dept_name} department.")
                # print()
                break
    # VIEW ALL STUDENTS IN DEPARTMENT
    elif user_input == "3":
        dept_name = input("Enter department's full name: ").title()
        
        # VIEW ALL STUDENTS IN DEPARTMENT
        for dept in my_university.departments:
            if dept.name == dept_name:
                dept.view_all_students()
                break
        else:
            print(f"❌ Department {dept_name} does not exist.")
            print()
    # SEARCH STUDENT BY ID IN UNIVERSITY
    elif user_input == "4":
        student_id = input("Enter student ID to search: ").upper()
        student_found = False
        for dept in my_university.departments:
            student = dept.find_student_by_id(student_id)
            if student:
                print("Student found:")
                print(f"🎓 {student.name} (ID: {student.id} | Department: {student.department} | CGPA: {student.cgpa})")
                print()
                student_found = True
                break
        if not student_found:
            print(f"❌ Student with ID {student_id} not found.")
            print()
    
    # UPDATE STUDENT CGPA BY ID IN UNIVERSITY
    elif user_input == "5":
        student_id = input("Enter student ID to update CGPA: ").upper()
        new_cgpa = float(input("Enter new CGPA: "))
        student_found = False
        for dept in my_university.departments:
            student = dept.find_student_by_id(student_id)
            if student:
                student.update_cgpa(new_cgpa)
                print(f"✅ Student {student.name}'s CGPA updated to {new_cgpa}.")
                print()
                student_found = True
                break
        if not student_found:
            print(f"❌ Could not update CGPA for student with ID {student_id}.")
            print()
    # EXIT THE SYSTEM
    elif user_input == "6":
        print("Exiting the University Student Management System. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 6.")
        print()