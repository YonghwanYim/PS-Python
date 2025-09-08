"""
* Author : Yonghwan Yim
* Final Update : 25.09.08

* Title : CodeUp Python 기초 100제
* Sub : [기초-입출력] 6009 ~ 6024
"""

"""
* 6009. [기초-입출력] - 문자 1개 입력받아 그대로 출력하기
"""
"""
c = input()
print(c)
"""

"""
* 6010 : [기초-입출력] 정수 1개 입력받아 int로 변환하여 출력하기
"""
"""
c = int(input())
print(c)
"""

"""
* 6011 : [기초-입출력] 실수 1개 입력받아 변환하여 출력하기
"""
"""
c = float(input())
print(c)
"""

"""
* 6012 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기1
"""
"""
num1 = int(input())
num2 = int(input())
print(num1)
print(num2)
"""

"""
* 6013 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기1
"""
"""
char1 = input()
char2 = input()
print(char2)
print(char1)
"""

"""
* 6014 : [기초-입출력] 실수 1개 입력받아 3번 출력하기
"""
"""
num = float(input())
for i in range(3):
    print(num)
"""

"""
* 6015 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기2
"""
"""
num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(num1)
print(num2)
"""

"""
* 6016 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기2
"""
"""
c1, c2 = input().split()
print(c2, c1)
"""

"""
* 6017 : [기초-입출력] 문장 1개 입력받아 3번 출력하기
"""
"""
s = input()
print(s, s, s)
"""

"""
* 6018 : [기초-입출력] 시간 입력받아 그대로 출력하기
"""
"""
min, sec = input().split(':')
print(min, sec, sep=':')
"""

"""
* 6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기
"""
"""
year, month, day = input().split('.')
print(day, month, year, sep='-')
"""

"""
* 6020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
"""
"""
birth, indicator = input().split('-')
print(birth + indicator)
"""

"""
* 6021 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기
"""
"""
s = input()
for element in s:
    print(element)
"""

"""
* 6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기
"""
"""
birth = input()
year, month, day = birth[0:2], birth[2:4], birth[4:]
print(year, month, day)
"""

"""
* 6023 : [기초-입출력] 시분초 입력받아 분만 출력하기
"""
"""
h, m, s = input().split(':') # h:m:s
print(m)
"""

"""
* 6024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기
"""
word1, word2 = input().split()
s = word1 + word2
print(s)