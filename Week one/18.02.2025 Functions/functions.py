# A function is defined using def keyword

def greet():
    print("Hello, Mercy!")  # Function definition

greet() # Function call


def greet(name):
    print(f"Hello, {name}!")

greet("Mercy")
greet("Alice")


# Functions with Multiple Parameters
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


def multiply(c, d):
    return c * d

print(multiply(4, 5))


# Default parameters
def greet(name = "Friend"):
    print(f"Hello, {name}")

greet()  # Uses default value
greet("Mercy")


# Keyword Arguments(kwargs)
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")


display_info(age = 22, name = "Mercy")


def student(name, course):
    print(f"Name: {name}, Course: {course}")


student("Mercy","Data Science")


# args (Arbitrary Positional Arguments)
# Used when tou don't know how many arguments will be passed

def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3, 4, 5))

































