# What is a Tuple in Python?
# A tuple is an immutable sequence type in Python, meaning its elements cannot be changed after creation.
# Tuples are used to store multiple items in a single variable and are defined using parentheses `()`.
# Tuples can contain elements of different data types, including other tuples, lists, or dictionaries.
# They are often used to group related data together, such as coordinates (x, y) or RGB color values (red, green, blue).
#
# Key Features of Tuples:
# 1. Immutable: Once created, the elements of a tuple cannot be modified, added, or removed.
# 2. Ordered: Tuples maintain the order of elements, allowing indexing and slicing.
# 3. Heterogeneous: Tuples can store elements of different data types (e.g., integers, strings, other tuples).
# 4. Lightweight: Tuples are generally more memory-efficient than lists, making them suitable for fixed collections of items.
# 5. Hashable: Tuples can be used as keys in dictionaries, while lists cannot.
# 6. Nested: Tuples can contain other tuples, lists, or dictionaries, allowing for complex data structures.
# 7. Packing and Unpacking: Tuples can be packed (grouped together) and unpacked (separated into individual variables).
# 8. Methods: Tuples have a limited set of built-in methods compared to lists, as they are immutable.
# 9. Comprehension: Tuples can be created using tuple comprehension, similar to list comprehension.
# 10. Iteration: Tuples can be iterated over using loops, similar to lists.
# 11. Conversion: Tuples can be converted to lists and vice versa using the `tuple()` and `list()` functions.
# 12. Length: The length of a tuple can be determined using the `len()` function.
# 13. Membership Testing: Elements can be checked for membership using the `in` and `not in` operators.
# 14. Slicing: Tuples can be sliced to create sub-tuples, similar to lists.
# 15. Indexing: Elements can be accessed using positive or negative indexing.
# 16. Repetition: Tuples can be repeated using the `*` operator.
# 17. Concatenation: Tuples can be concatenated using the `+` operator.
# 18. Sorting: Tuples can be sorted using the `sorted()` function, but this creates a new sorted list.
# 19. Comparison: Tuples can be compared using comparison operators, which compare elements lexicographically.
# 20. Memory Efficiency: Tuples are generally more memory-efficient than lists, making them suitable for fixed collections of items.
# They are similar to lists but are immutable, making them useful for data that should not be modified.

# Example of creating a tuple
example_tuple = (1, 2, 3, 4, 5)
print("Example Tuple:", example_tuple)
print(type(example_tuple))  # Output: <class 'tuple'>

# Accessing elements in a tuple
print("First element:", example_tuple[0])
print("Last element:", example_tuple[-1])

# Tuple operations
# 1. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# 2. Repetition
repeated_tuple = tuple1 * 2
print("Repeated Tuple:", repeated_tuple)

# 3. Membership testing
print("Is 2 in tuple1?", 2 in tuple1)
print("Is 7 in tuple1?", 7 in tuple1)

# 4. Slicing
sliced_tuple = example_tuple[1:4]
print("Sliced Tuple (index 1 to 3):", sliced_tuple)

# 5. Length of a tuple
print("Length of example_tuple:", len(example_tuple))

# 6. Iterating through a tuple
print("Iterating through example_tuple:")
for item in example_tuple:
    print(item)

# 7. Tuple unpacking
a, b, c, d, e = example_tuple
print("Unpacked values:", a, b, c, d, e)

# 8. Nested tuples
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[1][1])

# 9. Immutable nature of tuples
try:
    example_tuple[0] = 10  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)

# 10. Converting a list to a tuple
example_list = [1, 2, 3]
converted_tuple = tuple(example_list)
print("Converted Tuple:", converted_tuple)

# 11. Converting a tuple to a list
converted_list = list(example_tuple)
print("Converted List:", converted_list)

# Tuples are often used in scenarios where immutability is required, such as keys in dictionaries or fixed collections of items.

# Interviewer-Level Notes:
# 1. Tuples are immutable, which makes them thread-safe and suitable for use in multi-threaded environments.
# 2. They are hashable if all their elements are hashable, making them ideal for use as dictionary keys or in sets.
# 3. Tuples are faster than lists for iteration and access due to their immutability.
# 4. They are often used to return multiple values from a function in a single call.
# 5. Tuple unpacking can be used to swap variables in a single line: a, b = b, a.
# 6. Be cautious when using mutable objects (like lists) inside tuples, as the tuple itself remains immutable, but the mutable objects can still be modified.
# 7. Tuples are a good choice for representing fixed collections of data, such as database records or configuration settings.
# 8. When comparing tuples, Python compares element by element in lexicographical order, which can be useful for sorting or prioritization.