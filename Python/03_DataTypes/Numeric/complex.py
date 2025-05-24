# Complex numbers => Numbers with a real and imaginary part
# In Python, complex numbers are written in the form: a + bj
# where 'a' is the real part and 'b' is the imaginary part

# Creating complex numbers
num1 = 3 + 4j  # Direct definition
num2 = complex(2, 5)  # Using complex() function - creates 2 + 5j

# Basic operations with complex numbers
print("Complex number 1:", num1)
print("Complex number 2:", num2)

# Accessing real and imaginary parts
print("\nAccessing parts of complex numbers:")
print("Real part of num1:", num1.real)
print("Imaginary part of num1:", num1.imag)

# Mathematical operations
sum_complex = num1 + num2
diff_complex = num1 - num2
prod_complex = num1 * num2
div_complex = num1 / num2

print("\nMathematical operations:")
print("Sum:", sum_complex)
print("Difference:", diff_complex)
print("Product:", prod_complex)
print("Division:", div_complex)

# Built-in functions for complex numbers
print("\nBuilt-in functions:")
print("Absolute value (magnitude):", abs(num1))  # Returns magnitude of complex number
print("Conjugate of num1:", num1.conjugate())

# Converting string to complex
str_complex = "5+3j"
num3 = complex(str_complex)
print("\nComplex number from string:", num3)

# Note: Complex numbers cannot be compared with < or > operators
# They can only be compared for equality
print("\nEquality comparison:")
print("Is num1 == num2?", num1 == num2)


