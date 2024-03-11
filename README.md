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


---

## Program Contents
The program contains several files the CLI, setting up the database, helper functions that are called in the CLI file, and models for employee and order objects.

The cli.py file has the if __name__ == "__main__": block that starts the program and initiates the call to the functions in that block. The first call is to a greeting function to give a welcome to the user. Its followed by calling main() that displays the first menu and options by calling the menu(). Once one of the options is selected, it will proceed to call either the employees() and employees_menu() or orders() and orders_menu() and display all of employees or orders and options for viewing or managing them. Selection of the options calls functions from the helpers file to carry out further actions. There is also the option to go back to the previous menu or exit the program completely. The choice to exit provides teh user a message before exiting out of the program and returning the user to the console.

The cli.py file imports the employee, order, several helper functions, and cli_color_py. Employee and order are models used in the functions and helpers and cli_color_py is a module used to display colored text - it used to display success, warning, errors or failures, and startup/exit messages.

The helpers.py file imports the employee and order models to use these respective objects in the files functions and the cli_color_py module to give color to success, warning, error, or startup/exit messages to the user. Helpers.py contains several helper functions that are called in cli.py functions or within other helper functions. 

In helpers.py, list_employees() and list_orders() display all of the employee or order instances, by title or name only, via enumeration from the passed argument. The create_order() recieved user input for the data needed to create an order object. The object's data is verified via try and execpt statements when using the class method .create for Order





## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
