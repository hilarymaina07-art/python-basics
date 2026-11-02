# arithmetic operators (+,-,*,/,%)
a=7
b=2
c=a+b
d=a-b

# comparison orerator(==,!='<=,>=,<,>)
e=8
f=89
print(e == f)       #equal to
print(e != f)       #not equal to
print(e > f)        #greater than



# ARITHMETIC OPERATORS

num1 = 10
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % 3)
print("Floor division:", num1 // 3)
print("Power:", num1 ** 2)


# ASSIGNMENT OPERATORS
# Operator	Meaning
#=	Assign
#+=	Add and assign
#-=	Subtract and assign
#*=	Multiply and assign
#/=	Divide and assign
#%=	Modulus and assign

number = 10

number += 5
print("After addition:", number)

number -= 3
print("After subtraction:", number)

number *= 2
print("After multiplication:", number)

number /= 4
print("After division:", number)


# COMPARISON OPERATORS
# Operator	Meaning
# ==	Equal to
# !=	Not equal to
# >	Greater than
# <	Less than
# >=	Greater than or equal to
# <=	Less than or equal to

a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# LOGICAL OPERATORS
#There are three main logical operators:
#- and – Both conditions must be true.
#- or – At least one condition must be true.
#- not – Reverses the result.

age = 22
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)


# MEMBERSHIP OPERATORS
# There are two:
# - in – Checks whether an item exists.
# -not in – Checks whether an item does not exist.

students =["Erick", "Cherop", "Mary", "John"]

print("Erick" in students)

print("Peter" not in students)

print("Mary" in students)



# IDENTITY OPERATORS
#There are two:
#- is
#- is not

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a is not c)


# BITWISE OPERATORS
#These operators work on the binary representation of integers (numbers represented using 0s and 1s).

#| Operator | Meaning |
#|---|---|
#| & | AND |
#| | | OR |
#| ^ | XOR |
#| ~ | NOT |
# << | Left shift |
#| >> | Right shift |
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)


# PYTHON SIMPLE CALCULATOR

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- CALCULATOR ---")

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero")

print("Modulus:", num1 % num2 if num2 != 0 else "Undefined")
print("Power:", num1 ** num2)

# Summary of Python operators
# Category	     Operators
# Arithmetic	+ - * / % // **
# Assignment	= += -= *= /= %=
# Comparison	== != > < >= <=
# Logical	    and or not
# Membership	in, not in
# Identity	    is, is not
# Bitwise	    & \| ^ ~ << >>