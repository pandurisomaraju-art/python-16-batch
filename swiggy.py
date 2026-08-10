
class Swiggy:

    users = {}

    def __init__(self, name, username, age, gender):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = input("Enter your password: ")
        self.cart = []
        self.orders = []
        self.logged = False

        Swiggy.users[username] = self

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")

        while True:
            username = input("Enter your username: ")

            if username in Swiggy.users.keys():
                print("Username already registered, try another one")
                continue

            break

        age = input("Enter your age: ")
        gender = input("Enter your gender (Male/Female): ")

        return cls(name, username, age, gender)

    def login(self):
        if self.logged:
            print("Already logged in")
        else:
            user = input("Enter your username: ")
            password = input("Enter your password: ")

            if user == self.username and password == self.password:
                self.logged = True
                print("Logged in Successfully")
            else:
                print("Invalid Credentials")

    def logout(self):
        if self.logged:
            self.logged = False
            print("Logged out successfully")
        else:
            print("Already logged out")

    def add_to_cart(self, item, price):
        if self.logged:
            self.cart.append([item, price])
            print(item, "added to cart")
        else:
            print("Not logged in")

    def remove_from_cart(self, item):
        if self.logged:
            for i in self.cart:
                if i[0] == item:
                    self.cart.remove(i)
                    print(item, "removed from cart")
                    return

            print("Item not found in cart")
        else:
            print("Not logged in")

    def view_cart(self):
        if self.logged:
            if len(self.cart) == 0:
                print("Cart is empty")
            else:
                print("Your Cart")

                total = 0

                for i, j in enumerate(self.cart):
                    print(i, ":", j[0], "-", j[1])
                    total += j[1]

                print("Total Amount :", total)
        else:
            print("Not logged in")

    def place_order(self):
        if self.logged:
            if len(self.cart) == 0:
                print("Cart is empty")
            else:
                total = 0

                for i in self.cart:
                    total += i[1]

                self.orders.append(self.cart.copy())
                self.cart.clear()

                print("Order placed successfully")
                print("Total Amount :", total)
        else:
            print("Not logged in")

    def order_history(self):
        if self.logged:
            if len(self.orders) == 0:
                print("No orders found")
            else:
                print("Order History")

                for i, order in enumerate(self.orders):
                    print("\nOrder", i + 1)

                    total = 0

                    for item in order:
                        print(item[0], "-", item[1])
                        total += item[1]

                    print("Total :", total)
        else:
            print("Not logged in")

    def profile(self):
        if self.logged:
            print(f"{self.name}'s Profile")
            print(f"Name : {self.name}")
            print(f"Age : {self.age}")
            print(f"Gender : {self.gender}")
            print(f"Username : {self.username}")
            print(f"Cart Items : {len(self.cart)}")
            print(f"Orders : {len(self.orders)}")
        else:
            print("Not logged in")


# Creating users

s1 = Swiggy.signup()
s2 = Swiggy.signup()
s3 = Swiggy.signup()


# Login

s1.login()


# Adding items to cart

s1.add_to_cart("Chicken Biryani", 250)
s1.add_to_cart("Chicken 65", 180)
s1.add_to_cart("Coke", 50)


# View cart

s1.view_cart()


# Remove item

s1.remove_from_cart("Coke")


# View cart again

s1.view_cart()


# Place order

s1.place_order()


# Order history

s1.order_history()


# Profile

s1.profile()


# Logout

s1.logout()
