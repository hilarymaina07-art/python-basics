
# FOR LOOP
# A for loop is used when you want to repeat something over a sequence of items or a specified range.

for number in range(1, 6):
    print(number)

# Explanation:
# for starts the loop.
# number is the variable that stores each number.
# range(1, 6) generates numbers from 1 to 5.
# print(number) displays each number.


# LOOPING THROUGH A LIST

students = ["Erick", "Cherop", "Mary", "John"]

for student in students:
    print(student)


# WHILE LOOP
# A while loop repeats code as long as a condition remains true.
number = 1

while number <= 5:
    print(number)
    number += 1
    
# Explanation:
#- Start with number = 1.
#- Check whether number <= 5.
#- If true, print the number.
#- Increase the number by 1.
#- Stop when the condition becomes false.


# BREAK STATEMENT
# break stops a loop immediately.

for number in range(1, 10):

    if number == 5:
        break

    print(number)
    
# CONTINUE STATEMENT
# continue skips the current iteration and moves to the next one.

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# NESTED LOOPS
# A nested loop is a loop inside another loop.
for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)
        

# MULTIPLICATION TABLE

number = int(input("Enter a number: "))

for i in range(1, 11):

    result = number * i

    print(number, "x", i, "=", result)


# FINDING EVEN NUMBERS

for number in range(1, 21):

    if number % 2 == 0:

        print(number, "is even")


# STUDENT LIST

students = ["Erick", "Cherop", "Mary", "John"]

for index, student in enumerate(students, start=1):

    print("Student", index, ":", student)


# 10. Summary of Python loops
# Loop	Purpose
# for	Repeats through a sequence
# while	Repeats while a condition is true
# break	Stops the loop
# continue	Skips an iteration
# Nested loop	A loop inside another loop


# MY SHOPPING LIST

shopping_list = ["Milk", "Bread", "Sugar", "Rice", "Cooking oil"]

print("--- MY SHOPPING LIST ---")

for item in shopping_list:
    print(item)


# SHOPPING LIST PROGRAM

shopping_list = []

while True:

    item = input("Enter a shopping item (or type done to finish): ")

    if item.lower() == "done":
        break

    shopping_list.append(item)

print("\n--- YOUR SHOPPING LIST ---")

for item in shopping_list:
    print(item)

print("Total items:", len(shopping_list))


# How it works:
#1. shopping_list = [] creates an empty list.
#2. while True keeps the program running.
#3. input() collects shopping items.
#4. if item.lower() == "done" checks whether the user wants to finish.
#5. break stops the loop.
#6. append() adds an item to the list.
#7. for displays all the items.
#8. len() counts the items.


# SHOPPING LIST WITH PRICES

shopping_list = []

while True:

    item = input("Enter item name (or done to finish): ")

    if item.lower() == "done":
        break

    price = float(input("Enter item price in KSh: "))

    shopping_list.append({
        "name": item,
        "price": price
    })

# Display shopping list

print("\n--- SHOPPING RECEIPT ---")

total = 0

for item in shopping_list:

    print(item["name"], "- KSh", item["price"])

    total += item["price"]

print("----------------------")
print("Total cost: KSh", total)


# Allow the user to remove an item.



# Display the number of items.



# Calculate the total shopping cost.



# Display the most expensive item.