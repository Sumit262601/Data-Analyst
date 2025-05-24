# Python and NumPy Interview Guide

## Python History and Evolution

Python was created by Guido van Rossum and was first released in 1991. Here's its evolution:

- **1989:** Guido van Rossum starts writing Python
- **1991:** Python 0.9.0 released
- **1994:** Python 1.0 released
- **2000:** Python 2.0 released (List comprehensions, garbage collection)
- **2008:** Python 3.0 released (Major revision, not backward compatible)
- **2020:** Python 2 officially retired
- **Present:** Python is one of the most popular programming languages

Key Features that Made Python Popular:
- Simple and readable syntax
- Extensive standard library
- Large ecosystem of third-party packages
- Strong community support
- Versatility (web, data science, AI, automation)

## Python Interview Questions (Basic to Advanced)

### Basic Level Questions

#### Q1: What are the key features of Python?
**Answer:**
- Interpreted language
- Dynamically typed
- Object-oriented
- High-level language
- Large standard library
- Easy to learn and read
- Platform independent

#### Q2: What is PEP 8?
**Answer:** PEP 8 is Python's style guide. It provides coding conventions for writing Python code, including:
- Indentation (4 spaces)
- Line length (79 characters)
- Imports organization
- Naming conventions
- Comments style

#### Q3: What is the difference between lists and tuples?
**Answer:**
```python
# Lists: Mutable, slower, more memory
my_list = [1, 2, 3]
my_list[0] = 4  # Valid

# Tuples: Immutable, faster, less memory
my_tuple = (1, 2, 3)
my_tuple[0] = 4  # TypeError
```

#### Q4: Explain Python's memory management
**Answer:**
- Python uses reference counting for memory management
- Has a garbage collector for circular references
- Memory allocation through private heap space
- Built-in memory management with `del` keyword

### Intermediate Level Questions

#### Q5: What are decorators in Python?
**Answer:**
```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

#### Q6: Explain context managers and the with statement
**Answer:**
```python
# Using context manager
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closes

# Creating context manager
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
```

#### Q7: What are generators and how do they work?
**Answer:**
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib = fibonacci()
for _ in range(5):
    print(next(fib))  # 0, 1, 1, 2, 3
```

### Advanced Level Questions

#### Q8: Explain metaclasses in Python
**Answer:**
```python
class MyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Add methods or attributes to class
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMetaclass):
    pass
```

#### Q9: How does the GIL (Global Interpreter Lock) work?
**Answer:**
- GIL is a mutex that protects access to Python objects
- Only allows one thread to execute Python bytecode at a time
- Affects CPU-bound tasks more than I/O-bound tasks
- Can be bypassed using multiprocessing

#### Q10: Explain Python's descriptor protocol
**Answer:**
```python
class Descriptor:
    def __get__(self, obj, owner=None):
        return self._value
    
    def __set__(self, obj, value):
        self._value = value
    
    def __delete__(self, obj):
        del self._value
```

#### Q11: What are coroutines and how do they work with async/await?
**Answer:**
```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
```

### Expert Level Questions

#### Q12: How would you implement a thread-safe singleton?
**Answer:**
```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

#### Q13: Explain Python's method resolution order (MRO)
**Answer:**
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# Output: (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

#### Q14: How would you implement a custom iterator?
**Answer:**
```python
class CustomIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter - 1
        raise StopIteration
```

### Common Python Coding Tasks

#### Q15: Implement a decorator that measures function execution time
**Answer:**
```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
```

#### Q16: Write a context manager for database connections
**Answer:**
```python
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def __enter__(self):
        self.conn = self.connect()
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_type:
            return False  # Reraise exception
        return True
```

Remember these Python interview tips:
1. Always discuss time and space complexity
2. Mention potential edge cases
3. Consider thread safety when relevant
4. Explain your thought process
5. Discuss alternative approaches
6. Know the Python standard library well
7. Be familiar with common design patterns

# Python NumPy Indexing and Slicing Guide

## Files Overview
- `access.py`: Basic indexing operations
- `slicing.py`: Array slicing operations
- `fancy.py`: Fancy indexing with NumPy

## 1. Basic Indexing (access.py)
Basic indexing allows accessing single elements using integer indices.

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[0])     # First element
print(my_list[-1])    # Last element
```

## 2. Slicing (slicing.py)
Slicing allows extracting subsequences using `start:stop:step` syntax.

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])    # Elements from index 1 to 3
print(my_list[::-1])   # Reverse the list
```

## 3. Fancy Indexing (fancy.py)
NumPy's advanced indexing features for array manipulation.

### Basic Fancy Indexing
```python
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])    # Select multiple elements: [10 30 50]
```

### Boolean Masking
```python
data = np.array([1, 2, 3, 4, 5, 6])
mask = data > 3
print(data[mask])      # Elements greater than 3: [4 5 6]
```

### 2D Array Indexing
```python
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(matrix[[0, 2]])  # Select first and third rows
```

## Best Practices

### Indexing Best Practices
1. Always check index bounds
2. Use negative indices carefully
3. Handle IndexError exceptions

### Slicing Best Practices
1. Use clear slice parameters
2. Avoid modifying slices of mutable sequences
3. Consider memory usage with large slices

### Fancy Indexing Best Practices
1. Verify index bounds
2. Use boolean masking for filtering
3. Be careful with duplicate indices
4. Consider memory efficiency
5. Combine with regular indexing when appropriate

## Common Interview Questions

### Indexing Questions
- Difference between positive and negative indexing
- Handling index out of range errors
- Working with multi-dimensional arrays

### Slicing Questions
- Difference between slicing and indexing
- Understanding step parameter
- Modifying slices vs. creating copies

### Fancy Indexing Questions
- NumPy fancy indexing vs. regular indexing
- Boolean masking applications
- Performance considerations

## Installation Requirements
```bash
pip install numpy
```

## Running the Examples
1. Open Visual Studio Code
2. Navigate to the project directory
3. Run individual files:
```bash
python access.py
python slicing.py
python fancy.py
```
