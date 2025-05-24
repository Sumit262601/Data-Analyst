"""
What is Slicing in Python?
Slicing is a powerful feature in Python that allows you to extract a portion of a sequence (lists, tuples, strings).
The syntax for slicing is sequence[start:stop:step], where:
- start: the beginning index (inclusive)
- stop: the ending index (exclusive)
- step: the increment between each item
All these parameters are optional, and you can use negative values as well.
Understanding slicing is essential for efficient data manipulation in Python.
"""

# Basic Slicing in Python
my_list = [1, 2, 3, 4, 5]
# Basic slicing [start:stop]
print(my_list[1:4])    # Output: [2, 3, 4]
print(my_list[:3])     # Output: [1, 2, 3]
print(my_list[2:])     # Output: [3, 4, 5]

# Slicing with step
print(my_list[::2])    # Output: [1, 3, 5]
print(my_list[::-1])   # Output: [5, 4, 3, 2, 1]

# Advanced Slicing Examples
# String slicing
text = "Python Programming"
print("First word:", text[:6])        # Output: Python
print("Reversed:", text[::-1])        # Output: gnimmargorP nohtyP
print("Every second character:", text[::2])  # Output: Pto rgamn
print("Substring:", text[7:9])         # Output: Pro

# List slicing with negative indices
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[-3:])    # Output: [3, 4, 5]
print(numbers[:-2])    # Output: [0, 1, 2, 3]

# Common Interview Questions and Answers

# Q1: What happens if slice index is out of range?
# A1: Unlike indexing, slicing with out-of-range indices works fine
long_list = [1, 2, 3]
print(long_list[1:10])  # Output: [2, 3]

# Q2: How does step value work in slicing?
# A2: Step determines the increment between items
nums = [0, 1, 2, 3, 4, 5]
print(nums[::2])       # Output: [0, 2, 4]
print(nums[1::2])      # Output: [1, 3, 5]

# Q3: How to modify multiple elements using slicing?
# A3: Slice assignment is possible with lists
mutable_list = [1, 2, 3, 4, 5]
mutable_list[1:4] = [20, 30, 40]
print(mutable_list)    # Output: [1, 20, 30, 40, 5]

if __name__ == "__main__":
    # Run all examples
    pass


"""
Python Slicing Guide with Interview Questions

Q: What's the difference between slicing and indexing?
A: Slicing extracts a range of elements while indexing accesses a single element.

Q: What happens when you use a negative step in slicing?
A: It reverses the direction of slicing, useful for reversing sequences.

Q: Can you modify a string using slicing?
A: No, strings are immutable. Slicing creates a new string.

Q: What's the advantage of using slicing over a loop?
A: Slicing is more concise and often more efficient than using loops.

Q: What happens when slice indices are out of range?
A: Python adjusts them automatically to fit within sequence bounds.
"""