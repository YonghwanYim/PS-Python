"""
* Author : Yonghwan Yim
* Title : Test
"""
# PEP 8 : Use a def statement instead of an assignment that binds a lambda expression directly to an identifier.

""" 기본 클래스 """
from dataclasses import dataclass
@dataclass
class Rectangle:
    width: int
    height: int
    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())

""" dataclass (python에서 C의 struct 대안) """
from dataclasses import dataclass
@dataclass # dataclass decorator를 붙이면, 자동으로 여러 method 생성 (__init__ 등)
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10
apple.weight = 38
print(apple)


""" 배열 (list) 반복 """
foo = ['A', 'B', 'C']
for f in foo:
    print(f)


""" Python은 generic이 필요 없지만, 가독성을 위해 type 명시 """
from typing import TypeVar

T = TypeVar('T') # <class 'int'>
U = TypeVar('U') # <class 'float'>

def are_equal(a: T, b: U) -> bool:
    return a==b

# Python은 int, float간 비교가 허용되고 값이 같으면 True 반환.
print(are_equal(10, 10.0)) # 따라서 타입이 다르지만 True 출력

# 따라서 객체의 타입은 다르지만 연산은 내부적으로 아래와 같이 이뤄짐.
print(float(10) == 10.0) # True


""" Sum 1~10. Use range() """
sum = sum(range(1, 10+1))
print(sum)