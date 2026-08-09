import json
import utils

from pathlib import Path

FILE_NAME = Path(__file__).parent / "employees.json"
def load_employees():

    try:

        with open(FILE_NAME,"r") as file:
            return json.load(file)

    except FileNotFoundError:
        return [] 
    
    except json.JSONDecodeError:
        print("Error: emp.json contains invalid JSON.")
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

        "id": utils.get_int("ID : "),

        "name": input("Name : "),

        "department": input("Department : "),

        "salary": utils.get_float("Salary : ")
    }
    for item in employees:
        if item["id"] == emp["id"]:
            print("Employee ID already exists")
            return   
        
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
           
def update_employee(employee_id: int) -> None:
    employees = load_employees()

    for emp in employees:

        if emp["id"] == employee_id:

            print("Employee Found")

            # Ask for new values here
            
            print("Current Name: ", emp["name"])
            new_name = input("(press Enter to keep current):")
            if new_name:
                    emp["name"] = new_name
                    
                    
            print("Current Department: ", emp["department"])
            new_dept = input("(press Enter to keep current):")
            if new_dept:
                    emp["department"] = new_dept
                    
            print("Current Salary: ", emp["salary"])
            new_sal = input("(press Enter to keep current):")
            if new_sal:
                    emp["salary"] = utils.get_float(new_sal)

           

            # Save employees here
            save_employees(employees)
            print("Employee Updated.")
            return

    print("Employee not found.")
    

def delete_employee(employee_id: int) -> None:
    employees = load_employees()

    for emp in employees:

        if emp["id"] == employee_id:

            # Display employee

            confirm = input("Delete employee? (Y/N): ")

            if confirm.strip().lower() == "y":

                # Remove employee
                employees.remove(emp)
                # Save employees
                save_employees(employees)

                print("Employee deleted successfully.")

            return

    print("Employee not found.")
