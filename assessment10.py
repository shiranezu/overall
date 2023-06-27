class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return f"{self.name} has ${self.salary} as salary"
    
class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.bonus = 10/100

    def get_salary(self):
        return self.salary + (self.salary * self.bonus)

class Engineer(Employee):
     def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.bonus = 5/100

     def get_salary(self):
        return self.salary + (self.salary * self.bonus)
     
         
def payroll(employees):
    for employee in employees:
        print(f"Name :{employee.name} salary: ${employee.get_salary()}")

employees =[Manager('jack', 200000), Engineer('mary', 200000)]
payroll(employees)