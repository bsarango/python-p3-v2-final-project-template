# lib/helpers.py
from models.employee import Employee
from models.order import Order

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print()
    # print("Performing useful function#1.")

def department_menu():
    pass

def exit_program():
    print("Goodbye!")
    exit()
