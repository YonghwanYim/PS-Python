"""
* Author : Yonghwan Yim
* Title : Essential Python Data Structures for Coding Tests
"""

"""
1. List *********************************************************

* 데이터에 인덱스로 빠르게 접근해야 할 때 좋음

* 활용법
   - Stack(LIFO) 구현시 사용
   - pop(0)는 O(N)이라 매우 느리니 쓰지 말자. 차라리 데크를 쓰면 됨.

* 핵심 연산
   - append(value) : 맨 뒤에 값 추가;    O(1)
   - pop() : 맨 뒤의 값 꺼내기;           O(1)    
   - my_list[i] : i번째 값 접근;         O(1)
   - value in my_list : 값이 있는지 확인; O(N)
"""
scores = [90, 85, 100]
scores.append(70)  # [90, 85, 100, 70]
last_score = scores.pop()  # last_score = 70, scores = [90, 85, 100]
print(scores[1])  # 85


"""
2. Dictionary ****************************************************

* Key-Value 쌍으로 데이터 저장하는 자료구조 (다른 언어의 HashMap, HashTable)
* 탐색 속도가 매우 빠름. Key를 통해 Value에 매우 빠르게 접근 가능
* Python 3.7+ 부터는 입력된 순서가 유지

* 활용법
   - 데이터에 Key를 붙여 관리하거나, Counting 할 때 많이 사용 (당연히 Key는 중복 x)
   - 특히 탐색이 매우 빨라야 할 때도 사용

* 핵심 연산
   - my_dict[key] = value : 값 추가/수정;     O(1)
   - my_dict[key] : 값 조회;                 O(1)
   - key in my_dict : Key가 있는지 확인;       O(1)
"""
ages = {'Alice' : 25, 'Bob' : 30}
ages['Yong'] = 32   # {'Alice' : 25, 'Bob' : 30, 'Yong' = 32}
print(ages['Yong'])

if 'Bob' in ages:  # Bob이 있는지 확인
    print("Bob's age is", ages['Bob'])


"""
3. Tuple **********************************************************

* 튜플은 불변(immutable) 자료구조로, 한 번 생성된 후에는 값을 변경할 수 없음
* 해시 가능한 특성을 가져 딕셔너리의 키로 사용할 수 있음
* 그냥 ()로 감싸거나, 쉼표로 값을 나열하는 것으로 생성할 수 있음

* 활용법
   - 데이터를 묶어서 잠시 보관하거나, 변하지 않는 묶음으로 사용할 때 중요함
   - 딕셔너리의 Key 또는 Set의 원소로 사용 (둘 다 immutable 해야함)
   - 특히 이런 특징은 좌표 평면이나 그래프 문제에서 방문 여부 기록할 때 유용함
   - BFS나 다익스트라 같은 알고리즘에서는 (거리, 노드), (x, y, z)처럼 여러 정보를 한 덩어리로 묶어서 큐나 힙에 넣어야 함. 이럴 때 유용
   - 파이썬 함수는 기본적으로 여러 값을 동리에 return하면 이를 튜플로 묶어서 반환함
"""
pos1 = (3, 5)   # 일반적인 튜플 생성 방법
pos2 = 4, 5, 6  # 괄호 없이 쉼표로도 튜플 생성 가능 (Tuple Packing)
print(pos1)  # (3, 5)
print(pos2)  # (4, 5, 6)

# 원소가 하나인 튜플은 꼭 뒤에 쉼표를 붙어야 함. 쉼표 안붙이면 그냥 숫자가 됨
single_tuple = (1,)
not_a_tuple = (1)
print(type(single_tuple))
print(single_tuple)  # (1,)
print(type(not_a_tuple))

# Indexing & Slicing : List와 완전히 같음
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])  # 'a'
print(t[-1]) # 'e' (마지막 원소)
print(t[2:4]) # ('c', 'd')  # 슬라이싱의 범위 주의. end index는 결과에 포함되지 않음.

# 튜플 풀기
x, y = pos1  # 튜플의 원소를 x, y 변수에 각각 할당
print(f"x: {x}, y: {y}") # x : 3, y : 5

# 값 교환(swap)도 간단하게 가능
a, b = 10, 20
a, b = b, a       # (b, a)로 tuple을 만들어서 a, b에 할당하는 원리. 정렬 알고리즘 구현할 때 많이 씀
print(f"a: {a}, b: {b}")


"""
4. Set ************************************************************

* 중복을 허용하지 않는 값들의 모음. 
* 딕셔너리처럼 내부적으로 해시를 사용해서 탐색과 추가/삭제가 매우 빠름

* 활용법
   - 리스트에서 중복된 값 제거할 때 사용
   - 특정 값이 존재하는지 빠르게 확인할 때 사용
   - 두 데이터 그룹의 교집합, 합집합, 차집합 등을 구할 때 사용

* 핵심 연산
   - add(value) : 값 추가;              O(1)
   - remove(value) : 값 삭제;           O(1)
   - value in my_set : 값이 있는지 확인;   O(1)
"""
my_list = [1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7, 7]
unique_set = set(my_list)   # {1, 2, 3, 4, 5, 6, 7}
print(unique_set)

if 3 in unique_set: # 3이 있는지 확인
    print("3 is in the set!")


"""
5. deque(Double-ended queue) ****************************************

* Queue의 상위 호환으로, 양쪽 끝에서 데이터를 추가하거나 빼는 속도가 매우 빠른 자료구조.
* collections 라이브러리에 있음.
* 데크는 list와 사용법은 비슷하지만, 맨 앞, 맨 뒤에서의 추가/삭제가 O(1)으로 매우 빠름
  (list에서 pop(0)는 O(N)이라 매우 느림)

* 활용법
   - Queue(FIFO)를 구현할 때 주로 씀 (BFS 알고리즘 등)
   - Stack으로도 사용 가능 (list보다 조금 더 빠름)
   - 양쪽에서 데이터를 처리해야 하는 문제에 사용

* 핵심 연산
   - append(value) : 오른쪽에 값 추가;       O(1)
   - appendleft(value) : 왼쪽에 값 추가;    O(1)
   - pop() : 오른쪽 값 꺼내기;               O(1)
   - popleft() : 왼쪽 값 꺼내기;            O(1)
"""
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # deque([1, 2, 3, 4])
queue.appendleft(0)  # deque([0, 1, 2, 3, 4])
first_item = queue.popleft()  # first_itme = 0, queue = deque([1, 2, 3, 4])
print(first_item)  # 0


"""
6. heap **************************************************************

* 데이터를 넣으면 자동으로 정렬되는 우선순위 큐(Priority Queue)를 구현할 때 사용
* heapq 라이브러리를 통해 사용하고, 항상 가장 작은 값이 루트(0번 인덱스)에 위치하는 Min Heap
* max heap을 구현하려면, heappush 할 때 원래 값에 -를 붙여서 넣고, heappop을 할 때 다시 -를 붙여서 원래 값으로 되돌리면 됨
* 데이터를 넣고 뺄 때마다 자동으로 가장 작은 값이 위로 올라오도록 재정렬됨

* 활용법
   - 가장 작거나 큰 값을 계속해서 뽑아내야 하는 문제 (다익스트라 알고리즘, 최소 스패닝 트리 등)
   - 여러 데이터 중 상위 K개를 찾는 문제

* 핵심 연산
   - heapq.heappush(heap, value): 힙에 값 추가;    O(log N)
   - heapq.heappop(heap) : 가장 작은 값 꺼내기;      O(log N)
"""
import heapq

# min heap 구현 예시
min_heap = []
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 7)

smallest_value = heapq.heappop(min_heap)  # smallest_value = 1, min_heap = [4, 7, 5] (내부적으로는 트리)
print(f"Min : {smallest_value}")  # 1

# max heap 구현 예시
max_heap = []
heapq.heappush(min_heap, -4)   # 원래는 4지만, 음수를 붙여서 push
heapq.heappush(min_heap, -1)   # 원래는 1이지만, 음수를 붙여서 push
heapq.heappush(min_heap, -5)   # 원래는 5지만, 음수를 붙여서 push
heapq.heappush(min_heap, -7)   # 원래는 7이지만, 음수를 붙여서 push

max_value = -heapq.heappop(min_heap) # 꺼내는 값 앞에 음수를 다시 붙여서 원래대로 돌림.
print(f"Max : {max_value}")