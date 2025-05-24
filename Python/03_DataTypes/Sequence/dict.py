# What is a Dictionary in Python?
# A dictionary in Python is a built-in data type that allows you to store and manage data in key-value pairs.
# It is an unordered, mutable collection that is indexed by keys, which can be of any immutable type (e.g., strings, numbers, tuples).
# A dictionary is a mutable, unordered collection of key-value pairs.
# Each key must be unique and immutable (strings, numbers, or tuples).
# Values can be of any type, including other dictionaries.
# Dictionaries are defined using curly braces {} with key:value pairs.

# Key Features of Dictionaries:
# 1. Mutable: Can be modified after creation
# 2. Unordered: Items have no specific order (in Python < 3.7)
# 3. Dynamic: Can grow or shrink as needed
# 4. Key-Value Pairs: Each item is a pair of key and value
# 5. Unique Keys: Keys must be unique within a dictionary
# 6. Hashable Keys: Keys must be immutable (e.g., strings, numbers, tuples)
# 7. Nested: Can contain other dictionaries, lists, or tuples
# 8. Dictionary Comprehension: Can be created using comprehension syntax
# 9. Methods: Various built-in methods for manipulation (e.g., get, keys, values, items)
# 10. Membership Testing: Check if a key exists using `in` and `not in` operators
# 11. Iteration: Can iterate over keys, values, or key-value pairs
# 12. Length: Use `len()` to get the number of items in a dictionary
# 13. Copying: Can create shallow copies using `copy()` method or `dict()` constructor

# Creating Dictionaries
dict1 = {'name': 'John', 'age': 30, 'city': 'New York',}  # Using curly braces
dict2 = dict(name='Alice', age=25, city='London')  # Using dict() constructor
dict3 = dict([('name', 'Bob'), ('age', 35)],  add="west delhi", city="Delhi")  # From sequence of pairs

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)

# Dictionary Operations:
# 1. Accessing Values
print("Name:", dict1['name'])  # Using square bracket notation
print("Age:", dict1.get('age'))  # Using get() method
print("Country:", dict1.get('country', 'Not Found'))  # With default value

# 2. Modifying Dictionaries
dict1['age'] = 31  # Updating existing value
dict1['country'] = 'USA'  # Adding new key-value pair
print("Modified Dictionary:", dict1)

# 3. Dictionary Methods
# Adding/Updating multiple items
dict1.update({'email': 'john@example.com', 'phone': '123-456-7890'})
print("After update:", dict1)

# Removing items
removed_value = dict1.pop('phone')  # Remove specific key
print("Removed value:", removed_value)
last_item = dict1.popitem()  # Remove last item
print("Last removed item:", last_item)
dict1.clear()  # Remove all items
print("Cleared dictionary:", dict1)

# 4. Dictionary Views
dict2_keys = dict2.keys()  # Get all keys
dict2_values = dict2.values()  # Get all values
dict2_items = dict2.items()  # Get all key-value pairs
print("Keys:", dict2_keys)
print("Values:", dict2_values)
print("Items:", dict2_items)

# 5. Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print("Squares dictionary:", squares)

# 6. Nested Dictionaries
nested_dict = {
    'person1': {'name': 'John', 'age': 30},
    'person2': {'name': 'Alice', 'age': 25}
}
print("Nested dictionary:", nested_dict)
print("Person1's name:", nested_dict['person1']['name'])

# 7. Membership Testing
print("Is 'name' in dict2?", 'name' in dict2) # Check if key exists
print("Is 'country' in dict2?", 'country' not in dict2) # Check if key does not exist

# Copying a dictionary using dict() constructor
dict_copy2 = dict(dict2)  # Shallow copy
print("Copied dictionary using dict():", dict_copy2)

# 8. Dictionary Methods of copying
new_dict = dict2.copy()  # Create a shallow copy
print("Copy of dict2:", new_dict)

# 9. Dictionary Length
print("Length of dict2:", len(dict2))

# 10. Iterating Through Dictionaries
print("\nIterating through dict2:")
for key in dict2:
    print(f"Key: {key}, Value: {dict2[key]}")

print("\nIterating through items:")
for key, value in dict3.items():
    print(f"Key: {key}, Value: {value}")

# Interviewer-Level Notes:
# - Dictionary keys must be immutable and unique
# - Time complexity for average case operations is O(1)
# - Use dict.get() to safely access values with default fallback
# - Since Python 3.7, dictionaries maintain insertion order
# - Be cautious with mutable values as dictionary values
# - Memory usage is higher compared to lists due to hash table implementation