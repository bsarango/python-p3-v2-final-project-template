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
    print

def exit_program():
    print("Goodbye!")
    exit()
