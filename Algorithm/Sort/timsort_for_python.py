"""
* Author : Yonghwan Yim
* Title : Timsort 사용법 (python 내장함수)
"""
"""
* Timsort는 Python sort()와 sorted()가 사용하는 정렬 알고리즘
* Merge Sort + Insertion Sort를 혼합한 하이브리드 정렬
* 실제로 C로 구현되어 있어서 빠름. 현업에서 주로 사용.
* 가급적 파이썬의 내장 함수를 사용하는 것이 실행 속도가 가장 빠름.

* 배열을 작은 run(연속된 정렬된 구간)으로 나눈 뒤,
    - 작은 run은 Insertion Sort로 정렬 (데이터가 적을 때는 Insertion Sort가 빠른 것을 이용)
    - run들을 Merge Sort 방식으로 합쳐서 전체 정렬

* Time Complexity:
    - Best case: O(n)
    - Average case: O(n log n)
    - Worst case: O(n²)

* Space Complexity:
    - O(n) (Merge 과정에서 사용)
"""

"""
* sorted()를 활용한 정렬. 정렬 결과를 리스트로 리턴함 (즉, 원본은 유지)
* sort()와 달리 모든 iterable 객체에 적용 가능 (문자열, 튜플, 딕셔너리 모두 가능)
* sorted()는 'key=옵션'을 통해 정렬을 위한 키 또는 함수를 별도로 지정할 수 있음.
"""
a = [2, 5, 1, 9, 7]
print(sorted(a))
print(sorted(a, reverse=True)) # 내림차순

# 문자도 정렬 가능
b = 'zbdaf'
print(sorted(b))

# key 활용 1
c = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(c, key=len))   # 코드 정렬을 위한 함수로 len(길이) 설정.

# key 활용 2 (함수 정의)
d = ['cde', 'cfc', 'abc', 'akb']
def first_and_last(s):
    return s[0], s[-1]   # 첫 문자열(s[0])과 마지막 문자열(s[-1])을 기준으로 정렬
result_1 = sorted(d, key=first_and_last)
print(result_1)

# key 활용 3 (함수 대신 람다로 정의)
result_2 = sorted(d, key = lambda s : (s[0], s[-1]))
print(result_2)


"""
* list 자료형의 sort()를 활용한 정렬 (list에서만 사용 가능)
* list 자체를 정렬.
* 제자리 정렬(In-place Sort)이므로, 입력을 출력으로 덮어쓰고, 리턴값이 없음 (즉 원본 변경됨)
* 정렬 결과를 별도로 리턴하는 sorted()와 다르므로 주의.
"""
alist = [2, 5, 9, 10, 23, 1]
alist.sort()  # sort()는 None을 리턴하므로, 이걸 다른 변수에 저장하면 안됨
print(alist)

alist.sort(reverse=True) # 내림차순
print(alist)

# 튜플 리스트 두 번째 요소 기준 정렬
tuple_list = [(1, 3), (2, 2), (4, 1)]
tuple_list.sort(key=lambda x: x[1])
print(tuple_list)