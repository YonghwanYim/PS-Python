"""
* Author : Yonghwan Yim
* Final Update : 25.09.09
* Title : CodeUp Python 기초 100제
* Sub : [기초-조건/선택 실행구조] 6065 ~ 6070
"""

"""
* 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
"""
"""
n_list = list(map(int, input().split()))
for num in n_list:
    if (num % 2) == 0:
        print(num)
"""

"""
* 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
"""
"""
n_list = list(map(int, input().split()))
for num in n_list:
    if (num % 2) == 0: # it means even number
        print('even')
    else:              # it means odd number
        print('odd')
"""

"""
* 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기
"""
"""
n = int(input())
if n < 0:
    if (n % 2) == 0:  # it means even & negative number
        print('A')
    else:             # odd & negative
        print('B')
else:
    if (n % 2) == 0:  # even & positive number
        print('C')
    else:             # odd & positive
        print('D')
"""

"""
* 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기
"""
"""
score = int(input())
if (0 <= score <= 100):
    if score >= 90:
        print('A')
    elif score >= 70:
        print('B')
    elif score >= 40:
        print('C')
    else:
        print('D')
else:
    print('invalid input (must be 0~100)')
"""

"""
* 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
"""
"""
c = input()
match c.upper():
    case 'A':
        print('best!!!')
    case 'B':
        print('good!!')
    case 'C':
        print('run!')
    case 'D':
        print('slowly~')
    case _:  # wildcard (default)
        print('what?')
"""

"""
* 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
"""
month = int(input())

match month:
    case 3 | 4 | 5:
        print('spring')
    case 6 | 7 | 8:
        print('summer')
    case 9 | 10 | 11:
        print('fall')
    case 12 | 1 | 2:
        print('winter')
    case _:
        print('invalid input')
