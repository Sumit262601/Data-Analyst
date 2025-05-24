# What is a String in Python?
# A string in Python is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable, meaning their content cannot be changed after creation.
# They are widely used for representing and manipulating text data in Python.

# Key Features of Strings:
# 1. Immutable: Once created, the content of a string cannot be modified.
# 2. Ordered: Strings maintain the order of characters, allowing indexing and slicing.
# 3. Versatile: Strings support a wide range of operations, including concatenation, repetition, formatting, and built-in methods.

# Examples of Creating Strings:
string1 = 'Hello, World!'  # Single quotes
string2 = "Python is awesome!"  # Double quotes
string3 = '''This is a multi-line string.
It can span multiple lines.'''  # Triple quotes
print(string1)  # Output: Hello, World!
print(string2)  # Output: Python is awesome!
print(string3)  # Output: This is a multi-line string. It can span multiple lines.

# String Operations:
# 1. Concatenation
string4 = string1 + " " + string2
print("Concatenated String:", string4)  # Output: Hello, World! Python is awesome!

# 2. Repetition
string5 = string1 * 3
print("Repeated String:", string5)  # Output: Hello, World!Hello, World!Hello, World!

# 3. Indexing and Slicing
print("First character:", string1[0])  # Output: H
print("Last character:", string1[-1])  # Output: !
print("Substring (index 7 to 11):", string1[7:12])  # Output: World

# 4. String Formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted_string)  # Output: My name is Alice and I am 30 years old.

# 5. String Methods
print("Uppercase:", string1.upper())  # Output: HELLO, WORLD!
print("Lowercase:", string1.lower())  # Output: hello, world!
print("Stripped String:", string1.strip())  # Removes leading/trailing whitespace
print("Replaced String:", string1.replace("World", "Python"))  # Output: Hello, Python!
print("Split String:", string1.split(","))  # Output: ['Hello', ' World!']

# 6. Membership Testing
print("Is 'World' in string1?", "World" in string1)  # Output: True
print("Is 'Python' not in string1?", "Python" not in string1)  # Output: True

# 7. Iterating Through a String
print("Characters in string1:")
for char in string1:
    print(char, end=" ")  # Output: H e l l o ,   W o r l d !

# 8. String Length
print("\nLength of string1:", len(string1))  # Output: 13

# 9. Escape Characters
print("Tab Example:\tHello")  # Output: Tab Example:    Hello
print("Newline Example:\nHello")  # Output: Newline Example: (newline) Hello
print("Single Quote Example: \'Hello\'")  # Output: 'Hello'
print("Double Quote Example: \"Hello\"")  # Output: "Hello"
print("Backslash Example: \\Hello\\")  # Output: \Hello\

# 10. String Comparison
print("Equality Check:", string1 == string2)  # Output: False
print("Lexicographical Comparison:", string1 < string2)  # Output: True

# 11. Advanced String Methods
print("Title Case:", string1.title())  # Output: Hello, World!
print("Swap Case:", string1.swapcase())  # Output: hELLO, wORLD!
print("Starts with 'Hello':", string1.startswith("Hello"))  # Output: True
print("Ends with 'World!':", string1.endswith("World!"))  # Output: True

# 12. String Split and Join
split_string = string1.split(", ")
print("Split String:", split_string)  # Output: ['Hello', 'World!']
joined_string = ", ".join(split_string)
print("Joined String:", joined_string)  # Output: Hello, World!

# 13. String Validation
print("Is '123' numeric?", "123".isdigit())  # Output: True
print("Is 'abc' alphabetic?", "abc".isalpha())  # Output: True
print("Is 'abc123' alphanumeric?", "abc123".isalnum())  # Output: True
print("Is '   ' whitespace?", "   ".isspace())  # Output: True

# Interviewer-Level Notes:
# - Strings are immutable, making them thread-safe and efficient for certain operations.
# - Use f-strings for modern and efficient string formatting.
# - Be cautious with large string concatenations; consider using `join()` for better performance.
# - Strings are hashable, making them suitable as dictionary keys or elements in sets.


