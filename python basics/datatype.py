
# INTEGER DATA TYPE(int)
# An integer is a whole number without a decimal point.
age = 22
number = 100
year = 2026

print(age)
print(number)
print(year)

print(type(age))


# FLOAT DATA TYPE(float)
# A float is a number that contains a decimal point.
price = 250.50
height = 5.8
temperature = 36.5

print(price)
print(height)
print(temperature)

print(type(price))


# STRING DATA TYPE(str)
# A string stores text. It is written inside quotation marks.

name = "Hilary"
country = "Kenya"
course = "Python Programming"

print(name)
print(country)
print(course)

print(type(name))


# BOOLEAN DATA TYPE(bool)
# A Boolean stores only two possible values:
#- True
#- False

is_student = True
is_employed = False

print(is_student)
print(is_employed)

print(type(is_student))


# NONE DATA TYPE
# None represents the absence of a value.

result = None

print(result)

print(type(result))


# Summary of Python data types
#Data type	Example	            Description
#int	      age = 22	        Whole numbers
#float	      price = 20.50	    Decimal numbers
#str	      name = "Hilary"	    Text
#bool	      is_valid = True	True or False
#list	      [1, 2, 3]	        Changeable collection
#tuple	      (1, 2, 3)	        Unchangeable collection
#set	      {1, 2, 3}	        Unique values
#dict	      {"age": 22}	    Key-value pairs
#NoneType	  x = None	        No 


# STUDENT INFORMATION SYSTEM

name = "Hilary"
age = 22
marks = 85.5
is_student = True

subjects = ["Python", "HTML", "CSS"]

student = {
    "name": name,
    "age": age,
    "marks": marks,
    "is_student": is_student
}

print("--- STUDENT INFORMATION ---")

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Student:", is_student)
print("Subjects:", subjects)

print("\n--- CHECKING DATA TYPES ---")

print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))
print(type(subjects))
print(type(student))
