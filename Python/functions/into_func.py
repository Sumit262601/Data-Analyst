"""
Python Functions:
---------------
A function is a reusable block of code that performs a specific task.
Functions help in organizing code, promoting reusability, and making programs more modular.

Types of Functions:
1. Built-in functions (print(), len(), etc.)
2. User-defined functions (created by users)

Function Structure:
def function_name(parameters):
    # function body
    return value  # optional
"""

# 1. Basic Function Example
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

# 2. Function with Parameters
def greet_person(name): # parameters
    print(f"\nHello, {name}!")

greet_person("Alice") # arguments  # Output: Hello, Alice!

# 3. Function with Default Parameters
def greet_with_time(name, time="morning"):
    print(f"\nGood {time}, {name}!")

greet_with_time("Bob")  # Output: Good morning, Bob!
greet_with_time("Charlie", "evening")  # Output: Good evening, Charlie!

# 4. Function with Return Value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"\nSum: {result}")  # Output: Sum: 8

# 5. Multiple Return Values
def calculate_math(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    return add, subtract, multiply

sum_result, diff_result, prod_result = calculate_math(10, 5)
print(f"\nResults: {sum_result}, {diff_result}, {prod_result}")

# 6. *args (Variable-length Arguments)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# 7. **kwargs (Keyword Arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"\n{key}: {value}")

print_info(name="David", age=25, city="New York")

# 8. Lambda Functions (Anonymous Functions)
square = lambda x: x**2
print("Square of 5: " , square(5))  # Output: 25

# 9. Recursive Function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(f"\nFactorial of 5: {factorial(5)}")  # Output: 120

# 10. Function with Type Hints (Python 3.5+)
def calculate_area(length: float, width: float) -> float:
    return length * width

area = calculate_area(5.0, 3.2)
print(f"\nArea is: {area}")

def calculate_square_area( side ) -> float:
    return side * side

square_area = calculate_square_area(4)
print(f"\nArea of square: {square_area}")

# 11. Decorator Function
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator

def greet_world():
    return "hello, world!"

print(greet_world())  # Output: HELLO, WORLD!

# 12. Generator Function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num, end=" ")  # Output: 0 1 1 2 3

# 13. Nested Functions
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(f"\nResult: {add_five(3)}")  # Output: 8

# 14. Function with Documentation
def calculate_bmi(weight: float, height: float) -> float:
    """
    --------------- Calculate Body Mass Index (BMI) --------------- 
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
        
    Returns:
        float: BMI value
    """
    return weight / (height ** 2)

print(calculate_bmi(70, 1.75))
print(calculate_bmi.__doc__)  # Print function documentation

# Example Usage
if __name__ == "__main__":
    # Test various function calls here
    greet()
    greet_person("Alice")
    print(f"\nSum of 10 and 20: {add_numbers(10, 20)}")