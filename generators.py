#1
def numbers(n):
    for i in range(1, n + 1):
        yield i

# for x in numbers(5):
#     print(x,end=" ")

#2
def even(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
# for v in even(10):
#     print(v,end=" ")

#3
def chart(s):
    for i in s:
        yield i
# for z in chart("somaraju"):
#     print(z,end=" ")

#4

def reverse(n):
    for i in range(len(n)-1,-1,-1):
        yield n[i]
# for x in reverse("python"):
#     print(x,end=" ")

#5
def vowles(n):
    for i in n:
        if i.lower() in "aeiou":
            yield i
# for c in vowles("america"):
#     print(c,end=" ")

#6
def digits(n):
    for i in n:
        if i.isdigit():
            yield i
# for x in digits("python@561788816"):
#      print(x,end=" ")


#7
def square(lst):
    for i in lst:
        yield  i*i
# for x in square([1,3,4,5,5,5,3]):
#     print(x,end=' ')

#8
def integer_digits(n):
    for i in str(n):
        yield int(i)

# for x in integer_digits(747587):
#     print(x)



#9
def cumulative(lst):
    sum = 0

    for i in lst:
        sum =sum + i
        yield sum
#
# for x in cumulative([1,7,4,6]):
#     print(x,end=" ")


