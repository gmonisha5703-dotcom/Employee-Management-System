employees = {}

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    employees[emp_id] = {
        "Name": name,
        "Salary": salary
    }

    print("Employee Added Successfully!")

def view_employees():
    for emp_id, details in employees.items():
        print(emp_id, details)

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        break
    else:
        print("Invalid Choice")
