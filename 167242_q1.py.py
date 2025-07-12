# Filename: 167242_q1.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{book.title} has been borrowed.")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{book.title} has been returned.")

    def list_borrowed_books(self):
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(f"- {book.title} by {book.author}")


# Interactive part
if __name__ == '__main__':
    book1 = Book("1984", "George Orwell")
    book2 = Book("Brave New World", "Aldous Huxley")
    member = LibraryMember("Alice", "M001")

    while True:
        print("\n1. Borrow a book\n2. Return a book\n3. List borrowed books\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            if title == book1.title:
                member.borrow_book(book1)
            elif title == book2.title:
                member.borrow_book(book2)
            else:
                print("Book not found.")

        elif choice == '2':
            title = input("Enter book title to return: ")
            if title == book1.title:
                member.return_book(book1)
            elif title == book2.title:
                member.return_book(book2)
            else:
                print("Book not found.")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            break
        else:
            print("Invalid option.")


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
        self.students.append(student)

    def assign_grade(self, student_id, assignment, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment, grade)
                print(f"Grade added for {student.name}.")
                return
        print("Student not found.")

    def display_students(self):
        print(f"Students in {self.course_name}:")
        for student in self.students:
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
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment, grade)

        elif choice == '3':
            instructor.display_students()

        elif choice == '4':
            break
        else:
            print("Invalid option.")


# Filename: 167242_q3.py

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for {self.department_name}: {total}")

    def display_employees(self):
        print(f"Employees in {self.department_name}:")
        for emp in self.employees:
            emp.display_details()


# Interactive part
if __name__ == '__main__':
    department = Department("IT Department")

    while True:
        print("\n1. Add employee\n2. Display employees\n3. Show total salary expenditure\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            emp_id = input("Enter employee ID: ")
            salary = float(input("Enter salary: "))
            employee = Employee(name, emp_id, salary)
            department.add_employee(employee)

        elif choice == '2':
            department.display_employees()

        elif choice == '3':
            department.total_salary_expenditure()

        elif choice == '4':
            break
        else:
            print("Invalid option.")
