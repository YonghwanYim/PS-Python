"""
* Author : Yonghwan Yim
* Final Update : 25.09.08
* Title : CodeUp Python 기초 100제
* Sub : [기초-논리연산] 6052 ~ 6058
"""

"""
* 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기
"""
"""
n = int(input())
print(bool(n))
"""

"""
* 6053 : [기초-논리연산] 참 거짓 바꾸기
"""
"""
n = int(input())
print(bool(not n))
"""

"""
* 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기
"""
"""
n1, n2 = map(int, input().split())
print(bool(n1) and bool(n2))
"""

"""
* 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기
"""
"""
n1, n2 = map(int, input().split())
print(bool(n1) or bool(n2))
"""

"""
* 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기
"""
"""
n1, n2 = map(int, input().split())
print(bool(n1) != bool(n2))
"""

"""
* 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
"""
"""
n1, n2 = map(int, input().split())
print(bool(n1) == bool(n2))
"""

"""
* 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
"""
n1, n2 = map(int, input().split())
indicator = (not bool(n1)) and (not bool(n2))
print(indicator)