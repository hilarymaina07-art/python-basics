# IF ELIF ELSE STATEMENT
# It allows you to check several conditions.
marks = 75

if marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 50:
    print("Grade D")

else:
    print("Grade E")
    

# NESTED IF STATEMENT
# A nested if is an if statement inside another if statement.

age = 22
has_id = True

if age >= 18:

    if has_id:
        print("You can enter")

    else:
        print("You need an ID")

else:
    print("You are underage")
    

# Logical operators combine conditions.
age = 22
has_id = True

if age >= 18 and has_id:
    print("Requirements met")

if age >= 18 or has_id:
    print("At least one condition is true")

if not has_id:
    print("ID is missing")
    
# and – Both conditions must be true.
#or – At least one condition must be true.
#not – Reverses the result.
    
# which number is greater

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")

elif num1 < num2:
    print("Second number is greater")

else:
    print("Both numbers are equal")
   
# check even or odd numbers

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("This is an even number")

else:
    print("This is an odd number")

# The % operator gives the remainder after division.

#For example:
# 8 % 2 = 0 (even)
#7 % 2 = 1 (odd)

# Comparison operators
#Operator	Meaning	Example
#==	Equal to	5 == 5
#!=	Not equal to	5 != 3
#>	Greater than	8 > 4
#<	Less than	3 < 7
#>=	Greater than or equal to	5 >= 5
#<=	Less than or equal to	4 <= 6

