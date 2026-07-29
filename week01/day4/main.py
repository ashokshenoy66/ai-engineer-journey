import calculator
import employee
import utils
import employee_db


def show_menu():
    print("\n===== AI Office Toolkit =====")
    print("1. Calculator")
    print("2. Bonus Calculator")
    print("3. Even or Odd")
    print("4. Prime Number")
    print("5. BMI Calculator")
    print("6. Employee Database")
    print("7. Exit")

def display_calculator_menu():
    operations = [
    "1 Add",
    "2 Subtract",
    "3 Multiply",
    "4 Divide"
]

    for item in operations:
        print(item)
        
def display_employee_menu():
    operations = [
    "1 Add Employee",
    "2 List Employee",
    "3 Search by ID",
    "4 Return"
    ]

    for item in operations:
        print(item)
 
    

def main():    
    while True:      
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                a = float(input("First Number: "))
                b = float(input("Second Number: "))

                display_calculator_menu()

                operation = input("Select Operation: ")

                if operation == "1":
                    result = calculator.add(a, b)

                elif operation == "2":
                    result = calculator.subtract(a, b)

                elif operation == "3":
                    result = calculator.multiply(a, b)

                elif operation == "4":
                    result = calculator.divide(a, b)

                else:
                    print("Invalid Operation")
                    continue

                print("Answer =", result)
                again = input("Do another calculation? (Y/N): ")

                if again != "Y" and again != "y":
                    break

        elif choice == "2":
            salary = float(input("Enter Salary: "))
            bonus = employee.calculate_bonus(salary)
            print("Bonus =", bonus)

        elif choice == "3":
            number = int(input("Enter Number: "))

            is_even = utils.is_even(number)

            if is_even:
                print("Even Number")
            else:
                print("Odd Number")

        elif choice == "4":
            number = int(input("Enter Number: "))

            if utils.is_prime(number):
                print("Prime")
            else:
                print("Not Prime")

        elif choice == "5":
            print("BMI Selected")
            
        elif choice == "6":
            display_employee_menu()
            
            operation = input("Select Operation: ")
            
            if operation == "1":
                    result = employee_db.add_employee()

            elif operation == "2":
                result = employee_db.list_employees()
                
            elif operation == "3":
                searchid = int(input("enter ID: "))
                result = employee_db.search_employee(searchid)

            else :
                continue


        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")
            

            
if __name__ == "__main__":
    main()