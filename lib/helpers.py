# lib/helpers.py
from models.employee import Employee
from models.order import Order

def list_employees(employees):
    # employees = Employee.get_all()
    for count, ele in enumerate(employees, start=1):
        print(count,": ",ele.first_name, " ",ele.last_name)
    # print("Performing useful function#1.")

def department_menu():
    pass

def employees_menu():
    employees = Employee.get_all()

    while True:
        print("Your current employees:")
        list_employees(employees)
        user_input = (input("Select one of the employees by selecting the number next to them, enter B for back or 0 to exit: "))

        if user_input == "0":
            exit_program
        elif user_input == "b" or user_input == "B":
            main()
        elif int(user_input) > 0 and int(user_input)<len(employees):
            employee_submenu(employees[int(user_inpu)t-1])
        else:
            print("That isn't a valid choice. Please choose again!")

def employee_submenu(employee):
    print(f"You are currently viewing {employee.first_name} {employee.last_name}'s profile. Do you wish to perform any actions?")
    print(f"First name: {employee.first_name}")
    print(f"Last name: {employee.last_name}")
    print(f"Position: {employee.job_title}")
    print(f"Department: {employee.department}")



def exit_program():
    print("Goodbye!")
    exit()
