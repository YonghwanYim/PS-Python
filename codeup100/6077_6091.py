"""
* Author : Yonghwan Yim
* Final Update : 25.09.09
* Title : CodeUp Python 기초 100제
* Sub : [기초-종합] 6077 ~ 6091
"""

"""
* 6077 : [기초-종합] 짝수 합 구하기
"""
"""
n = int(input())
even_sum = 0

for i in range(0, n+1):
    if i % 2 == 0:
        even_sum += i
print(even_sum)
"""

"""
* 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
"""
"""
c = 'a'
while c != 'q':
    c = input()
    print(c)
"""

"""
* 6079 : [기초-종합] 언제까지 더해야 할까?
"""
"""
num = int(input())
if 0 <= num <= 1000:
    sum_result = 0
    index = 0
    while not (sum_result >= num):
        index += 1
        sum_result += index
    print(index)
"""

"""
* 6080 : [기초-종합] 주사위 2개 던지기
"""
"""
n1, n2 = map(int, input().split())
if ((1 <= n1 <= 10) and (1 <= n2 <= 10)):
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            print(i, j)
else:
    print('invalid input')
"""

"""
* 6081 : [기초-종합] 16진수 구구단 출력하기
"""
"""
hex_n = input()
decimal_num = int(hex_n, 16)
for i in range(1, 16):  # 원래 16진수는 0부터
    print(f"{decimal_num:X}*{i:X}={decimal_num * i:X}", sep='')
"""

"""
* 6082 : [기초-종합] 3 6 9 게임의 왕이 되자
"""
"""
n = int(input())
if 1 <= n <= 29:
    for i in range(1, n+1):
        if (i % 10) in [3, 6, 9]:
            print('X')
        else:
            print(i)
"""

"""
* 6083 : [기초-종합] 빛 섞어 색 만들기
"""
"""
r, g, b = map(int, input().split())
count = 0
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
            count += 1
print(count)
"""

"""
* 6084 : [기초-종합] 소리 파일 저장용량 계산하기
"""
"""
h, b, c, s = map(int, input().split())    # h : Hz, b : bit, c : channel, s : sec
mb = (h * b * c * s) / (8 * 1024 * 1024)  # It means MB
print(f"{mb:.1f} MB")
"""

"""
* 6085 : [기초-종합] 그림 파일 저장용량 계산하기
"""
"""
w, h, b = map(int, input().split())
storage = (w * h * b) / (8 * 1024 * 1024)
print(f"{storage:.2f} MB")
"""

"""
* 6086 : [기초-종합] 거기까지! 이제 그만~
"""
"""
n = int(input())
index = 0
result = 0
while not (result >= n):
    index += 1
    result += index
print(result)
"""

"""
* 6087 : [기초-종합] 3의 배수는 통과
"""
"""
n = int(input())
if (1 <= n <= 100):
    for i in range(1, n+1):
        if (i % 3) != 0:
            print(i, end=' ')
"""

"""
* 6088 : [기초-종합] 수 나열하기1 (등차수열)
"""
"""
a, d, n = map(int, input().split())
result = a + d * (n-1)
print(result)
"""

"""
* 6089 : [기초-종합] 수 나열하기2 (등비수열)
"""
"""
a, r, n = map(int, input().split())
result = a * (r ** (n-1))
print(result)
"""

"""
* 6090 : [기초-종합] 수 나열하기3
"""
"""
a, m, d, n = map(int, input().split())
result = a
for i in range(1, n):
    result = result * m + d # 점화식 그대로 적음. O(n) 알고리즘. n이 클 경우 점화식을 공식으로 유도하면 O(log n) 달성 가능.
print(result)
"""

"""
* 6091 : [기초-종합] 함께 문제 푸는 날 
"""
# 최소공배수 문제 다르게 접근해서 풀기
a, b, c = map(int, input().split())
d = 1
while (d % a != 0) or (d % b != 0) or (d % c != 0):
    d += 1
print(d)






