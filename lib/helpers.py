# lib/helpers.py
from models.employee import Employee
from models.order import Order

def list_employees(employees):
    for count, ele in enumerate(employees, start=1):
        print(count,": ",ele.first_name, " ",ele.last_name)
    

def list_orders(orders):
    for count, ele in enumerate(orders, start=1):
        print(count,": ",ele.title)

def create_order(_id):
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
        print(f"Order placed!")

    except Exception as exec:
        print("Failed to create an order. Try again.")

def delete_order(order):
    print("Are you sure you want to delete this order? Enter y or n")
    choice = input(">")
    if choice == "y" or choice == "Y":
        order.delete()
        print(f"The {employee.first_name} order has been removed.")
        return
    
    else:
        print("There was an issue removing this order!")

def update_order(order):
    print("Enter d to update the ordering doctor")
    print("Enter c to mark as completed")

    choice = input(">")

    if choice == "d":
        new_doctor = input("Enter the new doctor: ")
        order.ordering_doctor = new_doctor
        order.save()
        print("The ordering doctor has been updated!")

    elif choice == "c":
        if order.completed == 1:
            print("The order is already completed")
        else:
            order.completed = 1
            print("The order now has a completed status!")
    
    else:
        print("This isn't a valid choice, please try again!")
    

def manage_employee_orders(employee_orders, employee_id):

    while True:
        print("Do you wish to add or manage an order?")
        print("Enter a to add an order")
        print("Enter the number of the order to manage the order")
        print("Enter b to go back to the previous menu")

        choice = input(">")

        if choice == "a" or choice =="A":
            create_order(employee_id)
        elif choice == "b" or choice == "B":
            print("Returning to the previous menu")
            return
        elif int(choice) > 0 and int(choice)<= len(employee_orders):
            order_submenu(employee_orders[int(choice)-1])
        else:
            print("This isn't a valid choice, please try again!")
        
def display_order_info(order):
    print("Order details:")
    print(f"Title: {order.title}")
    print(f"Ordering Doctor: {order.ordering_doctor}")
    if order.completed == 1:
        print(f"Completion Status: Completed")
    else:
        print(f"Completion Status: Not Completed")
    print(f"Order issue time and date: {order.time_stamp}")

def display_employee_info(employee):
    print(f"You are currently viewing {employee.first_name} {employee.last_name}'s profile. Do you wish to perform any actions?")
    print(f"First name: {employee.first_name}")
    print(f"Last name: {employee.last_name}")
    print(f"Position: {employee.job_title}")
    print(f"Department: {employee.department}")

def create_employee():
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
            print("There was an error in entering the new employee's info into the system. Try again.", exec) 
    
    elif choice == "n" or choice == 'N':
        print("Returning to the previous menu")
        return

    else:
        print("This isn't a valid choice, please try again!")

def update_employee(employee):
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
            print(f"There was an error updating {employee.first_name} {employee.last}'s profile.", exec)
    
    elif choice == 'n' or choice == 'N':
        print("Returning to the previous menu")
        return

    else:
        print("This isn't a valid choice, please try again!")
        
def delete_employee(employee):
    print("Are you sure you want to delete this employee? Enter 'y' for yes or 'n' for no")
    choice = input(">")
    if choice == "y" or choice == "Y":
        employee.delete()
        print(f"{employee.first_name} {employee.last_name} has been removed from the system.")
        return
    
    else:
        print("There was an issue removing this employee!")
    
def employees_menu():
    while True:
        employees = Employee.get_all()
        print("Your current employees:")
        list_employees(employees)
        choice = (input("Select one of the employees by selecting the number next to them, enter 'e' to enter a new employee's info, 'b' to return to the Main Menu, or 0 to exit: "))

        if choice == "0":
            exit_program()
        elif choice == "e" or choice == 'E':
            create_employee()
        elif choice == "b" or choice == "B":
            print("Returning to the Main Menu")
            return 
        elif int(choice) > 0 and int(choice)<=len(employees):
            employee_submenu(employees[int(choice)-1])
        else:
            print("That isn't a valid choice. Please choose again!")

def employee_submenu(employee):
    display_employee_info(employee)

    while True:
        print(f"Enter o to view all the orders for {employee.first_name} {employee.last_name}")
        print(f"Enter u to update {employee.first_name} {employee.last_name} information")
        print(f"Enter d to delete {employee.first_name} {employee.last_name}'s profile")
        print("Enter b to go back to the previous menu")
        print("Enter 0 to exit the program")

        choice = input(">")
        if choice == "o" or choice == "O":
            current_employee_orders = employee.orders()
            list_orders(current_employee_orders)
            manage_employee_orders(current_employee_orders,employee.id)

        elif choice == "u" or choice == "U":
            update_employee(employee)
        elif choice == "d" or choice == "D":
            delete_employee(employee)
            return
        elif choice == "b" or choice == "B":
            print("Returning to the Previous Menu")
            return
        elif choice == "0":
            exit_program()
        else:
            print("That isn't a valid choice. Please choose again!")

def orders_menu():
    while True:
        orders = Order.get_all()
        print("All current orders: ")
        list_orders(orders)
        print("Select one of the orders by the number next to it to view it's details, select b to go back, or 0 to exit")
        choice = input("> ")

        if choice == "0":
            exit_program()
        elif choice == "b" or choice == "B":
            print("Returning to the Main Menu")
            return 
        elif int(choice) > 0 and int(choice)<=len(orders):
            order_submenu(orders[int(choice)-1])
        else:
            print("That isn't a valid choice. Please choose again!")

def order_submenu(order):
    while True:
        display_order_info(order)
        print("Enter u to update this order")
        print("Enter d to delete this order")
        print("Enter b to go back to the previous menu")
        print("Enter 0 to exit the program")

        choice = input(">")

        if choice == "u" or choice == "U":
            update_order(order)
        elif choice == "d" or choice == "D":
            delete_order(order)
        elif choice == "b" or choice == "B":
            "Returning to the Previous Menu"
            return
        elif choice == "0":
            exit_program()
        else:
            print("That isn't a valid choice. Please choose again!")

def exit_program():
    print("Goodbye!")
    exit()
