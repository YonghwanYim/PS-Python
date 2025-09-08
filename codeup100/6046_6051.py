"""
* Author : Yonghwan Yim
* Final Update : 25.09.08
* Title : CodeUp Python 기초 100제
* Sub : [기초-비트시프트연산, 비교연산] 6046 ~ 6051
"""

"""
* 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기

* python은 float에 대한 비트시프트 연산 허용 x
* 사실 파이썬의 int는 arbitrary-precision integer임, 따라서 메모리가 허용하는 한 큰 숫자도 담을 수 있음.
* 다른 언어의 자료형과 다름
"""
"""
n = int(input())
print(n << 1)
"""

"""
* 6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기
"""
"""
def bit_calculator(n_list):
    for num in n_list:
        if abs(num) > 10:
            print("Invalid Input")
            return
    print(n_list[0] << n_list[1])

num_list = list(map(int, input().split()))
bit_calculator(num_list)
"""

"""
* 6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1
"""
"""
num1, num2 = map(int, input().split())
print(num1 < num2)
"""

"""
* 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2
"""
"""
num1, num2 = map(int, input().split())
print(num1 == num2)

"""

"""
* 6050 : [기초-비교연산] 정수 2개 입력받아 비교하기3
"""
"""
num1, num2 = map(int, input().split())
print(num1 <= num2)
"""

"""
* 6051 : [기초-비교연산] 정수 2개 입력받아 비교하기4
"""
num1, num2 = map(int, input().split())
print(num1 != num2)
