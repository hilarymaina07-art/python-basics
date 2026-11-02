# Defining a function
def greet():
    print("Hello! Welcome to Python.")

# Calling the function
greet()

# Explanation
#def tells Python that you are creating a function.
#greet is the function name.
#() holds any information the function may need.
#: starts the function body.
#greet() calls or runs the function.

# Parameters
# Parameters allow you to pass information into a function.

# adding two numbers
def greet(name):
    print("Hello", name)

greet("Hilary")
greet("John")
greet("Mary")

def add_numbers(num1, num2):
    result = num1 + num2
    print("The sum is:", result)

add_numbers(10, 20)
add_numbers(5, 15)

# using return
def multiply(num1, num2):
    return num1 * num2

answer = multiply(5, 4)

print("The answer is:", answer)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

# Task: Create a function called calculate_age that:
#1. Accepts a person's birth year.
#2. Calculates their age using the current year, 2026.
#3. Returns the age.
#4. Prints the result.

from datetime import date
def calculate_age(birth_year):
    current_year = date.today().year
    age = current_year - birth_year
    return age
year = int(input("Enter your birth year: "))

print("Your age is:", calculate_age(year))

