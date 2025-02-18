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


# Kwargs (Arbitrary Keyword Arguments)
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


student_info(name="Mercy", age=22, course = "Data Science")


# Lambda Functions
#Adding two numbers
add = lambda x, y: x + y
print(add(4, 6))


# Recursion functions
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)

print(factorial(5))


# Functions with Lists
def find_max(numbers):
    return max(numbers)

nums = [10, 25, 3, 67, 90]
print(find_max(nums))


# Functions with Lists
def find_min(numbers):
    return min(numbers)

nums = [10, 25, 3, 67, 90]
print(find_min(nums))


# Functions with return values
def get_details():
    name = "Mercy"
    age = 22
    return name, age  #Returns as a tuple

details = get_details()
print(details)


# Functions reduce code duplication and improve readability.
# Use args for multiple positional arguments.
# Use kwargs for multiple named arguments.
# Use lambda for small, or e-line functions
# Use recursion for problems like factorial,Fibonnaci, etc.












