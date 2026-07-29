import json

FILE_NAME = "employees.json"
def load_employees():

    try:

        with open(FILE_NAME,"r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
    
def save_employees(employees):

    with open(FILE_NAME,"w") as file:

        json.dump(
            employees,
            file,
            indent=4
        )
def add_employee():

    employees = load_employees()

    emp = {

        "id": int(input("ID : ")),

        "name": input("Name : "),

        "department": input("Department : "),

        "salary": float(input("Salary : "))
    }
         
    employees.append(emp)

    save_employees(employees)

    print("Employee Added.")
    
def list_employees():

    employees = load_employees()

    if not employees:
        print("No employees found.")
        return

    for emp in employees:

        print(
            emp["id"],
            emp["name"],
            emp["department"],
            emp["salary"]
        )





def search_employee(employee_id: int):
    
    employees = load_employees()

    if not employees:
        print("No employees found.")
        return

    for emp in employees:
        if emp["id"] == employee_id:
            print(
            emp["id"],
            emp["name"],
            emp["department"],
            emp["salary"]
            )
            return
        
    print("Employee not found")
           
    

    
