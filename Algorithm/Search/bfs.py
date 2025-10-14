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

        #for next_node in graph[current_node]: # current_node를 key로, value를 가져와 반복 (F->G가 있을 때, G가 Key로 없으면 에러 발생)
        for next_node in graph.get(current_node, []): # 이렇게 선언하면 key가 없을 때 빈 리스트를 반환해서 더 안전함
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

        for next_node in graph.get(current_node, []):
            if next_node not in visited:      # 확인할 땐 빠른 set을 사용
                visited.add(next_node)
                path_list.append(next_node)  # 순서 기록
                queue.append(next_node)
    return path_list

print("BFS 탐색 결과:", bfs_2('A', graph))
# 출력: BFS 탐색 결과: ['A', 'B', 'C', 'D', 'E', 'F']


"""
* Graph가 2D Array 일 때, BFS 기본공식
"""
graph2 = [
    ['O', 'O', 'O', 'O', 'O', 'X'],
    ['O', 'O', 'O', 'O', 'X', 'O'],
    ['O', 'O', 'O', 'X', 'O', 'O'],
    ['O', 'O', 'X', 'O', 'O', 'O'],
    ['X', 'O', 'O', 'O', 'O', 'G'],
]

# 2차원 배영 인덱싱은 [row][col]이므로, 첫 번째 index가 세로, 두 번째 인덱스가 가로. 수학에서의 직교좌표랑 반대로 생각하자
def bfs_2D_array(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]   # 상하좌우 방향으로 이동 가능
    dy = [0, 0, -1, 1]

    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # len(graph) : 행의 개수, len(graph[0]) : 열의 개수 (직사각형 2D array라 성립)
            if 0 <= next_x < len(graph) and 0 <= next_y < len(graph[0]):
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
    # 모든 곳을 탐색했지만 도착지를 찾지 못하면 -1 리턴
    return -1

print(bfs_2D_array(0, 0, graph2)) # 조건을 넣어서 루프가 끝나기 전에 중간에 종료되도록 할 수 있음.


# visited을 쓰지 않고, distance로 통합해서 쓰는 버전. 방문하지 않은 곳은 -1로 초기화
def bfs_2D_array_with_distance(start_x, start_y, graph):
    rows, cols = len(graph), len(graph[0])
    # 방문 여부 (-1), 거리를 저장하는 2차원 배열 형성
    distance = [[-1] * cols for _ in range(rows)]   # graph 사이즈에 맞게 -1로 전체 초기화

    # 이동 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(start_x, start_y)])
    distance[start_x][start_y] = 0    # 시작 지점의 거리는 0

    while queue:
        curr_x, curr_y = queue.popleft()

        if graph[curr_x][curr_y] == 'G':
            return distance[curr_x][curr_y]

        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]

            if 0 <= next_x < rows and 0 <= next_y < cols:
                # 아직 방문 안했고, 벽(X)이 아니라면 (O, G의 경우에는 진행)
                if distance[next_x][next_y] == -1 and graph[next_x][next_y] != 'X':
                    distance[next_x][next_y] = distance[curr_x][curr_y] + 1   # 현재 거리에서 1 더함.
                    queue.append((next_x, next_y))
    # 모든 곳을 탐색했지만 도착지를 찾지 못하면 -1 리턴
    return -1

print(bfs_2D_array_with_distance(0, 0, graph2))