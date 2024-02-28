# lib/helpers.py
from models.employee import Employee
from models.order import Order

def list_employees(employees):
    # employees = Employee.get_all()
    for count, ele in enumerate(employees):
        print(count,": ",ele[first_name], " ",ele[last_name])
    # print("Performing useful function#1.")

def department_menu():
    pass

def employees_menu():
    employees = Employee.get_all()
    print("Select one of the employees by choosing the number next to their name to view their details.")
    list_employees(employees)
    employee_index = input("Select one of the employees by selecting the number next to them: ")
    employee_submenu(employees[employee_index-1])

def employee_submenu(employee):
    print(f"You are currently viewing {employee[first_name]} {employee[last_name]}'s profile. Do you wish to perform any actions?")


def exit_program():
    print("Goodbye!")
    exit()
