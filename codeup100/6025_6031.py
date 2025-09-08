"""
* Author : Yonghwan Yim
* Final Update : 25.09.08
* Title : CodeUp Python 기초 100제
* Sub : [기초-값변환, 출력변환] 6025 ~ 6031
"""

"""
* 6025 : [기초-값변환] 정수 2개 입력받아 합 계산하기
"""
#print(sum(map(int, input().split())))

"""
* 6026 : [기초-값변환] 실수 2개 입력받아 합 계산하기
"""
"""
num1 = float(input())
num2 = float(input())
print(num1 + num2)
"""

"""
* 6027 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1
"""
"""
num = int(input())
print(f'{num:x}') # 16진수
"""

"""
* 6028 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2
"""
"""
num = int(input())
print(f'{num:X}')
"""

"""
* 6029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기
"""
"""
num_x = input()
num_d = int(num_x, 16)
print(f'{num_d:o}')
"""

"""
* 6030 : [기초-값변환] 영문자 1개 입력받아 10진수로 변환하기
"""
"""
uni_n = ord(input())   # ord()-> ASCII 값 구해줌.
print(uni_n)
"""

"""
* 6031 : [기초-값변환] 정수 입력받아 유니코드 문자로 변환하기
"""
num = int(input())
print(chr(num))      # chr() -> ASCII 코드에 해당되는 문자로