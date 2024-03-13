# lib/cli.py
import cli_color_py
from models.employee import Employee
from models.order import Order
from helpers import (
    exit_program, 
    space_and_border,
    list_employees,
    list_orders,
    create_employee,
    order_options,
    add_space
)

def welcome():
    print(cli_color_py.green("Welcome and thank you for using our system \nNow starting your system!"))
    print(cli_color_py.green("Please read and follow prompts to navigate menus and select options for your employees or orders"))


def main():
    space_and_border()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "e" or choice == "E":
            employees()
        elif choice =="o" or choice == "O":
            orders()
        else:
            print(cli_color_py.yellow("Invalid choice"))


def menu():
    add_space()
    print("Please select an option:")
    print("0. Exit the program")
    print("e. Display all the employees")
    print("o. Display all orders")


def orders():
    space_and_border()
    while True:
        orders = Order.get_all()
        print("All current orders: ")
        list_orders(orders)
        orders_menu()

        choice = input("> ")

        if choice == "0":
            exit_program()
        elif choice == "b" or choice == "B":
            print("Returning to the Main Menu")
            return 
        elif int(choice) > 0 and int(choice)<=len(orders):
            order_options(orders[int(choice)-1])
        else:
            print(cli_color_py.yellow("That isn't a valid choice. Please choose again!"))

def orders_menu():
    add_space()
    print("Select one of the following options:")
    print("Enter the number for the respective order")
    print("Enter b to go back")
    print("Enter 0 to exit the program")      

def employees():
    space_and_border()
    while True:
        employees = Employee.get_all()
        print("Your current employees:")
        list_employees(employees)
        employees_menu()
        choice = input("> ")

        if choice == "0":
            exit_program()
        elif choice == "e" or choice == 'E':
            create_employee()
            add_space()
        elif choice == "b" or choice == "B":
            print("Returning to the Main Menu")
            return 
        elif int(choice) > 0 and int(choice)<=len(employees):
            employee_options(employees[int(choice)-1])
        else:
            print(cli_color_py.yellow("That isn't a valid choice. Please choose again!"))   

def employees_menu():
    add_space()
    print("Select one of the following:")
    print("Enter an Employee by their respective number:")
    print("Enter e to enter an employee to the system:")
    print("Enter b to return to the main menu:")

def employee_options(employee):
    while True:
        add_space()
        display_employee_info(employee)
        employee_options_menu(employee)

        choice = input(">")
        if choice == "o" or choice == "O":
            space_and_border()
            current_employee_orders = employee.orders()
            list_orders(current_employee_orders)
            manage_employee_orders(employee)

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
            print(cli_color_py.yellow("That isn't a valid choice. Please choose again!"))

def employee_options_menu(employee):
    add_space()
    print(f"Enter o to view all the orders for {employee.first_name} {employee.last_name}")
    print(f"Enter u to update {employee.first_name} {employee.last_name} information")
    print(f"Enter d to delete {employee.first_name} {employee.last_name}'s profile")
    print("Enter b to go back to the previous menu")
    print("Enter 0 to exit the program")

if __name__ == "__main__":
    welcome()
    main()
