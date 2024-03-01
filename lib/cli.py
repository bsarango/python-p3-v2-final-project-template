# lib/cli.py

from helpers import (
    exit_program,
    list_employees,
    employees_menu,
    orders_menu 
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "e" or choice == "E":
            employees_menu()
        elif choice =="o" or choice == "O":
            orders_menu()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("e. Display all the employees")
    print("o, Display all orders")


if __name__ == "__main__":
    main()
