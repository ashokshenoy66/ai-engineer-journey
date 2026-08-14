class Employee:
    ''' define class Employee with attributes employee ID, name, department and salary"
        and methods calculate_bonus, give_increment, find_employee and change_department '''
    
    def __init__(self,employee_id,name,department,salary):
        self.id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
    
    def display(self):
        print(f"ID         : {self.id}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.department}")
        print(f"Salary     : {self.salary}")

    def calculate_bonus(self, percentage: float = 10) -> float:
        return self.salary * percentage / 100
    
    def give_increment(self, percentage: float)-> float:
        increment = self.salary * percentage /100
        self.salary = self.salary + increment
        return  self.salary
    
    
    
    def change_department(self, new_department: str) -> None:
        if new_department:
            self.department = new_department
            return 
     
def find_employee(employees: list[Employee], employee_id: int) -> Employee | None:
    for employee in employees:
        if employee.id == employee_id:
            return employee

    return None
    
# employee1, 2, 3 values
      
employee1 = Employee(
    101,
    "Ashok",
    "IT",
    75000
)

employee2 = Employee(
    102,
    "Priya",
    "HR",
    60000
)

employee3 = Employee(
    103,
    "Rahul",
    "Sales",
    55000
)

#employees list with dict
employees = [
    employee1,
    employee2,
    employee3
]
    
#display employees
for employee in employees:
    employee.display()  
 

#test employee search

employee = find_employee(employees, 103)

if employee:
    print ("\n")
    employee.display()
else:
    print("Employee not found")
    
    
#test change department

employee1.change_department("IT Support")
print ("\n")

employee1.display()
