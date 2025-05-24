# Numbers with decimals are known as float data type
# In Python, float is a data type that represents floating-point numbers, which are numbers that have a decimal point.
# Float numbers can be positive or negative, and they can also be represented in scientific notation.
# The float data type is used to represent real numbers, and it is commonly used in mathematical calculations, scientific computations, and data analysis.

# Examples of float data type in Python:
fl_1 = 0.0001  # A small float number
fl_2 = 3.14  # A positive float number
fl_3 = -2.5  # A negative float number
fl_4 = 0.0   # A float number equal to zero
fl_5 = 3.14159  # A float number representing the value of pi
fl_6 = 1.5e3  # A float number in scientific notation (1.5 * 10^3 = 1500.0)
fl_7 = 1.0e-10  # A very small float number in scientific notation (1.0 * 10^-10 = 0.0000000001)

print(fl_1)  # Output: 0.0001
print(fl_2)  # Output: 3.14
print(fl_3)  # Output: -2.5
print(fl_4)  # Output: 0.0
print(fl_5)  # Output: 3.14159
print(fl_6)  # Output: 1500.0
print(fl_7)  # Output: 1e-10

# Float numbers can also be represented in different formats, such as fixed-point notation and scientific notation.
# For example:
fl_8 = 1.23456789e2  # Scientific notation (1.23456789 * 10^2 = 123.456789)
fl_9 = 1.23456789E2  # Scientific notation (1.23456789 * 10^2 = 123.456789, using uppercase 'E')
fl_10 = 1.23456789E-2  # Scientific notation (1.23456789 * 10^-2 = 0.0123456789)

print("\nfl_8")  # Output: 123.456789
print(fl_9)  # Output: 123.456789
print(fl_10)  # Output: 0.0123456789


# Float numbers can also be used in mathematical operations, such as addition, subtraction, multiplication, and division.
# For example:
sum = fl_1 + fl_2  # Adding two float numbers
diff = fl_1 - fl_2  # Subtracting two float numbers
prod = fl_1 * fl_2  # Multiplying two float numbers
quot = fl_1 / fl_2  # Dividing two float numbers
mod = fl_1 % fl_2  # Modulus operation (remainder of division)
exp = fl_1 ** 2  # Exponentiation (raising to the power of 2)

print("\nsum")  # Output: 3.1401
print(diff)  # Output: -3.1399
print(prod)  # Output: 0.000314
print(quot)  # Output: 0.031831746031746032
print(mod)  # Output: 0.0001
print(exp)  # Output: 1e-08


# Float numbers can also be converted to other data types, such as integers and strings.
# For example:
int_num = int(fl_1)  # Converting a float number to an integer (truncating the decimal part)
print("\nint_num")  # Output: 0

str_num = str(fl_1)  # Converting a float number to a string
print("\nstr_num")  # Output: '0.0001'

