
# Creating a class
##class Student:
   # name = "Erick"
   # age = 22

# Creating an object
#student1 = Student()

# Displaying student information
#print(f"Name of student: {student1.name}")
#print(f"Age of student: {student1.age}")


#lass Student:

   # def __init__(self, name, age):
       # self.name = name
      #  self.age = age


# Creating objects
#student1 = Student("Erick", 22)
#student2 = Student("Cherop", 19)

# Displaying student details
#print(student1.name)
#print(student1.age)

#print(student2.name)
#print(student2.age)


from abc import ABC, abstractmethod

# ==================================
# 1. ABSTRACTION
# ==================================

class MpesaPayment(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass


# ==================================
# 2. CLASS AND ENCAPSULATION
# ==================================

class MpesaAccount(MpesaPayment):

    def __init__(self, name, phone, balance):
        self.name = name
        self.phone = phone
        self.__balance = balance

    # Check account balance
    def check_balance(self):
        return self.__balance

    # Deposit money
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")

        else:
            print("Invalid deposit amount!")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount!")

        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")

        else:
            print("Insufficient balance!")

    # Send money to another customer
    def send_money(self, receiver, amount):

        if not isinstance(receiver, MpesaAccount):
            print("Invalid receiver!")

        elif amount <= 0:
            print("Invalid amount!")

        elif amount > self.__balance:
            print("Insufficient balance!")

        else:
            self.__balance -= amount
            receiver.deposit(amount)

            print(f"Ksh {amount} sent to {receiver.name}")

    # Implement abstract payment method
    def make_payment(self, amount):
        self.withdraw(amount)


# ==================================
# 3. INHERITANCE
# ==================================

class CustomerAccount(MpesaAccount):

    def account_type(self):
        print("Personal M-PESA Account")


class BusinessAccount(MpesaAccount):

    def account_type(self):
        print("Business M-PESA Account")


# ==================================
# 4. CREATING OBJECTS
# ==================================

eric = CustomerAccount("Eric", "0712345678", 5000)

john = CustomerAccount("John", "0723456789", 3000)

shop = BusinessAccount("Eric Shop", "0734567890", 10000)


# ==================================
# 5. POLYMORPHISM
# ==================================

eric.account_type()
shop.account_type()


# ==================================
# 6. DISPLAY CUSTOMER INFORMATION
# ==================================

print("\n--- M-PESA SYSTEM ---")

print("Customer:", eric.name)
print("Phone:", eric.phone)
print("Balance:", eric.check_balance())


# ==================================
# 7. DEPOSIT
# ==================================

print("\n--- DEPOSIT ---")

eric.deposit(2000)


# ==================================
# 8. WITHDRAWAL
# ==================================

print("\n--- WITHDRAW ---")

eric.withdraw(1000)


# ==================================
# 9. SEND MONEY
# ==================================

print("\n--- SEND MONEY ---")

eric.send_money(john, 1500)


# ==================================
# 10. MAKE PAYMENT
# ==================================

print("\n--- PAYMENT ---")

eric.make_payment(500)


# ==================================
# 11. DISPLAY FINAL BALANCES
# ==================================

print("\n--- FINAL BALANCES ---")

print("Eric:", eric.check_balance())
print("John:", john.check_balance())
print("Shop:", shop.check_balance())

#1. Encapsulation – Keeping information safe
#  means keeping data and the functions that work with that data together in one class, while controlling how the data is accessed or changed.

#Example: M-Pesa account

#You have money in your M-Pesa account. You should not be able to change your balance anyhow. You use specific actions such as depositing or withdrawing.
class Mpesa:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def check_balance(self):
        return self.__balance


account = Mpesa(1000)

account.deposit(500)

print(account.check_balance())

# – Receiving features from another class
# Inheritance means one class can receive properties and methods from another class.

# Example:

# A parent has certain characteristics that a child can inherit.
class Animal:
    def eat(self):
        print("This animal eats food")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


my_dog = Dog()

my_dog.eat()
my_dog.bark()

# Polymorphism – One action, different behaviours
# Polymorphism means different classes can use the same method name but perform different actions.

#Example:
# Different animals make different sounds.
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


class Cow:
    def sound(self):
        print("Cow moos")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
    
#  Abstraction – Hiding complicated details
# Abstraction means showing only what someone needs to use while hiding the complicated internal details.

#Example:
# When you withdraw money from an ATM, you enter your PIN and amount. You don't need to understand all the internal processes.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class Mpesa(Payment):

    def pay(self, amount):
        print("Paid using M-Pesa:", amount)


payment = Mpesa()
payment.pay(500)

# Summary: The four pillars of OOP
#1. Encapsulation
# Protecting data.

#Example: M-Pesa balance.


#. Inheritance
#Receiving features from another class.

#Example: Dog inherits from Animal.


#3. Polymorphism
#Same method, different behaviours.

#Example: Animals making different sounds.

#4. Abstraction
#Hiding complicated details.

#Example: Using an ATM.