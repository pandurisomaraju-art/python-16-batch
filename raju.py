#1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40


s1 = Student("Rahul", 75)
s2 = Student("Ravi", 35)

print(s1.name, "Passed" if s1.is_passed() else "Failed")
print(s2.name, "Passed" if s2.is_passed() else "Failed")
#2
class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


e1 = Employee("Rahul")
e2 = Employee("Ravi")

print(e1.company_name)
print(e2.company_name)

Employee.change_company("Infosys")

print(e1.company_name)
print(e2.company_name)
#3
class MathOps:

    @staticmethod
    def is_even(num):
        return num % 2 == 0


print(MathOps.is_even(8))

obj = MathOps()
print(obj.is_even(7))
#4
class Car:
    wheels = 4

    def __init__(self, mileage):
        self.mileage = mileage

    def display_specs(self):
        print("Mileage:", self.mileage)
        print("Wheels:", Car.wheels)

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels


c1 = Car(20)

c1.display_specs()

Car.change_wheels(6)

c1.display_specs()
#5
class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def show_conversion(self):
        print("Celsius:", self.celsius)
        print("Fahrenheit:", Temperature.to_fahrenheit(self.celsius))


t = Temperature(30)
t.show_conversion()
#6
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3


if Book.is_valid_title("Python"):
    b1 = Book("Python", "Guido")

if Book.is_valid_title("Java"):
    b2 = Book.from_string("Java-James")

print(b1.title, b1.author)
print(b2.title, b2.author)

print("Total Books:", Book.total_books)
#7
class Employee:
    bonus_rate = 0.1

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def final_salary(self):
        return self.base_salary + (self.base_salary * Employee.bonus_rate)

    @classmethod
    def update_bonus(cls, new_rate):
        cls.bonus_rate = new_rate

    @staticmethod
    def is_valid_salary(sal):
        return sal > 0


if Employee.is_valid_salary(50000):
    e1 = Employee("Rahul", 50000)

if Employee.is_valid_salary(40000):
    e2 = Employee("Ravi", 40000)

print(e1.final_salary())
print(e2.final_salary())

Employee.update_bonus(0.2)

print(e1.final_salary())
print(e2.final_salary())
#8
class Course:
    total_students = 0

    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self):
        Course.total_students += 1

    @classmethod
    def show_total(cls):
        print("Total Students:", cls.total_students)

    @staticmethod
    def is_eligible(age):
        return age >= 18


s1 = Course("Rahul")
s2 = Course("Ravi")

if Course.is_eligible(20):
    s1.enroll()

if Course.is_eligible(19):
    s2.enroll()

Course.show_total()
#9
class BankAccount:
    bank_name = "SBI"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print("New Balance:", self.balance)
        else:
            print("Invalid Amount")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0


acc = BankAccount("Rahul", 1000)

acc.deposit(500)

print(BankAccount.bank_name)

BankAccount.change_bank_name("IOB")

print(BankAccount.bank_name)
#10
class Student:
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")

    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks

    @staticmethod
    def grade_category(marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"


s1 = Student("Rahul", 85)
s2 = Student("Ravi", 55)

print(Student.grade_category(s1.marks))
print(Student.grade_category(s2.marks))

s1.result()
s2.result()

Student.update_passing_marks(60)

print("\nAfter Updating Passing Marks")

s1.result()
s2.result()