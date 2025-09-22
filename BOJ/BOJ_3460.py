"""
* Author : Yonghwan Yim
* Final update : 25.09.22
* 3460. 이진수
* https://www.acmicpc.net/problem/3460
"""
"""
* [풀이방법 1] bin() + 문자열 방식 (Pythonic)

   - python의 bin() 함수로 문자열 형태로 이진수 받기
   - [::-1]로 문자열 뒤집기 (시간복잡도 O(N))
   - enumerate으로 문자열의 인덱스 접근
   
* [풀이방법 2] 수학적(%, //) 방식 : 효율성 중시

   - 성능과 메모리 효율성에서 이점
   - 문자열 객체를 만들고 변환하는 과정이 없으므로, 숫자가 크거나 반복 횟수가 많은 경우에는 더 효율적   
"""
import sys

# 입력부
read = sys.stdin.readline
T = int(read())  # 테스트 케이스 개수 T 받음
n_list = []      # 테스트 케이스를 저장할 리스트
for i in range(T):
    n_list.append(int(read())) # 테스트 케이스를 개행 기준으로 읽어서 저장

# 풀이방법 1. Pythonic
for n in n_list:
    n_string = bin(n)[2:]  # 10진수를 2진수 문자열 형태로 변환 (bin 함수의 앞에 붙는 0b 제거를 위해 index 2부터 슬라이싱)
    for index, value in enumerate(n_string[::-1]):  # [::-1]로 문자열 뒤집고, enumerate으로 index, value 동시에 가져옴
        if value == '1':  # 1이 있으면, index를 출력.
            print(index, end=' ')
    print('') # 하나의 테스트 케이스 끝나면 개행

# 풀이방법 2. 연산 활용
for n in n_list:
    position = 0
    while n > 0:
        if n % 2 == 1:  # 2로 나눈 나머지가 1이면 position 출력
            print(position, end=' ')
        position += 1   # 자릿수 하나 올림
        n //= 2         # 2로 나눈 나머지 저장 (2진수의 왼쪽으로 shift)
    print('') # 테스트 케이스 하나가 끝나면 개행