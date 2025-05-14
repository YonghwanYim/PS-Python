"""
* Author : Yonghwan Yim
* Title : Test
"""
# PEP 8 : Use a def statement instead of an assignment that binds a lambda expression directly to an identifier.

"""
range() function.
A typical function that uses the generator approach.
"""


"""
Generator (Python 2.2~)
Use 'yield' to return a generator, and 'next' to retrieve the next value.
"""
def get_natural_number():
    n = 0
    while True:
        n += 1    # After each next() call, the code executes and returns the value using yield.
        yield n

gen = get_natural_number() # Assign the generator object to a variable.
for _ in range(0,10):
    print(next(gen))

def generator():
    # Multiple types of values can be generated in a single function.
    yield 1
    yield 'string'
    yield 'True'

g = generator()
for _ in range(0,3):
    print(next(g))

"""
List Comprehension (Python 2.7~)
Applicable to both lists and dictionaries
"""
a = [n * 2 for n in range(1, 10+1) if n % 2 == 1]
print(a)


""" 
Type Hint (Python 3.5~)
Even when using type hints, they are not enforced at runtime,
so it's important to be aware that values can still be dynamically assigned.
"""
def fn(a: int) -> bool: # use type hint !!
    result = True if a==10 else False  # Reminder : Python's ternary operator has a different order than in C/Java
    return result

"""
class
"""
from dataclasses import dataclass
@dataclass
class Rectangle:
    width: int
    height: int
    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())

"""
dataclass
serves as a lightweight alternative to C structs in Python
"""
from dataclasses import dataclass
@dataclass # The @dataclass decorator automatically generates methods like __init__, etc.
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10
apple.weight = 38
print(apple)

"""
Loop through a list
"""
foo = ['A', 'B', 'C']
for f in foo:
    print(f)

""" 
Python doesn't require generics, but type hints improve readability
"""
from typing import TypeVar

T = TypeVar('T') # <class 'int'>
U = TypeVar('U') # <class 'float'>

def are_equal(a: T, b: U) -> bool:
    return a==b

# Python allows comparisons between int and float; returns True if values are equal
print(are_equal(10, 10.0)) # Types are different, but True is returned
# Although the object types differ, the comparison is internally evaluated like this:
print(float(10) == 10.0)   # True

"""
Sum 1~10. Use range()
"""
sum = sum(range(1, 10+1))
print(sum)