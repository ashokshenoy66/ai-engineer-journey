import json

from pathlib import Path

FILE_NAME = Path(__file__).parent / "employees.json"
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
    for item in employees:
        if item["id"] == emp["id"]:
            print("Employee ID already exists")
            return   
        else:
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
           
    

    
