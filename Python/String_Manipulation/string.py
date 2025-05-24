"""
String manipulation functions for various purposes.
This module provides functions to manipulate strings, including:
- `remove_special_characters`: Removes special characters from a string.
- `remove_extra_spaces`: Removes extra spaces from a string.
- `remove_punctuation`: Removes punctuation from a string.
- `remove_numbers`: Removes numbers from a string.
- `remove_whitespace`: Removes whitespace from a string.
- `remove_html_tags`: Removes HTML tags from a string.
- `remove_accents`: Removes accents from a string.
- `remove_unicode`: Removes unicode characters from a string.
- `remove_links`: Removes links from a string.
- `remove_emails`: Removes email addresses from a string.
- `remove_usernames`: Removes usernames from a string.
- `remove_hashtags`: Removes hashtags from a string.
- `remove_mentions`: Removes mentions from a string.
- `remove_repeated_characters`: Removes repeated characters from a string.

"""

# Create a string variable
name="String_Manipulation"
print(name)

# How to concatenate two strings
firatName = "Sumit"
LastName = "Kumar"
print(firatName, "" + LastName + '\n')

# How to access a strign character

# print(name[3]) # Accessing the 3rd character of the string
# print(name[6:8]) # Accessing the 6th and 7th character of the string
# print(name[0:5]) # Accessing the 0th to 5th character of the string

# # print(name[0:8:1]) # 0 to 5 with step of 1
# print(name[0:8:2]) # 0 to 5 with step of 2
# print(name[::2]) # 0 to end with step of 2

# print(name[::-1]) # Reverse the string
# print(name[::-2]) # Reverse the string with step of 2

# How to replace a string
print(name.replace("String", "Manipulation")) # Replace String with Manipulation

name2 = "Currently I am learning Python"
print(len(name2))

number = 10
print(number)
print(type(number))


number2 = str(number)
print(str(number2))
print(type(number2))
