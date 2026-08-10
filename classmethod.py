1 first
class Student:
    total_students = 0
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def result(self):
        if self.marks >= Student.passing_marks:
            return "Passed"
        return "Failed"

    @classmethod
    def curve_marks(cls, percentage):
        cls.curve = percentage

    def apply_curve(self):
        self.marks += self.marks * Student.curve / 100

    @staticmethod
    def letter_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"


s1 = Student("Ram", 35)
s2 = Student("Hari", 70)
s3 = Student("Sai", 90)

Student.curve_marks(10)

# for s in [s1, s2, s3]:
#     s.apply_curve()
#     print(s.name, s.marks, s.result(), Student.letter_grade(s.marks))
#
# print("Total Students:", Student.total_students)

#2 second
class Product:
    tax_rate = 18

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price + self.price * Product.tax_rate / 100

    @classmethod
    def change_tax(cls, rate):
        cls.tax_rate = rate

    @staticmethod
    def valid_price(price):
        return 0 <= price <= 100000


p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)

# print(p1.final_price())
# print(p2.final_price())
#
# Product.change_tax(10)
#
# print(p1.final_price())
# print(p2.final_price())
#
# print(Product.valid_price(500))
# print(Product.valid_price(-100))

#3 third
class Employee:
    promotion_exp = 5

    def __init__(self, name, exp, dept):
        self.name = name
        self.exp = exp
        self.dept = dept

    def eligible(self):
        return self.exp >= Employee.promotion_exp

    @classmethod
    def update_criteria(cls, exp):
        cls.promotion_exp = exp

    @staticmethod
    def valid_department(dept):
        return dept in ["HR", "Tech", "Admin"]


e1 = Employee("Ram", 6, "Tech")
e2 = Employee("Hari", 3, "HR")

# print(e1.eligible())
# print(e2.eligible())
#
# Employee.update_criteria(3)
#
# print(e1.eligible())
# print(e2.eligible())
#
# print(Employee.valid_department("Tech"))
# print(Employee.valid_department("Sales"))

#4 fourth

class Loan:
    interest_rate = 8

    def __init__(self, name, principal):
        self.name = name
        self.principal = principal

    def total_amount(self):
        return self.principal + self.principal * Loan.interest_rate / 100

    @classmethod
    def update_interest(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def eligible(salary):
        return salary > 30000


l1 = Loan("Ram", 100000)
l2 = Loan("Hari", 200000)

# print(l1.total_amount())
# print(l2.total_amount())
#
# Loan.update_interest(10)
#
# print(l1.total_amount())
# print(l2.total_amount())
#
# print(Loan.eligible(50000))
# print(Loan.eligible(20000))

#5 fifth

class Course:
    total_courses = 0
    min_duration = 30

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.enrolled_students = []
        Course.total_courses += 1

    def enroll(self, name):
        self.enrolled_students.append(name)

    @classmethod
    def update_duration(cls, d):
        cls.min_duration = d

    @staticmethod
    def valid_duration(d):
        return 0 < d <= 365


c1 = Course("Python", 45)
c2 = Course("Java", 60)

c1.enroll("Ram")
c1.enroll("Hari")

# print(c1.enrolled_students)
#
# Course.update_duration(20)
#
# print(Course.valid_duration(40))
# print(Course.valid_duration(-5))

#6 sixth

class Vehicle:
    service_rate = 5

    def __init__(self, model, km):
        self.model = model
        self.km = km
        self.history = []

    def service_charge(self):
        return self.km * Vehicle.service_rate

    @classmethod
    def update_rate(cls, rate):
        cls.service_rate = rate

    @staticmethod
    def eligible(year):
        return 2026 - year <= 15


v1 = Vehicle("Swift", 10000)
v2 = Vehicle("City", 25000)

# print(v1.service_charge())
# print(v2.service_charge())
#
# Vehicle.update_rate(8)
#
# print(v1.service_charge())
# print(v2.service_charge())
#
# print(Vehicle.eligible(2018))
# print(Vehicle.eligible(2005))

#7 seventh

class Inventory:
    total_items = 0
    min_stock = 10

    def __init__(self):
        self.stock = {}

    def update_stock(self, item, qty):
        self.stock[item] = self.stock.get(item, 0) + qty
        Inventory.total_items += qty

        if Inventory.below_threshold(self.stock[item]):
            print(item, "is below threshold")

    @classmethod
    def update_threshold(cls, value):
        cls.min_stock = value

    @staticmethod
    def below_threshold(qty):
        return qty < Inventory.min_stock


# i1 = Inventory()
# i2 = Inventory()
#
# i1.update_stock("Pen", 5)
# i2.update_stock("Book", 20)
#
# Inventory.update_threshold(15)
#
# i1.update_stock("Pen", 2)

#8 eighth

class HotelRoom:
    base_price = 2000

    def __init__(self, room, nights, guest):
        self.room = room
        self.nights = nights
        self.guest = guest

    def bill(self):
        return self.nights * HotelRoom.base_price

    @classmethod
    def update_price(cls, price):
        cls.base_price = price

    @staticmethod
    def valid_nights(n):
        return isinstance(n, int) and n > 0


r1 = HotelRoom(101, 2, "Ram")
r2 = HotelRoom(102, 5, "Hari")

# print(r1.bill())
# print(r2.bill())
#
# HotelRoom.update_price(2500)
#
# print(r1.bill())
# print(r2.bill())
#
# print(HotelRoom.valid_nights(3))
# print(HotelRoom.valid_nights(-2))


#9 ninth

class LibraryMember:
    total_members = 0
    borrow_limit = 3

    def __init__(self, name):
        self.name = name
        self.books = 0
        LibraryMember.total_members += 1

    def borrow(self, title):
        if not LibraryMember.valid_title(title):
            print("Invalid title")
            return

        if self.books < LibraryMember.borrow_limit:
            self.books += 1
            print(self.name, "borrowed", title)
        else:
            print("Borrow limit exceeded")

    @classmethod
    def update_limit(cls, limit):
        cls.borrow_limit = limit

    @staticmethod
    def valid_title(title):
        return isinstance(title, str) and 0 < len(title) <= 50


# m1 = LibraryMember("Ram")
# m2 = LibraryMember("Hari")
#
# m1.borrow("Python")
#
# LibraryMember.update_limit(5)
#
# m1.borrow("Java")
#
# print(LibraryMember.total_members)

#10 tenth

class Member:
    bmi_limit = 25

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        value = self.weight / (self.height ** 2)
        print("BMI:", round(value, 2))
        if value <= Member.bmi_limit:
            print("Fit")
        else:
            print("Not Fit")

    @classmethod
    def update_limit(cls, limit):
        cls.bmi_limit = limit

    @staticmethod
    def valid(height, weight):
        return height > 0 and weight > 0


m1 = Member("Ram", 1.75, 70)
m2 = Member("Hari", 1.7, 8 )

# m1.bmi()
# m2.bmi()
#
# Member.update_limit(23)
#
# m1.bmi()
#
# print(Member.valid(1.8, 75))
# print(Member.valid(-1.7, 60))
