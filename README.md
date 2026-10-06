# OOP_coffee_machine
Coffee Machine

A command-line coffee machine simulation built with Python using object-oriented programming.

The program allows users to order different coffee drinks, checks whether enough ingredients are available, processes coin payments, calculates change, and updates the machine's resources.

Available Drinks
Espresso
Latte
Cappuccino

Features
Displays available coffee options
Checks available machine resources
Processes coin payments
Calculates and returns change
Tracks machine profit
Updates ingredients after making a drink
Displays resource and money reports
Supports shutting down the machine with the off command

Technologies
Python
Object-Oriented Programming (OOP)
Python Concepts Practiced
Classes and objects
Methods
Attributes
Dictionaries
Loops
Conditional statements
Importing modules
Working with multiple Python files
Project Structure
coffee-machine/
│
├── main.py
├── coffee_maker.py
├── menu.py
└── money_machine.py
main.py

Controls the main program and user interaction.

coffee_maker.py

Manages the coffee machine resources and prepares drinks.

menu.py

Stores the available drinks and their required ingredients.

money_machine.py

Processes coin payments, calculates change, and tracks profit.

How to Run

Make sure all four Python files are located in the same directory.

Then run:

python main.py

You can enter:

espresso
latte
cappuccino
report
off

Purpose

This project was created to practice object-oriented programming and understand how a larger Python program can be divided into multiple classes and modules.

Possible Future Improvements
Add more drink options
Improve user input validation
Add support for additional payment methods
Create a graphical user interface
Save machine statistics between sessions
