class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)


class User(Bank):
    def __init__(self, name, balance):
        super().__init__(balance)
        self.name = name

    def display_name(self):
        print("User:", self.name)

#
# u = User("Somaraju", 5000)
#
# u.display_name()
# u.deposit(2000)
# u.withdraw(1000)
# u.check_balance()

#2
class employee:
    def __init__(self,emp_name,sal):
        self.emp_name=emp_name
        self.salary=sal
    def display_details(self):
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)
class manager(employee):
    def bonus(self, amount):
        self.salary += amount
        print("Bonus:", amount)
        print("Total Salary:", self.salary)

# m = manager("Ravi", 50000)
#
# m.display_details()
# m.bonus(10000)

#3
class student:
    def __init__(self,na,ma):
        self.name=na
        self.marks=ma
    def display_marks(self):
        print("Name:", self.name)
        print("total marks:",self.marks)
class result(student):
    def res(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")
# s = result("Somaraju", 75)
#
# s.display_marks()
# s.res()

#4
class Restaurant:
    def menu(self, item):
        prices = {
            "pizza": 250,
            "burger": 150,
            "biryani": 200,
            "fried_rice": 120
        }

        return prices.get(item, 0)


class FoodCourt(Restaurant):
    def __init__(self):
        self.total = 0

    def display_menu(self):
        print("Pizza - 250")
        print("Burger - 150")
        print("Biryani - 200")
        print("Fried_rice - 120")

    def order(self):
        self.display_menu()

        while True:
            item = input("Enter item (or done): ").lower()

            if item == "done":
                break

            price = self.menu(item)

            if price > 0:
                self.total += price
                print("Added:", item, price)
            else:
                print("Item not available")

        self.billing()

    def billing(self):
        print("Food Bill:", self.total)
        print("Packing Charge: 20")
        print("Total Amount:", self.total + 20)


class Customer(FoodCourt):
    pass


# c = Customer()
# c.order()

#5
class Movie:
    def ticket(self, movie):
        prices = {
            "avatar": 250,
            "pushpa": 200,
            "bahubali": 180
        }

        return prices.get(movie, 0)


class Booking(Movie):
    def __init__(self):
        self.total = 0

    def movies(self):
        print("Avatar - 250")
        print("Pushpa - 200")
        print("Bahubali - 180")

    def selection(self):
        self.movies()

        while True:
            movie = input("Enter movie (or done): ").lower()

            if movie == "done":
                break

            quantity = int(input("Enter number of tickets: "))

            price = self.ticket(movie)

            if price > 0:
                self.total += price * quantity
                print("Tickets booked")
            else:
                print("Movie not available")

        self.billing()

    def billing(self):
        print("Ticket Amount:", self.total)
        print("Booking Charge: 30")
        print("Total Amount:", self.total + 30)


class Customer(Booking):
    pass


# c = Customer()
# c.selection()


#6
class Course:
    def fee(self, course):
        fees = {
            "python": 5000,
            "java": 6000,
            "web": 4000
        }

        return fees.get(course, 0)


class Academy(Course):
    def __init__(self):
        self.total = 0

    def courses(self):
        print("Python - 5000")
        print("Java - 6000")
        print("Web - 4000")

    def enroll(self):
        self.courses()

        while True:
            course = input("Enter course (or done): ").lower()

            if course == "done":
                break

            price = self.fee(course)

            if price > 0:
                self.total += price
                print("Course enrolled")
            else:
                print("Course not available")

        self.billing()

    def billing(self):
        print("Course Fee:", self.total)
        print("Registration Fee: 100")
        print("Total Amount:", self.total + 100)


class Student(Academy):
    pass


# s = Student()
# s.enroll()

#7
class Cab:
    def bike(self, distance):
        return distance * 10

    def auto(self, distance):
        return distance * 15

    def car(self, distance):
        return distance * 20


class Uber(Cab):
    def __init__(self):
        self.total = 0

    def menu(self):
        print("1. Bike - ₹10/km")
        print("2. Auto - ₹15/km")
        print("3. Car - ₹20/km")

    def booking(self):
        self.menu()

        choice = int(input("Enter choice: "))
        distance = int(input("Enter distance: "))

        if choice == 1:
            self.total = self.bike(distance)
        elif choice == 2:
            self.total = self.auto(distance)
        elif choice == 3:
            self.total = self.car(distance)
        else:
            print("Invalid choice")
            return

        self.billing()

    def billing(self):
        amount = self.total

        if amount > 1000:
            discount = amount * 0.15
            amount -= discount
        else:
            discount = 0

        gst = amount * 0.10
        amount += gst

        print("Fare:", self.total)
        print("Discount:", discount)
        print("GST:", gst)
        print("Total Bill:", amount)


class Ola(Cab):
    def __init__(self):
        self.total = 0

    def menu(self):
        print("1. Bike - ₹10/km")
        print("2. Auto - ₹15/km")
        print("3. Car - ₹20/km")

    def booking(self):
        self.menu()

        choice = int(input("Enter choice: "))
        distance = int(input("Enter distance: "))

        if choice == 1:
            self.total = self.bike(distance)
        elif choice == 2:
            self.total = self.auto(distance)
        elif choice == 3:
            self.total = self.car(distance)
        else:
            print("Invalid choice")
            return

        self.billing()

    def billing(self):
        amount = self.total

        if amount > 1500:
            discount = amount * 0.20
            amount -= discount
        else:
            discount = 0

        gst = amount * 0.12
        amount += gst

        print("Fare:", self.total)
        print("Discount:", discount)
        print("GST:", gst)
        print("Total Bill:", amount)


# choice = input("Choose Uber or Ola: ").lower()
#
# if choice == "uber":
#     obj = Uber()
#     obj.booking()
#
# elif choice == "ola":
#     obj = Ola()
#     obj.booking()
#
# else:
#     print("Invalid choice")

#8
class Grocery:
    def rice(self, quantity):
        return quantity * 60

    def sugar(self, quantity):
        return quantity * 50

    def oil(self, quantity):
        return quantity * 120


class Dmart(Grocery):
    def __init__(self):
        self.total = 0

    def items(self):
        print("Rice - ₹60/kg")
        print("Sugar - ₹50/kg")
        print("Oil - ₹120/litre")

    def shopping(self):
        self.items()

        while True:
            item = input("Enter item (or done): ").lower()

            if item == "done":
                break

            quantity = int(input("Enter quantity: "))

            if item == "rice":
                self.total += self.rice(quantity)
            elif item == "sugar":
                self.total += self.sugar(quantity)
            elif item == "oil":
                self.total += self.oil(quantity)
            else:
                print("Item not available")

        self.billing()

    def billing(self):
        amount = self.total

        if amount > 2000:
            discount = amount * 0.10
            amount -= discount
        else:
            discount = 0

        gst = amount * 0.05
        amount += gst

        print("Bill:", self.total)
        print("Discount:", discount)
        print("GST:", gst)
        print("Total Amount:", amount)


class RelianceSmart(Grocery):
    def __init__(self):
        self.total = 0

    def items(self):
        print("Rice - ₹60/kg")
        print("Sugar - ₹50/kg")
        print("Oil - ₹120/litre")

    def shopping(self):
        self.items()

        while True:
            item = input("Enter item (or done): ").lower()

            if item == "done":
                break

            quantity = int(input("Enter quantity: "))

            if item == "rice":
                self.total += self.rice(quantity)
            elif item == "sugar":
                self.total += self.sugar(quantity)
            elif item == "oil":
                self.total += self.oil(quantity)
            else:
                print("Item not available")

        self.billing()

    def billing(self):
        amount = self.total

        if amount > 2500:
            discount = amount * 0.15
            amount -= discount
        else:
            discount = 0

        gst = amount * 0.05
        amount += gst

        print("Bill:", self.total)
        print("Discount:", discount)
        print("GST:", gst)
        print("Total Amount:", amount)


# choice = input("Choose Dmart or Reliance Smart: ").lower()
#
# if choice == "dmart":
#     obj = Dmart()
#     obj.shopping()
#
# elif choice == "reliance smart":
#     obj = RelianceSmart()
#     obj.shopping()
#
# else:
#     print("Invalid choice")

#9

class Bus:
    def sleeper(self, tickets):
        return tickets * 800

    def semi_sleeper(self, tickets):
        return tickets * 600

    def ac(self, tickets):
        return tickets * 1000


class RedBus(Bus):
    def __init__(self):
        self.total = 0

    def routes(self):
        print("1. Sleeper - ₹800")
        print("2. Semi-Sleeper - ₹600")
        print("3. AC - ₹1000")

    def booking(self):
        self.routes()

        choice = int(input("Enter choice: "))
        tickets = int(input("Enter number of tickets: "))

        if choice == 1:
            self.total = self.sleeper(tickets)
        elif choice == 2:
            self.total = self.semi_sleeper(tickets)
        elif choice == 3:
            self.total = self.ac(tickets)
        else:
            print("Invalid choice")
            return

        self.billing()

    def billing(self):
        gst = self.total * 0.10
        total = self.total + gst + 30

        print("Fare:", self.total)
        print("GST:", gst)
        print("Reservation Charge: 30")
        print("Total:", total)


class AbhiBus(Bus):
    def __init__(self):
        self.total = 0

    def routes(self):
        print("1. Sleeper - ₹800")
        print("2. Semi-Sleeper - ₹600")
        print("3. AC - ₹1000")

    def booking(self):
        self.routes()

        choice = int(input("Enter choice: "))
        tickets = int(input("Enter number of tickets: "))

        if choice == 1:
            self.total = self.sleeper(tickets)
        elif choice == 2:
            self.total = self.semi_sleeper(tickets)
        elif choice == 3:
            self.total = self.ac(tickets)
        else:
            print("Invalid choice")
            return

        self.billing()

    def billing(self):
        gst = self.total * 0.10
        total = self.total + gst + 20

        print("Fare:", self.total)
        print("GST:", gst)
        print("Reservation Charge: 20")
        print("Total:", total)
# choice = input("Choose RedBus or AbhiBus: ").lower()
#
# if choice == "redbus":
#     obj = RedBus()
#     obj.booking()
#
# elif choice == "abhibus":
#     obj = AbhiBus()
#     obj.booking()
#
# else:
#     print("Invalid choice")


#10
class SBI:
    def __init__(self):
        self.balance = 5000

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def check_balance(self):
        print("Balance:", self.balance)


class UnionBank:
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def mini_statement(self):
        print("Current Balance:", self.balance)


class ATM(SBI, UnionBank):
    def menu(self):
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Mini Statement")
        print("5. Exit")

    def transaction(self):
        while True:
            self.menu()

            choice = int(input("Enter choice: "))

            if choice == 1:
                amount = int(input("Enter amount: "))
                self.deposit(amount)

            elif choice == 2:
                amount = int(input("Enter amount: "))
                self.withdraw(amount)

            elif choice == 3:
                self.check_balance()

            elif choice == 4:
                self.mini_statement()

            elif choice == 5:
                print("Thank you")
                break

            else:
                print("Invalid choice")

#
# obj = ATM()
# obj.transaction()
#11
class MobileRecharge:
    def recharge_plans(self):
        print("1. ₹199 - 1GB/day")
        print("2. ₹299 - 1.5GB/day")
        print("3. ₹399 - 2GB/day")

    def mobile_recharge(self):
        self.recharge_plans()

        choice = int(input("Select plan: "))

        if choice == 1:
            print("₹199 recharge successful")
        elif choice == 2:
            print("₹299 recharge successful")
        elif choice == 3:
            print("₹399 recharge successful")
        else:
            print("Invalid plan")


class BusTicketBooking:
    def display_buses(self):
        print("1. Visakhapatnam to Hyderabad")
        print("2. Visakhapatnam to Vijayawada")
        print("3. Visakhapatnam to Chennai")

    def book_ticket(self):
        self.display_buses()

        choice = int(input("Select bus: "))

        if choice in [1, 2, 3]:
            print("Bus ticket booked successfully")
        else:
            print("Invalid choice")


class ElectricityBills:
    def bill_details(self):
        print("Electricity Bill Payment")

    def pay_bill(self):
        self.bill_details()

        amount = float(input("Enter bill amount: "))
        print("Electricity bill of ₹", amount, "paid successfully")


class Paytm(MobileRecharge, BusTicketBooking, ElectricityBills):
    def menu(self):
        print("\n--- Paytm ---")
        print("1. Mobile Recharge")
        print("2. Bus Ticket Booking")
        print("3. Electricity Bill Payment")
        print("4. Exit")

    def services(self):
        while True:
            self.menu()

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.mobile_recharge()

            elif choice == 2:
                self.book_ticket()

            elif choice == 3:
                self.pay_bill()

            elif choice == 4:
                print("Thank you for using Paytm")
                break

            else:
                print("Invalid choice")


obj = Paytm()
obj.services()



























































