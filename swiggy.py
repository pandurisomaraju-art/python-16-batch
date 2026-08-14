
# class Swiggy:
#
#     users = {}
#
#     def __init__(self, name, username, age, gender):
#         self.name = name
#         self.username = username
#         self.age = age
#         self.gender = gender
#         self.password = input("Enter your password: ")
#         self.cart = []
#         self.orders = []
#         self.logged = False
#
#         Swiggy.users[username] = self
#
#     @classmethod
#     def signup(cls):
#         name = input("Enter your Name: ")
#
#         while True:
#             username = input("Enter your username: ")
#
#             if username in Swiggy.users.keys():
#                 print("Username already registered, try another one")
#                 continue
#
#             break
#
#         age = input("Enter your age: ")
#         gender = input("Enter your gender (Male/Female): ")
#
#         return cls(name, username, age, gender)
#
#     def login(self):
#         if self.logged:
#             print("Already logged in")
#         else:
#             user = input("Enter your username: ")
#             password = input("Enter your password: ")
#
#             if user == self.username and password == self.password:
#                 self.logged = True
#                 print("Logged in Successfully")
#             else:
#                 print("Invalid Credentials")
#
#     def logout(self):
#         if self.logged:
#             self.logged = False
#             print("Logged out successfully")
#         else:
#             print("Already logged out")
#
#     def add_to_cart(self, item, price):
#         if self.logged:
#             self.cart.append([item, price])
#             print(item, "added to cart")
#         else:
#             print("Not logged in")
#
#     def remove_from_cart(self, item):
#         if self.logged:
#             for i in self.cart:
#                 if i[0] == item:
#                     self.cart.remove(i)
#                     print(item, "removed from cart")
#                     return
#
#             print("Item not found in cart")
#         else:
#             print("Not logged in")
#
#     def view_cart(self):
#         if self.logged:
#             if len(self.cart) == 0:
#                 print("Cart is empty")
#             else:
#                 print("Your Cart")
#
#                 total = 0
#
#                 for i, j in enumerate(self.cart):
#                     print(i, ":", j[0], "-", j[1])
#                     total += j[1]
#
#                 print("Total Amount :", total)
#         else:
#             print("Not logged in")
#
#     def place_order(self):
#         if self.logged:
#             if len(self.cart) == 0:
#                 print("Cart is empty")
#             else:
#                 total = 0
#
#                 for i in self.cart:
#                     total += i[1]
#
#                 self.orders.append(self.cart.copy())
#                 self.cart.clear()
#
#                 print("Order placed successfully")
#                 print("Total Amount :", total)
#         else:
#             print("Not logged in")
#
#     def order_history(self):
#         if self.logged:
#             if len(self.orders) == 0:
#                 print("No orders found")
#             else:
#                 print("Order History")
#
#                 for i, order in enumerate(self.orders):
#                     print("\nOrder", i + 1)
#
#                     total = 0
#
#                     for item in order:
#                         print(item[0], "-", item[1])
#                         total += item[1]
#
#                     print("Total :", total)
#         else:
#             print("Not logged in")
#
#     def profile(self):
#         if self.logged:
#             print(f"{self.name}'s Profile")
#             print(f"Name : {self.name}")
#             print(f"Age : {self.age}")
#             print(f"Gender : {self.gender}")
#             print(f"Username : {self.username}")
#             print(f"Cart Items : {len(self.cart)}")
#             print(f"Orders : {len(self.orders)}")
#         else:
#             print("Not logged in")
#
#
# # Creating users
#
# s1 = Swiggy.signup()
# s2 = Swiggy.signup()
# s3 = Swiggy.signup()
#
#
# # Login
#
# s1.login()
#
#
# # Adding items to cart
#
# s1.add_to_cart("Chicken Biryani", 250)
# s1.add_to_cart("Chicken 65", 180)
# s1.add_to_cart("Coke", 50)
#
#
# # View cart
#
# s1.view_cart()
#
#
# # Remove item
#
# s1.remove_from_cart("Coke")
#
#
# # View cart again
#
# s1.view_cart()
#
#
# # Place order
#
# s1.place_order()
#
#
# # Order history
#
# s1.order_history()
#
#
# # Profile
#
# s1.profile()
#
#
# # Logout
#
# s1.logout()


class Swiggy:
    users = {}  # Registry mapping phone_number -> Swiggy user instance

    # Mock catalog of restaurants, menu items, and prices (in ₹)
    catalog = {
        "Biryani Zone": {
            "Chicken Biryani": 250,
            "Paneer Biryani": 200,
            "Garlic Naan": 40
        },
        "Pizza Hut": {
            "Pepperoni Pizza": 400,
            "Margherita Pizza": 300,
            "Garlic Bread": 150
        },
        "Burger King": {
            "Veg Whopper": 180,
            "Chicken Whopper": 220,
            "Fries": 90
        }
    }

    def __init__(self, name, phone, address, password, wallet_balance=500.0):
        self.name = name
        self.phone = phone
        self.address = address
        self.password = password
        self.wallet_balance = float(wallet_balance)
        self.cart = []
        self.order_history = []
        self.logged = False

        # Register user in class registry
        Swiggy.users[phone] = self

    @classmethod
    def signup(cls):
        print("\n--- Swiggy Sign Up ---")
        name = input("Enter your Name: ").strip()
        while True:
            phone = input("Enter your 10-digit Phone Number: ").strip()
            if phone in cls.users:
                print("Phone number already registered. Try another number.")
                continue
            if len(phone) != 10 or not phone.isdigit():
                print("Invalid phone number. Must be exactly 10 digits.")
                continue
            break

        address = input("Enter your Delivery Address: ").strip()
        password = input("Enter your Password: ")

        print(f"Account created successfully for {name}!")
        return cls(name, phone, address, password)

    def login(self):
        if self.logged:
            print(f"{self.name} is already logged in.")
            return

        print(f"\n--- Login ({self.name}) ---")
        entered_phone = input("Enter your phone number: ").strip()
        entered_pass = input("Enter your password: ")

        if entered_phone == self.phone and entered_pass == self.password:
            self.logged = True
            print(f"Logged in successfully! Welcome back, {self.name}.")
        else:
            print("Invalid phone number or password.")

    def logout(self):
        if self.logged:
            self.logged = False
            print(f"{self.name} logged out successfully.")
        else:
            print("Already logged out.")

    def view_restaurants(self):
        print("\n--- Available Restaurants ---")
        for idx, restaurant in enumerate(Swiggy.catalog.keys(), 1):
            print(f"{idx}. {restaurant}")

    def add_to_cart(self):
        if not self.logged:
            print("Action failed: Not logged in.")
            return

        self.view_restaurants()
        res_list = list(Swiggy.catalog.keys())

        try:
            r_choice = int(input("Select restaurant number: ")) - 1
            if not (0 <= r_choice < len(res_list)):
                print("Invalid restaurant choice.")
                return

            selected_res = res_list[r_choice]
            menu = Swiggy.catalog[selected_res]

            print(f"\n--- Menu for {selected_res} ---")
            menu_items = list(menu.items())
            for idx, (item, price) in enumerate(menu_items, 1):
                print(f"{idx}. {item} - ₹{price}")

            item_choice = int(input("Select item number to add: ")) - 1
            if not (0 <= item_choice < len(menu_items)):
                print("Invalid item choice.")
                return

            item_name, item_price = menu_items[item_choice]
            self.cart.append({
                "restaurant": selected_res,
                "item": item_name,
                "price": item_price
            })
            print(f"Added '{item_name}' (₹{item_price}) to your cart.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    def view_cart(self):
        if not self.logged:
            print("Action failed: Not logged in.")
            return

        if not self.cart:
            print("Your cart is empty.")
            return

        total = sum(item["price"] for item in self.cart)
        print("\n--- Current Cart ---")
        for idx, item in enumerate(self.cart, 1):
            print(f"{idx}. {item['item']} ({item['restaurant']}) - ₹{item['price']}")
        print(f"Total Amount: ₹{total}")

    def checkout(self):
        if not self.logged:
            print("Action failed: Not logged in.")
            return

        if not self.cart:
            print("Cannot checkout: Your cart is empty.")
            return

        total = sum(item["price"] for item in self.cart)
        print(f"\nTotal Order Price: ₹{total}")
        print(f"Wallet Balance: ₹{self.wallet_balance}")

        if self.wallet_balance < total:
            print(f"Insufficient funds! You need ₹{total - self.wallet_balance} more.")
            return

        # Process payment
        self.wallet_balance -= total
        order_summary = {
            "items": list(self.cart),
            "total": total,
            "address": self.address
        }
        self.order_history.append(order_summary)
        self.cart.clear()

        print(f"Order placed successfully!")
        print(f"Delivering to: {self.address}")
        print(f"Remaining Wallet Balance: ₹{self.wallet_balance:.2f}")

    def view_order_history(self):
        if not self.logged:
            print("Action failed: Not logged in.")
            return

        if not self.order_history:
            print("No past orders found.")
            return

        print(f"\n--- Order History for {self.name} ---")
        for idx, order in enumerate(self.order_history, 1):
            items_str = ", ".join([f"{item['item']}" for item in order['items']])
            print(f"Order #{idx}: [{items_str}] -> Total: ₹{order['total']}")

    def profile(self):
        print(f"\n--- {self.name}'s Swiggy Profile ---")
        print(f"Phone       : {self.phone}")
        print(f"Address     : {self.address}")
        print(f"Wallet      : ₹{self.wallet_balance:.2f}")
        print(f"Cart Items  : {len(self.cart)}")
        print(f"Total Orders: {len(self.order_history)}")


# Demonstration Script
if __name__ == "__main__":
    # Create user via signup
    u1 = Swiggy.signup()

    # Login and interact
    u1.login()
    u1.add_to_cart()  # Select restaurant and add an item
    u1.add_to_cart()  # Add another item
    u1.view_cart()  # View cart contents and total
    u1.checkout()  # Place order using wallet balance
    u1.view_order_history()
    u1.profile()
