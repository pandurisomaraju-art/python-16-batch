#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)

#2
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
# print(squares)

#3
marks = [75, 35, 60, 28, 90]
result = ["Pass" if mark >= 40 else "Fail" for mark in marks]
# print(result)

#4
numbers = [10, 15, 10, 20, 25, 20, 30, 35, 30]
even_numbers = {x for x in numbers if x % 2 == 0}
# print(even_numbers)

#5
words = ["Python", "Java", "C", "Django", "Python"]
lengths = {len(word) for word in words}
# print(lengths)

#6
students = { "Rahul": 75,"Anil": 32, "Priya": 56,"Sneha": 28}
result = {name: "Pass" if mark >= 40 else "Fail"
          for name, mark in students.items()}
# print(result)

#7
usernames = ["charan", "rahul", "priya", "sneha"]
passwords = ["abc123", "xyz456", "pqr789", "hello123"]
# result = {usernames[i]: passwords[i] for i in range(len(usernames))}
# print(result)
rs={i:j for i,j in zip (usernames,passwords)}
# print(rs)

#8
products = {"Laptop": 65000,"Mouse": 500, "Keyboard": 1500, "Monitor": 12000 }
r={item: "expensive" if price>=10000 else "Affortable"
        for item,price in products.items()}
# print(r)

#9
students = {"Rahul": 35,"Anil": 72,"Priya": 81,"Sneha": 29,"Kiran": 65}
passed = {name: mark for name, mark in students.items() if mark >= 40}
# print(passed)

#10
squares = (x * x for x in range(1, 11))
# print(next(squares))
# print(next(squares))
# print(next(squares))

#11
even_numbers = (x for x in range(1, 21) if x % 2 == 0)
# for x in even_numbers:
#     print(x,end=" ")

#12
numbers = [10, 15, 20, 25, 30, 35]
result = (x for x in numbers if x > 20)
# for x in result:
#     print(x,end=" ")

#13
marks = {"Rahul": 85,"Anil": 32,"Priya": 76,"Sneha": 45,"Kiran": 28}
result = { name: "Distinction" if mark >= 75 else "Pass" if mark >= 40 else "Fail" for name, mark in marks.items()}
# print(result)

#14
usernames = ["admin", "charan", "root", "guest", "developer"]
result = { username: "Valid" if len(username) >= 5 else "Invalid" for username in usernames}
# print(result)

#15
names = ["Rahul", "Priya", "Kiran", "Sneha"]
marks = [75, 35, 82, 28]
result = { names[i]: "Pass" if marks[i] >= 40 else "Fail" for i in range(len(names))}
# print(result)

