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
        employee_index = int(input("Select one of the employees by selecting the number next to them: "))
        if employee_index > 0 and employee_index<len(employees):
            employee_submenu(employees[employee_index-1])
        else:
            print("THat isn't a valid choice. Please choose again!")

def employee_submenu(employee):
    print(f"You are currently viewing {employee.first_name} {employee.last_name}'s profile. Do you wish to perform any actions?")
    print(f"First name: {employee.first_name}")
    print(f"Last name: {employee.last_name}")
    print(f"Position: {employee.job_title}")
    print(f"Department: {employee.department}")



def exit_program():
    print("Goodbye!")
    exit()
