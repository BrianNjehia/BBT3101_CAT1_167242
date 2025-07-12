# Filename: 167242_q2.py

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"Grades for {self.name}:")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                print(f"Student ID {student.student_id} already exists.")
                return
        self.students.append(student)
        print(f"Student {student.name} added.")

    def assign_grade(self, student_id, assignment, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment, grade)
                print(f"Grade added for {student.name}.")
                return
        print("Student not found.")

    def display_students(self):
        print(f"\nStudents in {self.course_name}:")
        for student in sorted(self.students, key=lambda s: s.name):
            print(f"- {student.name} ({student.student_id})")
            student.display_grades()


# Interactive part
if __name__ == '__main__':
    instructor = Instructor("Dr. Smith", "Python Programming")

    while True:
        print("\n1. Add student\n2. Assign grade\n3. Display all students\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == '2':
            student_id = input("Enter student ID: ")
            assignment = input("Enter assignment name: ")
            try:
                grade = float(input("Enter grade: "))
                instructor.assign_grade(student_id, assignment, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == '3':
            instructor.display_students()

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option.")
