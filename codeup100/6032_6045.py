"""
* Author : Yonghwan Yim
* Final Update : 25.09.08
* Title : CodeUp Python 기초 100제
* Sub : [기초-산술연산, 값변환] 6032 ~ 6045
"""



"""
* 6032 : [기초-산술연산] 정수 1개 입력받아 부호 바꾸기
"""
"""
num = int(input())
print(-num)
"""

"""
* 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기
"""
"""
c = input()
num_c = ord(c)             # 문자 -> 아스키코드 변환
print(chr(num_c + 1))      # 다음 문자 출력
"""

"""
* 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기
"""
"""
num1, num2 = map(int, input().split())
print(num1 - num2)
"""

"""
* 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기
"""
"""
f1, f2 = map(float, input().split())
print(f1 * f2)
"""

"""
* 6036 : [기초-산술연산] 단어 여러 번 출력하기
"""
"""
word, num = input().split()
print(word * int(num))
"""

"""
* 6037 : [기초-산술연산] 문장 여러 번 출력하기
"""
"""
num = int(input())
s = input()
print(s * num)
"""

"""
* 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기
"""
"""
n1, n2 = map(int, input().split())
n3 = n1 ** n2
print(n3)
"""

"""
* 6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기
"""
"""
n1, n2 = map(float, input().split())
n3 = n1 ** n2
print(n3)
"""

"""
* 6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기
"""
"""
n1, n2 = map(int, input().split())
print(n1 // n2)
"""

"""
* 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기
"""
"""
n1, n2 = map(int, input().split())
print(n1 % n2)                               # % : remainder
"""

"""
* 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기
"""
"""
f1 = float(input())
print(f"{f1:.2f}")
"""

"""
* 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기
"""
"""
f1, f2 = map(float, input().split())
result = f1 / f2
print(f"{result:.3f}")
"""

"""
* 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기
"""
"""
num1, num2 = map(int, input().split())
if num2 == 0:  # 0으로 나눠지는 것 방지
    print("Invalid Input")

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)
print(f"{num1/num2:.2f}")
"""

"""
* 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
"""
num_list = list(map(int, input().split()))   # map -> list
print(f"{sum(num_list)} {sum(num_list)/len(num_list):.2f}")