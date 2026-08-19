#1
class OneToN:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            x = self.i
            self.i += 1
            return x
        raise StopIteration


# n = int(input("Enter N: "))
#
# obj = OneToN(n)
#
# for i in obj:
#     print(i, end=" ")


#2
class NToOne:
    def __init__(self, n):
        self.i = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 1:
            x = self.i
            self.i -= 1
            return x
        raise StopIteration

# n = int(input("Enter N: "))
#
# obj = NToOne(n)
#
# for i in obj:
#     print(i, end=" ")

#3from

class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.i = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            x = self.i
            self.i += 2
            self.count += 1
            return x
        raise StopIteration


# n = int(input("Enter N: "))
#
# obj = EvenNumbers(n)
#
# for i in obj:
#     print(i, end=" ")

#4from
class OddNumbers:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            x = self.i
            self.i += 2
            self.count += 1
            return x
        raise StopIteration


# n = int(input("Enter N: "))
#
# obj = OddNumbers(n)
#
# for i in obj:
#     print(i, end=" ")

#5from

class EvenList:
    def __init__(self, l):
        self.l = l
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.l):
            x = self.l[self.i]
            self.i += 1

            if x % 2 == 0:
                return x

        raise StopIteration


# l = list(map(int, input("Enter numbers: ").split()))
#
# obj = EvenList(l)
#
# for i in obj:
#     print(i, end=" ")


#6from

class OddList:
    def __init__(self, l):
        self.l = l
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.l):
            x = self.l[self.i]
            self.i += 1

            if x % 2 != 0:
                return x

        raise StopIteration


# l = list(map(int, input("Enter numbers: ").split()))
#
# obj = OddList(l)
#
# for i in obj:
#     print(i, end=" ")


#7from

class PositiveNumbers:
    def __init__(self, l):
        self.l = l
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.l):
            x = self.l[self.i]
            self.i += 1

            if x > 0:
                return x

        raise StopIteration

#
# l = list(map(int, input("Enter numbers: ").split()))
#
# obj = PositiveNumbers(l)
#
# for i in obj:
#     print(i, end=" ")


#8from


class Characters:
    def __init__(self, s):
        self.s = s
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.s):
            x = self.s[self.i]
            self.i += 1
            return x

        raise StopIteration
#
#
# s = input("Enter string: ")
#
# obj = Characters(s)
#
# for i in obj:
#     print(i)

#9from


class ReverseCharacters:
    def __init__(self, s):
        self.s = s
        self.i = len(s) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            x = self.s[self.i]
            self.i -= 1
            return x

        raise StopIteration


# s = input("Enter string: ")
#
# obj = ReverseCharacters(s)
#
# for i in obj:
#     print(i, end="")

# 1. Custom iterator that prints numbers from 1 to N
class OneToN:
    def __init__(self, n):
        self.n = n
        self.i = 1


    def __iter__(self):
        return self


    def __next__(self):
        if self.i <= self.n:
            x = self.i
            self.i += 1
            return x
        raise StopIteration


#
#
# n = int(input("Enter N: "))
#
#
# obj = OneToN(n)
#
#
# for i in obj:
#     print(i, end=" ")


# 2. Iterator that returns only even numbers from a list
class EvenNumbers:
    def __init__(self, l):
        self.l = l
        self.i = 0


    def __iter__(self):
        return self


    def __next__(self):
        while self.i < len(self.l):
            x = self.l[self.i]
            self.i += 1


            if x % 2 == 0:
                return x


        raise StopIteration


# l = list(map(int, input().split()))
#
#
# obj = EvenNumbers(l)
#
#
# for i in obj:
#     print(i, end=" ")



# 3. Iterator that iterates over a string in reverse
class ReverseString:
    def __init__(self, s):
        self.s = s
        self.i = len(s) - 1


    def __iter__(self):
        return self


    def __next__(self):
        if self.i >= 0:
            x = self.s[self.i]
            self.i -= 1
            return x


        raise StopIteration


# s = input()
#
#
# obj = ReverseString(s)
#
#
# for i in obj:
#     print(i, end="")

# 4. Iterator that returns elements with their index


class ListIndex:
    def __init__(self, l):
        self.l = l
        self.i = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.i < len(self.l):
            x = (self.i, self.l[self.i])
            self.i += 1
            return x


        raise StopIteration

# l = input().split()
#
#
# obj = ListIndex(l)
#
#
# for i in obj:
#     print(i)


# 5. Generator that yields digits from an integer
def digits(n):
    n = abs(n)

    for i in str(n):
        yield int(i)


# n = int(input())
#
# for i in digits(n):
#     print(i, end=" ")


# 6. Generator for cumulative sum


def cumulative(l):
    total = 0


    for i in l:
        total = total + i
        yield total

# l = list(map(int, input().split()))
#
#
# for i in cumulative(l):
#     print(i, end=" ")

# 7. Generator that yields vowels from a string
def vowels(s):
    for i in s:
        if i.lower() in "aeiou":
            yield i

# s = input()
#
#
# for i in vowels(s):
#     print(i, end=" ")


# 8. Iterator that yields words from a sentence
class Words:
    def __init__(self, s):
        self.l = s.split()
        self.i = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.i < len(self.l):
            x = self.l[self.i]
            self.i += 1
            return x


        raise StopIteration

# s = input()
#
#
# obj = Words(s)
#
#
# for i in obj:
#     print(i)

# 9. Iterator that returns characters at even indices



class EvenIndex:
    def __init__(self, s):
        self.s = s
        self.i = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.i < len(self.s):
            x = self.s[self.i]
            self.i += 2
            return x


        raise StopIteration




# s = input()
#
#
# obj = EvenIndex(s)
#
#
# for i in obj:
#     print(i, end=" ")

# 10. Generator for running maximum


def running_max(l):
    maximum = l[0]


    for i in l:
        if i > maximum:
            maximum = i


        yield maximum



#
# l = list(map(int, input().split()))
#
#
# for i in running_max(l):
#     print(i, end=" ")

