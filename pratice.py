#1
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

#
# s1 = Student("Somaraju", 21, 85)
# s1.display_details()

#2
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Updated Balance:", self.balance)


# a1 = BankAccount("Somaraju", 5000)
# a1.deposit(2000)

#3
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def increment_salary(self, amount):
        self.salary += amount
        print("Updated Salary:", self.salary)


# e1 = Employee(101, "Somaraju", 30000)
# e1.increment_salary(5000)


#4
class Employee:
    company = "Infosys"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


# print(Employee.company)
#
# Employee.change_company("TCS")
#
# print(Employee.company)


#5
class Bank:
    bank_name = "SBI"

    @classmethod
    def change_bank(cls, new_bank):
        cls.bank_name = new_bank


# print(Bank.bank_name)
#
# Bank.change_bank("HDFC")
#
# print(Bank.bank_name)


#6
class Hospital:
    hospital_name = "City Hospital"

    @classmethod
    def change_hospital(cls, new_name):
        cls.hospital_name = new_name


# print(Hospital.hospital_name)
#
# Hospital.change_hospital("Apollo Hospital")
#
# print(Hospital.hospital_name)

#7
class Voting:
    @staticmethod
    def is_eligible(age):
        if age >= 18:
            print("Eligible to Vote")
        else:
            print("Not Eligible")


# Voting.is_eligible(20)
# Voting.is_eligible(16)

#8

class MovieTicket:
    @staticmethod
    def ticket_price(age):
        if age < 12:
            return 100
        elif age <= 60:
            return 200
        else:
            return 150


# print(MovieTicket.ticket_price(10))
# print(MovieTicket.ticket_price(25))
# print(MovieTicket.ticket_price(65))

#9
class DeliveryService:
    @staticmethod
    def delivery_charge(amount):
        if amount >= 500:
            return 0
        else:
            return 50


print(DeliveryService.delivery_charge(600))
print(DeliveryService.delivery_charge(300))