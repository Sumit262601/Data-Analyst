"""
What is Indexing in Python?
Indexing is a fundamental concept in Python that allows you to access elements in sequences like lists, tuples, and strings.
Indexing refers to accessing a single element in a sequence using its position (index).
Indexing starts at 0, so the first element is at index 0, the second at index 1, and so on. Negative indexing allows you to access elements from the end of the sequence, where -1 refers to the last element, -2 to the second last, and so forth.
Indexing is a powerful tool in Python that allows for efficient data access and retrieval. Understanding this concept is crucial for effective programming in Python, especially when dealing with data structures like lists, tuples, and strings.
"""

# Basic Indexing in Python
my_list = [1, 2, 3, 4, 5]
# Positive indexing (starts from 0)
print(my_list[0])  # Output: 1
print(my_list[4])  # Output: 5

# Negative indexing (starts from -1)
print(my_list[-1])  # Output: 5
print(my_list[-2])  # Output: 4

# Advanced Indexing Examples
# Multi-dimensional list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix element:", matrix[1][2])  # Output: 6

# String indexing
text = "Python"
print("First character:", text[0])      # Output: P
print("Last character:", text[-1])      # Output: n
print("Substring:", text[1:4])         # Output: yth

# Common Interview Questions and Answers

# Q1: What happens if index is out of range?
# A1: Raises IndexError
try:
    print(my_list[10])
except IndexError as e:
    print("Index out of range!")

# Q2: Can you explain negative indexing in Python?
# A2: Negative indices start from the end of the sequence
example = [1, 2, 3, 4]
print(example[-1])    # Output: 4 (last element)
print(example[-2])    # Output: 3 (second to last element)

# Q3: How to access elements in a multi-dimensional list?
# A3: Use multiple square brackets or chain the index operators
grid = [[1, 2], [3, 4]]
print(grid[0][1])    # Output: 2

if __name__ == "__main__":
    # Run all examples
    pass


"""
Python Indexing Guide with Interview Questions

Q: What's the difference between positive and negative indexing?
A: Positive indexing starts from the beginning (0) and counts forward, while negative indexing starts from the end (-1) and counts backward.

Q: What happens when you try to access an index that doesn't exist?
A: Python raises an IndexError exception.

Q: How does indexing work with strings?
A: Strings can be indexed just like lists, with both positive and negative indices.

Q: Is it possible to modify a string using indexing?
A: No, strings are immutable in Python. You cannot modify individual characters using indexing.

Q: What's the time complexity of accessing an element by index in a list?
A: O(1) - constant time, as it provides direct access to the element.
"""