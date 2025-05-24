# What is a List in Python?
# A list in Python is a mutable, ordered collection of items that can hold elements of different data types.
# Lists are one of the most versatile and widely used data structures in Python.
# They are defined using square brackets `[]`, and elements are separated by commas.
# Lists allow indexing, slicing, and a variety of operations, making them a powerful tool for data manipulation.

# Key Features of Lists:
# 1. Mutable: Lists can be modified after creation (e.g., adding, removing, or changing elements).
# 2. Ordered: The order of elements is preserved.
# 3. Heterogeneous: Lists can store elements of different data types (e.g., integers, strings, other lists).
# 4. Dynamic: Lists can grow or shrink in size as needed.
# 5. Indexing: Elements can be accessed using positive or negative indexing.
# 6. Slicing: Subsets of lists can be created using slicing syntax.
# 7. Nested: Lists can contain other lists, allowing for complex data structures.
# 8. Comprehension: A concise way to create lists using expressions and loops.
# 9. Methods: Lists have a variety of built-in methods for manipulation (e.g., append, remove, sort).
# 10. Iteration: Lists can be iterated over using loops, allowing for easy access to each element.
# 11. Length: The length of a list can be determined using the `len()` function.
# 12. Membership Testing: Elements can be checked for membership using the `in` and `not in` operators.
# 13. Sorting: Lists can be sorted in ascending or descending order using the `sort()` method.
# 14. Repetition: Lists can be repeated using the `*` operator.
# 15. Concatenation: Lists can be concatenated using the `+` operator.
# 16. Copying: Lists can be copied using the `copy()` method or slicing.
# 17. Clearing: Lists can be cleared using the `clear()` method.


# Example of creating lists:
list1 = [1, 2, 3, 4, 5]  # A list of integers
list2 = ["apple", "banana", "cherry"]  # A list of strings
list3 = [1, "apple", 3.14, True]  # A list with mixed data types
list4 = [1, 2, [3, 4, [7, 8, 9, 12]], 5]  # A nested list

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)
list2,list1.copy()  # Creating a shallow copy of list1
print("Copy of List 1:", list2,list1.copy())

# List Operations:
# 1. Indexing and Slicing
print("First element of list1:", list1[0])  # Accessing the first element
print("Last element of list1:", list1[-1])  # Accessing the last element
print("Slice of list1 (index 1 to 3):", list1[1:4])  # Slicing
print("Nested element from list4:", list4[2][1])  # Accessing nested elements
print("Deeply nested element from list4:", list4[2][2][2])  # Accessing deeply nested elements

# 2. Concatenation and Repetition
list5 = list1 + list2  # Concatenation
print("Concatenated List:", list5)
list6 = list1 * 2  # Repetition
print("Repeated List:", list6)

# 3. Adding and Removing Elements
list1.append(6)  # Add an element to the end
print("After appending 6:", list1)
list1.insert(0, 0)  # Insert an element at a specific index
print("After inserting 0 at index 0:", list1)
list1.remove(3)  # Remove the first occurrence of an element
print("After removing 3:", list1)
list1.pop()  # Remove and return the last element
print("After popping the last element:", list1)
list1.pop(2)  # Remove and return the element at index 2
print("After popping element at index 2:", list1)

# 4. Sorting and Reversing
list1.sort()  # Sort the list in ascending order
print("Sorted List:", list1)
list1.reverse()  # Reverse the order of the list
print("Reversed List:", list1)

# 5. Clearing the List
list1.clear()  # Remove all elements from the list
print("Cleared List:", list1)

# 6. List Comprehension
# List comprehension is a concise way to create lists.
squares = [x**2 for x in range(10)]  # List of squares
print("Squares:", squares)
even_numbers = [x for x in range(10) if x % 2 == 0]  # List of even numbers
print("Even Numbers:", even_numbers)
nested_list = [[x, y] for x in range(3) for y in range(3)]  # Nested list
print("Nested List:", nested_list)

# 7. Membership Testing
print("Is 2 in list1?", 2 in list1)
print("Is 'apple' in list2?", "apple" in list2)

# 8. Copying a List
list_copy = list2.copy()  # Create a shallow copy of the list
print("Copied List:", list_copy)

# 9. Length of a List
print("Length of list2:", len(list2))

# 10. Iterating Through a List
print("Iterating through list2:")
for item in list2:
    print(item)

# Interviewer-Level Notes:
# - Lists are dynamic and mutable, making them suitable for scenarios where frequent modifications are required.
# - They are not hashable and cannot be used as dictionary keys.
# - Use list comprehensions for concise and efficient list creation.
# - Be cautious with nested lists, as modifying one list may affect others if they share references.







