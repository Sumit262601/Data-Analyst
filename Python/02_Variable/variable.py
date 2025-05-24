"""
Python Variables:
---------------
1. Variables are containers for storing data values
2. Variables are created when you assign a value using the = operator
3. No need to explicitly declare variables or their type
4. Variable names are case-sensitive
5. Variables can store different data types

Variable Naming Rules:
-------------------
1. Must start with a letter (a-z, A-Z) or underscore (_)
2. Can contain letters, numbers, and underscores
3. Cannot start with a number
4. Cannot use reserved keywords
5. Case-sensitive (age, Age, and AGE are different variables)
"""

# Examples of valid variable names
name = "John"
age = 25
_private = "Hidden"
first_name = "Jane"
lastName = "Doe"
CONSTANT = 3.14

# Examples of invalid variable names (commented out to avoid errors)
# 2name = "Invalid"    # Cannot start with number
# my-name = "Invalid"  # Cannot use hyphen
# class = "Invalid"    # Cannot use reserved keyword

# Multiple assignments
x, y, z = 1, 2, 3
print("Multiple assignments:", x, y, z)

# Same value to multiple variables
a = b = c = 10
print("Same value assignment:", a, b, c)

# Variable types in Python
string_var = "Hello"
integer_var = 42
float_var = 3.14
boolean_var = True
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)
dict_var = {"name": "John", "age": 25}

# Checking variable types
print("\nVariable Types:")
print(f"string_var: {type(string_var)}")
print(f"integer_var: {type(integer_var)}")
print(f"float_var: {type(float_var)}")
print(f"boolean_var: {type(boolean_var)}")
print(f"list_var: {type(list_var)}")
print(f"tuple_var: {type(tuple_var)}")
print(f"dict_var: {type(dict_var)}")

# Variable scope demonstration
global_var = "I am global"

def scope_test():
    local_var = "I am local"
    print("\nInside function:")
    print(f"Local variable: {local_var}")
    print(f"Global variable: {global_var}")

scope_test()
print("\nOutside function:")
print(f"Global variable: {global_var}")
# print(local_var)  # This would raise an error as local_var is not accessible here

# Checking Python keywords (words that cannot be used as variable names)
import keyword
print("\nPython Keywords:")
print(keyword.kwlist)

"""
My Name = sumit
Age = 20
BSC = 7.9

[   'False', 
    'None', 
    'True', 
    'and', 
    'as', 
    'assert', 
    'async', 
    'await', 
    'break', 
    'class', 
    'continue', 
    'def', 
    'del', 
    'elif', 
    'else', 
    'except', 
    'finally', 
    'for', 
    'from', 
    'global', 
    'if', 
    'import', 
    'in', 
    'is', 
    'lambda', 
    'nonlocal', 
    'not', 
    'or', 
    'pass', 
    'raise', 
    'return', 
    'try', 
    'while', 
    'with', 
    'yield'
]

variables value varies to a values

"""