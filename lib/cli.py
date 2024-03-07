# lib/cli.py

from helpers import (
    exit_program, 
    space_and_border
)

def welcome():
    print("Welcome, now starting your system!")

def main():
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
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("e. Display all the employees")
    print("o, Display all orders")
    space_and_border()


def orders():
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
            print("That isn't a valid choice. Please choose again!")

def orders_menu():
    print("Select on of the following options:")
    print("Enter the number for the respective order")
    print("Enter b to go back")
    print("Enter 0 to exit the program")      

def employees():
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
        elif choice == "b" or choice == "B":
            print("Returning to the Main Menu")
            return 
        elif int(choice) > 0 and int(choice)<=len(employees):
            employee_options(employees[int(choice)-1])
        else:
            print("That isn't a valid choice. Please choose again!")   

def employees_menu():
    print("Select one of the following:")
    print("Enter an Employee by their respective number:")
    print("Enter e to enter an employee to the system:")
    print("Enter b to return to the main menu:")

if __name__ == "__main__":
    welcome()
    main()
