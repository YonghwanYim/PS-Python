"""
* Author : Yonghwan Yim
* Final Update : 25.09.09
* Title : CodeUp Python 기초 100제
* Sub : [기초-반복실행구조] 6071 ~ 6076
"""

"""
* 6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기
"""
"""
n = 1
while n != 0:
    n = int(input())
    if n == 0:
        break
    else:
        print(n)
"""

"""
* 6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1
"""
"""
n = int(input())
while (n != 0) and (1 <= n <= 100):
    print(n)
    n -= 1
"""

"""
* 6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2
"""
"""
n = int(input())
while (n != 0) and (1 <= n <= 100):
    n -= 1
    print(n)
"""

"""
* 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
"""
"""
c = input()
for i in range(ord('a'), ord(c) + 1):
    print(chr(i), end=' ')
"""

"""
* 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1
"""
"""
num = int(input())
if 0 <= num <= 100:
    for i in range(0, num+1):
        print(i)
"""

"""
* 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2 (range 쓰는 문제. 사실 위와 동일)
"""
num = int(input())
if 0 <= num <= 100:
    for i in range(0, num+1):
        print(i)