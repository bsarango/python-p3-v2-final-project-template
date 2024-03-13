# Phase 3 Hospital Order Management System Program 

## Project Description

This program is a simple hospital management system intended for a nursing or shift manager or supervisor to insert employee and order data as well as retrieve existing or previously added data. The program accepts inputs and shows data via a CLI. It manipulates and holds data that is inserted or retrieved via models for employees and orders in python. All the data that is stored or retreived is done in a database for the hospital. 

## Project Installation and Setup

To access the repository for this project, click the following link.

https://github.com/bsarango/python-p3-v2-final-project-template

To fork the Repo to your system, click on the green Code button and click on the double boxed icon next to the provided link. 

Once copied, open your terminal and enter the directory you want to clone the Repo into. Enter the following to clone the Repo

```console
git clone https://github.com/bsarango/python-p3-v2-final-project-template
```

Once cloned, enter the cloned directory. Inside the newly cloned directory, enter the following to install all the files from pipfile and set up the pipenv.

```console
pipenv install
```

Enter the following to create the virtual environment to run the program

```console
pipenv shell
```

Once the virtual environement is successfully set up, enter the following to start the program.

```
python lib/cli.py
```

Upon entering this in the console, the program will start with a greeting to the user and give a menu with options to select from for an input


## Program Contents
The program contains several files for the CLI, __init__.py to set up the database and create a connection to the code, a file for helper functions that are called in the CLI file, and models for employee and order classes.

The cli.py file is where the main logic and interaction with the user occurs. The user is given menu options to select from when then calls other functions to perform those tasks. The file imports the employee, order, several helper functions, and cli_color_py. Employee and order are models used in the functions and helpers and cli_color_py is a module used to display colored text - it used to display success, warning, errors or failures, and startup/exit messages.

The helpers.py file imports the employee and order models to use these respective objects in the files functions and the cli_color_py module to give color to success, warning, error, or startup/exit messages to the user. Helpers.py contains several helper functions that are called in cli.py functions or within other helper functions. 

The models folder contains the models for employee, orders, and the connection to the database.

The __init__.py file creates and establishes the connection to the hospital.db database where data is store tables for employees and orders created in the program.

The employee.py model contains the code for the Employee class as well as attributes and methods for creating, updating, deleting, saving, and retrieving data to and from the database as well as the __init__ for instantiating instances of the class.

The order.py model contains the code for the Order class as well as attributes and methods for creating, updating, deleting, saving, and retrieving data to and from the database as well as the __init__ for instantiating instances of the class.



