"""
* Author : Yonghwan Yim
* Final update : 25.10.15
* 1260. DFS와 BFS
* https://www.acmicpc.net/problem/1260
"""
"""
* DFS, BFS 탐색 결과 출력하는 프로그램 작성 (탐색 로그 출력)
* Dictionary 형태로 graph 저장 후 문제 풀이.
* 우선순위 : 방문 가능 정점이 여러개면 번호가 작은 것 먼저 방문   -> graph 정렬 후 시작으로 해결
* 더이상 방문할 수 있는 점 없으면 종료
* 정점 번호는 1번부터 N번까지
"""
import sys
from collections import defaultdict
from collections import deque

def dfs(node, visited, graph, path):  # O(N+M) # 모든
    visited.add(node)
    path.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited, graph, path)
    return -1

def bfs(start_node, graph):  # O(N+M)
    queue = deque([start_node])
    visited = set([start_node])
    path = [start_node]

    while queue:
        curr_node = queue.popleft()
        for neighbor in graph.get(curr_node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                path.append(neighbor)
    return path

# 입력 처리
read = sys.stdin.readline   # 가독성을 위해 read로 새롭게 정의

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, read().split())

# M번 입력받아 그래프 저장 (dictionary)
graph = defaultdict(list) # 존재하지 않는 키 호출하면, 빈 list를 자동으로 생성해줌. 따라서 append만 쓰면 됨
for i in range(M):
    N1, N2 = map(int, read().split())
    graph[N1].append(N2)
    graph[N2].append(N1)

# DFS/BFS 시작 전, 각 인접리스트 정렬 (내장함수 sort() 사용)
for i in range(N+1):
    graph[i].sort()      # Timesort, O(N log N)으로 빠름

# visited 정의
visited_dfs = set()    # O(1)로 비교할 수 있도록 set으로 정의
path_dfs = []          # 실제 탐색 경로 저장

# 탐색 실행
dfs(V, visited_dfs, graph, path_dfs)
path_bfs = bfs(V, graph)

# DFS, BFS 경로 출력
print(*path_dfs) # python의 unpacking 사용
print(*path_bfs)

"""
for value in path_dfs:
    print(value, end=' ')
print()

for value in path_bfs:
    print(value, end=' ')
"""