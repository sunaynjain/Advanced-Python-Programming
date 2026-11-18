class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def get_category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary: Rs.", self.salary)
        print("Category:", self.get_category())
        print()


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            employee.display()


company = Company()

e1 = Employee(101, "Amit", 80000)
e2 = Employee(102, "Neha", 55000)
e3 = Employee(103, "Rahul", 30000)

company.add_employee(e1)
company.add_employee(e2)
company.add_employee(e3)

company.display_employees()
