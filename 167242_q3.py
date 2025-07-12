
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
