"""
* Author : Yonghwan Yim
* Title : BFS (Breadth First Search)
"""

"""
* 자주 등장하는 BFS 문제 유형은
   - 기본 순회 문제 : 현재 노드를 기준으로 이동할 수 있는 모든 노드를 탐색
   - 최단 경로 문제 : 특정 두 노드 사이의 최단 경로를 탐색
   - 연결 요소 문제 : 현재 노드를 기준으로 연결된 모든 노드를 탐색
   - 플러드 필 문제 : 그래프의 영역을 특정 색상으로 채우는 문제 (땅따먹기)
"""

"""
* BFS 기본 구현
"""
from collections import deque

# 인접 리스트 형태로 그래프 표현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

"""
* Graph가 Dictionary일 때, BFS 기본 공식 (탐색 경로 자체는 의미 없을 때. set으로 빠르게 계산)
"""
def bfs(start_node, graph):
    queue = deque([start_node]) # 시작 노드를 queue에 넣음
    visited = set([start_node]) # 변수가 아닌 리스트 자체를 전달 (set을 쓰면 방문 순서는 기억 x. 하지만 빠름)

    while queue:  # python에서는 비어있지 않은 모든 컨테이너는 True로 취급하는 것 이용.
        current_node = queue.popleft()

        for next_node in graph[current_node]: # current_node를 key로, value를 가져와 반복
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return visited

# BFS 실행
print("BFS 탐색 결과:", bfs('A', graph))  # set이라 순서는 의미 x


"""
* Graph가 Dictionary일 때, BFS 탐색 경로 자체도 기억해야 할 때는 list 하나 추가.
"""
def bfs_2(start_node, graph):
    queue = deque([start_node]) # 시작 노드를 queue에 넣음
    visited = set([start_node]) # 변수가 아닌 리스트 자체를 전달 (set을 쓰면 방문 순서는 기억 x. 하지만 빠름)
    path_list = [start_node]    # 실제 탐색 순서 기록용

    while queue:  # python에서는 비어있지 않은 모든 컨테이너는 True로 취급하는 것 이용.
        current_node = queue.popleft()

        for next_node in graph[current_node]: # current_node를 key로, value를 가져와 반복
            if next_node not in visited:      # 확인할 땐 빠른 set을 사용
                visited.add(next_node)
                path_list.append(next_node)  # 순서 기록
                queue.append(next_node)
    return path_list

print("BFS 탐색 결과:", bfs_2('A', graph))
# 출력: BFS 탐색 결과: ['A', 'B', 'C', 'D', 'E', 'F']






