# import copy
# l=[[1,2],[3,4]]
# x=l.copy()
# y=copy.deepcopy(l)
# z=l [0][0]=100
# print(l)
# print(x)
# print(y)
#
# from functools import reduce
# sales=[{"item":"pen","price":10,"qty":5},
#        {"item":"bag","price":500,"qty":0},
#        {"item":"book","price":120,"qty":3},
#        {"item":"eraser","price":5,"qty":10}]
# fun=reduce(lambda a,b:a+b,
#            map (lambda x:x["price"]*x["qty"],filter(lambda x:x["qty"]>0,sales)))
# print(fun)

def registration():
    name = input("Enter your name: ")
    password = input("Create a password: ")
    print(f"Registration successful! Welcome, {name}.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(f"Login successful! Welcome back, {username}.")

def profile():
    print("Name : Somaraju")
    print("Course : Python")
    print("Status : Active User")

menu = {1: registration,2: login,3: profile}

while True:
    print("\n== MENU =====")
    print("1. Registration")
    print("2. Login")
    print("3. Profile")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice.isdigit():
        choice = int(choice)

        if choice == 4:
            print("Thank you! Exiting the application.")
            break
        elif choice in menu:
            menu[choice]()
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Please enter a valid number.")

