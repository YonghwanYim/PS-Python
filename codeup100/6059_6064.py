"""
* Author : Yonghwan Yim
* Final Update : 25.09.09
* Title : CodeUp Python 기초 100제
* Sub : [기초-비트단위논리연산, 3항연산] 6059 ~ 6064
"""

"""
* 6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기
"""
"""
n = int(input())
print(~n)
"""

"""
* 6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기
"""
"""
n1, n2 = map(int, input().split())
print(n1 & n2)
"""

"""
* 6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기
"""
"""
n1, n2 = map(int, input().split())
print(n1 | n2)
"""

"""
* 6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기
"""
"""
n1, n2 = map(int, input().split())
print(n1 ^ n2)
"""

"""
* 6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기
"""
"""
n1, n2 = map(int, input().split())
result = n1 if (n1 >= n2) else n2
print(result)
"""

"""
* 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기
"""
n_list = list(map(int, input().split()))
min_number = n_list[0] if ((n_list[0] <= n_list[1]) and (n_list[0] <= n_list[2])) \
    else (n_list[1] if (n_list[1] <= n_list[2]) else n_list[2])
print(min_number)
