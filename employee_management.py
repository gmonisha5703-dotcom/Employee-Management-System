employees = {}

def add_employee():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        print("Employee ID already exists!")
        return

    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    employees[emp_id] = {
        "Name": name,
        "Salary": salary
    }

    print("Employee Added Successfully!")

def view_employees():
    if not employees:
        print("No Employee Records Found!")
        return

    print("\nEmployee Records:")
    for emp_id, details in employees.items():
        print("ID:", emp_id)
        print("Name:", details["Name"])
        print("Salary:", details["Salary"])
        print("----------------------")

def search_employee():
    emp_id = input("Enter Employee ID to Search: ")

    if emp_id in employees:
        print("Employee Found!")
        print(employees[emp_id])
    else:
        print("Employee Not Found!")

def update_employee():
    emp_id = input("Enter Employee ID to Update: ")

    if emp_id in employees:
        name = input("Enter New Name: ")
        salary = input("Enter New Salary: ")

        employees[emp_id]["Name"] = name
        employees[emp_id]["Salary"] = salary

        print("Employee Updated Successfully!")
    else:
        print("Employee Not Found!")

def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee Deleted Successfully!")
    else:
        print("Employee Not Found!")

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
