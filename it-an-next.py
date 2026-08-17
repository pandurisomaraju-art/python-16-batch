#1
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} — Rs.{self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"


b = Book("Python", "Guido", 500)

# print(b)
# print(str(b))
# print(repr(b))
# print(f"{b}")
# print(f"{b!r}")

#2
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Vector2D(self.x * n, self.y * n)

    def __truediv__(self, n):
        return Vector2D(self.x / n, self.y / n)

    def __floordiv__(self, n):
        return Vector2D(self.x // n, self.y // n)

    def __mod__(self, n):
        return Vector2D(self.x % n, self.y % n)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
#
# print(v1 + v2)
# print(v1 - v2)
# print(v1 * 2)
# print(v1 / 2)
# print(v1 // 2)
# print(v1 % 2)
#
# print(repr(v1))

#3
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __le__(self, other):
        return self.celsius <= other.celsius

    def __gt__(self, other):
        return self.celsius > other.celsius

    def __ge__(self, other):
        return self.celsius >= other.celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __hash__(self):
        return hash(self.celsius)

    def __repr__(self):
        return f"Temperature({self.celsius})"


t1 = Temperature(100)
t2 = Temperature(50)
t3 = Temperature(25)

# print(t1 > t2)
# print(t1 >= t2)
# print(t3 < t2)
# print(t2 == Temperature(50))
#
# temperatures = [
#     Temperature(100),
#     Temperature(25),
#     Temperature(50),
#     Temperature(75)
# ]
#
# print(sorted(temperatures))
#
# s = {
#     Temperature(100),
#     Temperature(50),
#     Temperature(100)
# }
#
# print(s)


#4
class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

    def __contains__(self, title):
        return title in self.books

    def __str__(self):
        return f"Library with {len(self.books)} books"


library = Library(["Python", "Java", "HTML"])

# print(len(library))
# print("Python" in library)
# print("C++" in library)
# print(library)
#
# empty_library = Library([])
#
# print(len(empty_library))
# print(bool(empty_library))

#5
def simulate_for_loop(iterable):
    iterator = iter(iterable)
    index = 0

    while True:
        try:
            value = next(iterator)
            print(index, value)
            index += 1
        except StopIteration:
            break


# print("List:")
# simulate_for_loop([10, 20, 30])
#
# print("String:")
# simulate_for_loop("ABC")
#
# print("Range:")
# simulate_for_loop(range(3))

#6
class EvenNumbers:
    def __init__(self, start, count):
        self.current = start
        self.count = count
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated < self.count:

            if self.current % 2 != 0:
                self.current += 1

            value = self.current
            self.current += 2
            self.generated += 1

            return value

        raise StopIteration


obj = EvenNumbers(3, 5)
#
# print(obj.__iter__() is obj)
#
# for i in obj:
#     print(i)