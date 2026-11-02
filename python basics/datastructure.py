
# LIST DATA STRUCTURE
# A list stores multiple items in one variable.
#- Uses square brackets [].
#- Allows duplicate values.
#- Can be changed (mutable).
#- Maintains order.

students = ["Erick", "Cherop", "Mary", "John"]

# Display all students
print(students)

# Access one student
print(students[0])

# Add a new student
students.append("Hilary")

# Remove a student
students.remove("John")

# Change a student name
students[1] = "Peter"

print(students)


# TUPLE DATA STRUCTURE
# A tuple stores multiple items, just like a list, but it cannot be changed after creation.
#- Uses parentheses ().
#- Allows duplicates.
#- Maintains order.
#- Cannot be modified (immutable).

students = ("Erick", "Cherop", "Mary", "John")

# Display all students
print(students)

# Access an item
print(students[1])

# Count items
print(len(students))


# SET DATA STRUCTURE
# A set stores unique items. It automatically removes duplicates.
#- Uses curly brackets {}.
#- Does not allow duplicate values.
#- Does not maintain a guaranteed order.
#- You can add and remove items.

students ={"Erick", "Cherop", "Mary", "Erick"}

# Display students
print(students)

# Add a new student
students.add("John")

# Remove a student
students.remove("Mary")

print(students)


# DICTIONARY DATA STRUCTURE
# A dictionary stores information in key-value pairs.
#- Uses curly brackets {}.
#- Stores data as key-value pairs.
#- Keys must be unique.
#- Values can be changed.

    
student = {
    "name": "Erick",
    "age": 22,
    "course": "Python",
    "county": "Nairobi"
}

# Access information
print(student["name"])
print(student["age"])

# Add new information
student["gender"] = "Male"

# Change information
student["age"] = 23

# Display all information
print(student)


# STRING DATA TYPE
# A string stores text. It is written inside quotation marks.

name = "Erick"

print(name)

# Access a character
print(name[0])

# Find the length
print(len(name))

# Convert to uppercase
print(name.upper())

#Summary: Comparing the data structures
#Structure	Brackets	Changeable?	Duplicates?
#List	     []	           Yes	    Yes
#Tuple	     ()	           No	    Yes
#Set	     {}            Yes	    No
#Dictionary	 {key:value}   Yes	    Keys are unique
#String	     ""	           No	    Yes