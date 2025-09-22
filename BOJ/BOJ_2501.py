"""
* Author : Yonghwan Yim
* Final update : 25.09.22
* BOJ 2501. 약수 구하기
* https://www.acmicpc.net/problem/2501
"""
"""
* 브루트 포스로 풀어도 O(N)
* N <= 10,000이니, 시간제한 1초면 여유.
"""

import sys
def find_divisors(N, K):
    count = 0
    for i in range(1, N+1):   # 자기 자신도 약수에 포함되니, N+1까지로 해야함.
                              # 처음에 range(1, N)으로 해서 틀림.
        if N % i == 0:  # 나머지가 0이면 약수
            count += 1
        if count >= K:
            return i    # K번째 약수 리턴하고 종료.
    if count < K:
        return 0        # 약수의 개수가 K개보다 적으면, 0 출력

read = sys.stdin.readline # 가독성을 위해 read로 정의
N, K = map(int, read().split())
print(find_divisors(N, K))


