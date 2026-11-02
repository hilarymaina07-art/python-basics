# VARIABLE
# A variable is a container used to store information in a program.

x = 5
y = "Hello, world!"
print(x)
print(y)

# Different types of variables

# STRING VARIABLE
name = "Hilary"

# INTEGER VARIABLE
age = 22

# FLOAT VARIABLE
price = 250.50

# BOOLEAN VARIABLE
is_student = True

# DISPLAY VARIABLES
print(name)
print(age)
print(price)
print(is_student)

#changing variables

age = 22

print("Original age:", age)

age = 25

print("New age:", age)

# Variable naming rules
# Python has rules when naming variables.

# Rule	                          Correct example
# Start with a letter	            name = "Hilary"
# Can start with underscore  	    _age = 22
# Can contain numbers	            student1 = "Hilary"
# No spaces                     	student_name = "Hilary"
# Cannot start with a number	    age2 = 22


# Mathematical operations

num1 = 20
num2 = 10

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)



# Collecting user information

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Your name is:", name)
print("Your age is:", age)



# STUDENT INFORMATION SYSTEM

# Variables
name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course: ")
marks = float(input("Enter student marks: "))

# Display student details
print("\n--- STUDENT DETAILS ---")

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)

# Check data types
print("\n--- DATA TYPES ---")

print(type(name))
print(type(age))
print(type(course))
print(type(marks))
