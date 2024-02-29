# lib/helpers.py
from models.employee import Employee
from models.order import Order

def list_employees(employees):
    # employees = Employee.get_all()
    for count, ele in enumerate(employees, start=1):
        print(count,": ",ele.first_name, " ",ele.last_name)
    # print("Performing useful function#1.")

def list_orders(orders):
    for count, ele in enumearte(orders, start=1):
        print( "Orders to be listed")

def list_employee_orders(employee):
    pass

def department_menu():
    pass

def employees_menu():
    employees = Employee.get_all()

    while True:
        print("Your current employees:")
        list_employees(employees)
        user_input = (input("Select one of the employees by selecting the number next to them, enter 'b' for back or 0 to exit: "))

        if user_input == "0":
            exit_program()
        elif user_input == "b" or user_input == "B":
            print("Returning to the Main Menu")
            return 
        elif int(user_input) > 0 and int(user_input)<=len(employees):
            employee_submenu(employees[int(user_input)-1])
        else:
            print("That isn't a valid choice. Please choose again!")

def employee_submenu(employee):
    print(f"You are currently viewing {employee.first_name} {employee.last_name}'s profile. Do you wish to perform any actions?")
    print(f"First name: {employee.first_name}")
    print(f"Last name: {employee.last_name}")
    print(f"Position: {employee.job_title}")
    print(f"Department: {employee.department}")

    while True:
        print(f"Enter o to view all the orders for {employee.first_name} {employee.last_name}")
        print(f"Enter u to updated {employee.first_name} {employee.last_name} information")
        print(f"Enter d to delete {employee.first_name} {employee.last_name}'s profile")
        print("Enter b to go back to the previous menu")
        print("Enter 0 to exit the program")

        choice = input(">")
        if choice == "o" or choice == "O":
            current_employee_orders = employee.orders()
            list_employee_orders(current_employee_orders)
        elif choice == "u" or choice == "U":
            pass
        elif choice == "d" or choice == "D":
            pass
        elif choice == "b" or choice == "B":
            print("Returning to the Previous Menu")
            return
        elif choice == "0":
            exit_program()
        else:
            print("That isn't a valid choice. Please choose again!")

def exit_program():
    print("Goodbye!")
    exit()
