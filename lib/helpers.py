# lib/helpers.py
from models.employee import Employee
from models.order import Order
import cli_color_py

def list_employees(employees):
    add_space()
    for count, ele in enumerate(employees, start=1):
        print(count,": ",ele.first_name, " ",ele.last_name)
    
def list_orders(orders):
    print("All current orders: ")
    add_space()
    if len(orders)>0:
        for count, ele in enumerate(orders, start=1):
            print(count,": ",ele.title)
    else:
        print(cli_color_py.yellow("There are currently no orders assigned"))

def create_order(_id):
    add_space
    title = input("Enter the order title: ")
    ordering_doctor = input("Enter the ordering doctor: ")
    completed_response = input("Is this a completed order (y or n): ")
    completed = None
    if completed_response == 'y' or completed =="Y":
        completed = 1
    elif completed_response == 'n' or completed_response == "N":
        completed = 0

    employee_id = _id

    try:
        Order.create(title, ordering_doctor,completed,employee_id)
        add_space()
        print(cli_color_py.green("Order placed!"))

    except Exception as exec:
        add_space()
        print(cli_color_py.red("Failed to create an order. Try again."))

def delete_order(order):
    add_space()
    print(cli_color_py.yellow("Are you sure you want to delete this order? Enter y or n"))
    choice = input(">")
    if choice == "y" or choice == "Y":
        order.delete()
        print(cli_color_py.green("The order has been removed."))
        return
    
    else:
        print(cli_color_py.red("There was an issue removing this order!"))

def update_order(order):
    add_space()
    print("Enter d to update the ordering doctor")
    print("Enter c to mark as completed")
    print("Enter e to changed assigned employee")

    choice = input(">")

    if choice == "d":
        new_doctor = input("Enter the new doctor: ")
        order.ordering_doctor = new_doctor
        order.update()
        print(cli_color_py.green("The ordering doctor has been updated!"))

    elif choice == "c":
        if order.completed == 1:
            print(cli_color_py.yellow("The order is already completed"))
        else:
            order.completed = 1
            order.update()
            print(cli_color_py.green("The order now has a completed status!"))

    elif choice == 'e':
        change_assigned_employee(order)
    
    else:
        print(cli_color_py.yellow("This isn't a valid choice, please try again!"))
    
        
def display_order_info(order):
    add_space()
    print("Order details:")
    print(f"Title: {order.title}")
    print(f"Ordering Doctor: {order.ordering_doctor}")
    assigned_employee = order.employee()
    if assigned_employee:
        print(f"Assigned employee: {assigned_employee.first_name} {assigned_employee.last_name}")
    else:
        print(cli_color_py.yellow("No current employee assigned to this order"))

    if order.completed == 1:
        print(f"Completion Status: Completed")
    else:
        print(f"Completion Status: Not Completed")
         
    print(f"Order issue time and date: {order.time_stamp}")

def change_assigned_employee(order):
    add_space()
    while True:
        employees = Employee.get_all()
        list_employees(employees)

        print("Enter the number of the employee to select or")
        print("Enter b to cancel and go back")

        choice = input(">")

        try:
            if int(choice) > 0 and int(choice) <= len(employees):
                new_employee = employees[int(choice)-1]
                order.employee_id = new_employee.id
                order.update()
                print(cli_color_py.green("A new employee has been assigned to this order"))
                return
            elif choice == "b":
                print("Returning to the previous menu")
                return
            else:
                print(cli_color_py.yellow("This isn't a valid choice for an employee, please try again!"))
        except Exceptions as exec:
            print("This isn't a valid choice, please choose again!")

def reassign_orders(employee):
    orders = employee.orders()
    for order in orders:
        order.ordering_doctor = "No current Doctor"
        order.update()

def display_employee_info(employee):
    add_space()
    print(f"You are currently viewing {employee.first_name} {employee.last_name}'s profile. Do you wish to perform any actions?")
    print(f"First name: {employee.first_name}")
    print(f"Last name: {employee.last_name}")
    print(f"Position: {employee.job_title}")
    print(f"Department: {employee.department}")

def create_employee():
    add_space()
    print("Are you sure you want to enter a new employee? Enter 'y' for yes or 'n' for no")
    choice = input(">")
    if choice == "y" or choice == "Y":
        first_name = input("Enter the employee's first name: ")
        last_name = input("Enter the employee's last name: ")
        job_title = input("Enter the employee's job title: ")
        department = input("Enter the employee's department: ")

        try:
            employee = Employee.create(first_name,last_name,job_title,department)
            print(f"{employee.first_name} {employee.last_name} has been successfully added to the system!")

        except Exception as exec:
            print(cli_color_py.red("There was an error in entering the new employee's info into the system. Try again."), exec) 
    
    elif choice == "n" or choice == 'N':
        print("Returning to the previous menu")
        return

    else:
        print(cli_color_py.yellow("This isn't a valid choice, please try again!"))

def update_employee(employee):
    add_space()
    print("Are you sure you want to update the employee? Enter 'y' for yes or 'n' for no")
    choice = input(">")
    if choice == "y" or choice == "Y":
        try:
            first_name = input("Enter the new first name or leave blank to leave the same.") 
            if first_name == "":
                print("Kept the same first name.")
            else:
                employee.first_name = first_name

            last_name = input("Enter the new last name or leave blank to leave the same.")
            if last_name == "":
                print("Kept the same last name.")
            else:
                employee.last_name = last_name

            job_title = input("Enter the new job title or leave blank to leave the same.")
            if job_title == "":
                print("Kept the same job title.")
            else:
                employee.job_title = job_title

            department = input("Enter the new department or leave blank to leave the same.")
            if department == "":
                print("Kept the same department.")
            else:
                employee.department = department

            employee.update()
            print(f"{employee.first_name} {employee.last_name} has been updated successfully!")

        except Exception as exec:
            print(cli_color_py.red(f"There was an error updating {employee.first_name} {employee.last}'s profile."), exec)
    
    elif choice == 'n' or choice == 'N':
        print("Returning to the previous menu")
        return

    else:
        print(cli_color_py.yellow("This isn't a valid choice, please try again!"))
        
def delete_employee(employee):
    add_space()
    print(cli_color_py.yellow("Are you sure you want to delete this employee? Enter 'y' for yes or 'n' for no"))
    choice = input(">")
    if choice == "y" or choice == "Y":
        reassign_orders(employee)
        employee.delete()
        print(f"{employee.first_name} {employee.last_name} has been removed from the system.")
        return
    
    else:
        add_space()
        print(cli_color_py.red("There was an issue removing this employee!"))
        return

def space_and_border():
    print("")
    print('/'* 20)
    print("")

def add_space():
    print("")

def exit_program():
    space_and_border()
    print(cli_color_py.green("Now closing the system, thank you for your hard work!"))
    print(cli_color_py.green("Goodbye!"))
    exit()
