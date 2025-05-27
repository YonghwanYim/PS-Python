"""
* Author : Yonghwan Yim
* Title : Note
"""
# PEP 8 : Use a def statement instead of an assignment that binds a lambda expression directly to an identifier.
import sys
import pprint  # for locals()

"""
locals() [<-> globals()]
Returns a dictionary of the current local symbol table (i.e., local variables and their values)
"""
pprint.pprint(locals())

def example(a : int, b : int) -> int:
    c = a + b
    print(locals()) # Useful for debugging.

example(3, 5)

"""
Use 'pass' to define a placeholder for future implementation
"""
class MyClass(object):
    def method_a(self):
        pass  # placeholder for future implementation.
    def method_b(self):
        print("Method B")

c = MyClass()

"""
print
"""
print('A', 'B', sep=',') # sep parameter
print('aa', end=' ') # Setting the end parameter to a space avoids line breaks between print outputs
print('bb')

# f-string (formated string literal)
idx = 1
fruit = 'Apple'
print(f'{idx + 1} : {fruit}') # Most intuitive.

"""
'//' operator performs floor division (returns the largest whole number less than or equal to the result)
In other words, it returns the integer part of the division (the quotient).
"""
print(5/3)  # 1.66..
print(5//3) # 1
print(5%3)  # Remainder; 2
# divmod() returns both the quotient and the remainder at once.
print(divmod(5, 3))

"""
enumerate returns both the index and the value when iterating over an iterable
"""
a = [1, 2, 3, 2, 45, 2, 5]
print(list(enumerate(a)))

for i, v in enumerate(a):
    print(i, v)


"""
range() function.
A typical function that uses the generator approach (Python 3~).
"""
# Compare memory usage when generating 1 million numbers.
a = [n for n in range(1000000)]
b = range(1000000)

# 'a' holds pre-generated values, while 'b' only defines the condition to generate them; both have the same length
print(len(a) == len(b))
print(type(b)) # <class 'range'>

# Memory usage comparison
sys.getsizeof(a) # 8448728
sys.getsizeof(b) # 48

print(b[999])    # Configured to generate values on-the-fly when accessed by index.

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
Be careful not to overuse it, as it can reduce readability.
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