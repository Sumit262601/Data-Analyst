# Whole numbers without a decimal values
# Integers are whole numbers that can be positive, negative, or zero.
# Integers are represented in Python using the `int` data type.
# They can be used in mathematical operations, comparisons, and other operations.
# Integers are commonly used in programming for counting, indexing, and performing arithmetic calculations.

# Examplers of integers:
int1 = 42
int2 = -7
int3 = 0
int4 = 1234567890

print("Integer 1:", int1)  # Output: Integer 1: 42
print("Integer 2:", int2)  # Output: Integer 2: -7
print("Integer 3:", int3)  # Output: Integer 3: 0
print("Integer 4:", int4)  # Output: Integer 4: 1234567890

# Integer operations:
sum_result = int1 + int2  # Addition
difference_result = int1 - int2  # Subtraction
product_result = int1 * int2  # Multiplication
quotient_result = int1 / int2  # Division
modulus_result = int1 % 3  # Modulus (remainder)
exponent_result = int1 ** 2  # Exponentiation (power)
floor_division_result = int1 // 3  # Floor division

print("\nSum:", sum_result)  # Output: Sum: 35
print("Difference:", difference_result)  # Output: Difference: 49
print("Product:", product_result)  # Output: Product: -294
print("Quotient:", quotient_result)  # Output: Quotient: -6.0
print("Modulus:", modulus_result)  # Output: Modulus: 0
print("Exponent:", exponent_result)  # Output: Exponent: 1764
print("Floor Division:", floor_division_result)  # Output: Floor Division: 14

# Typr Of Data:
print("\nType of int1:", type(int1))  # Output: Type of int1: <class 'int'>

# Type conversion:
float_value = float(int1)  # Convert integer to float
print("\nConverted to float:", float_value)  # Output: Converted to float: 42.0

# Converting float to integer (truncating the decimal part):
int_value = int(float_value)  # Convert float to integer
print("\nConverted back to integer:", int_value)  # Output: Converted back to integer: 42

# Converting string to integer:
string_value = "12345"  # String representation of an integer
int_from_string = int(string_value)  # Convert string to integer
# Note: This will raise a ValueError if the string cannot be converted to an integer.
print("\nConverted from string:", int_from_string)  # Output: Converted from string: 12345

# Converting integer to string:
int_to_string = str(int1)  # Convert integer to string
print("\nConverted to string:", int_to_string)  # Output: Converted to string: '42'

# Converting binary, octal, and hexadecimal to integer:
binary_value = "1010"  # Binary representation of 10
octal_value = "12"  # Octal representation of 10
hexadecimal_value = "E"  # Hexadecimal representation of 10

int_from_binary = int(binary_value, 2)  # Convert binary to integer
int_from_octal = int(octal_value, 8)  # Convert octal to integer
int_from_hexadecimal = int(hexadecimal_value, 16)  # Convert hexadecimal to integer

print("\nConverted from binary:", int_from_binary)  # Output: Converted from binary: 10
print("Converted from octal:", int_from_octal)  # Output: Converted from octal: 10
print("Converted from hexadecimal:", int_from_hexadecimal)  # Output: Converted from hexadecimal: 10


# Integer limits:
# In Python, integers can be arbitrarily large, limited only by available memory.
# However, in other programming languages, there may be limits on the size of integers.
# For example, in C/C++, the size of an integer is typically 4 bytes (32 bits), which limits the range of values.
# In Python, you can work with very large integers without worrying about overflow.

# For example:
large_int = 1234567890123456789012345678901234567890
print("\nLarge integer:", large_int)  # Output: Large integer: 1234567890123456789012345678901234567890

# This is a valid integer in Python, and it can be used in calculations without any issues.
# However, keep in mind that very large integers may consume more memory and processing time.
# Python's int type can handle arbitrarily large integers, so you can work with very large numbers without worrying about overflow.
# However, performance may be affected for extremely large integers.

# In practice, it's important to consider the specific requirements of your application and choose appropriate data types accordingly.
# In summary, integers are a fundamental data type in Python used for representing whole numbers.

# They support various arithmetic operations and can be easily converted to and from other data types like float and string.
# Python's int type can handle very large integers, making it suitable for a wide range of applications.
# Integers are commonly used in programming for counting, indexing, and performing arithmetic calculations.





