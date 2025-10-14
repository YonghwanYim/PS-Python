"""
* Author : Yonghwan Yim
* Title : DFS (Depth First Search) - 재귀함수 사용
"""
"""
* 문제 유형
   - 경로탐색 유형 (최단거리, 시간)
   - 네트워크 유형 (연결)
   - 조합 유형 (모든 조합 만들기)
"""

"""
* Graph가 Dictionary, DFS 기본
"""
# 인접 리스트 형태로 그래프 표현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 재귀함수를 사용하니, visit 정보는 함수 내부에서 구현하면 x. 인자로 전달
def dfs_dict(node, visited, graph):
    # 현재 노드 방문처리
    visited.add(node)
    #print(node, end=' ') # 방문 순서 확인. 나중에 주석 처리

    # 현재 노드와 연결된 이웃 노드들 순회
    for neighbor in graph.get(node, []):
        # 이웃 노드가 아직 방문하지 않은 곳이라면, 재귀 호출로 더 깊게 탐색
        if neighbor not in visited:
            dfs_dict(neighbor, visited, graph) # 호출될 때, visited도 첫 줄에 의해 업데이트 됨

visited_set = set()  # 방문 기록을 위한 set 선언
dfs_dict('A', visited_set, graph)


"""
* Graph가 2D array, DFS 기본
"""
graph2 = [
    ['O', 'O', 'O', 'O', 'O', 'X'],
    ['O', 'O', 'O', 'O', 'X', 'O'],
    ['O', 'O', 'O', 'X', 'O', 'O'],
    ['O', 'O', 'X', 'O', 'O', 'O'],
    ['X', 'O', 'O', 'O', 'O', 'G'],
]
rows, cols = len(graph2), len(graph2[0])

# 상하좌우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_grid(x, y, visited, graph):
    rows, cols = len(graph), len(graph[0])

    # 현재 위치 방문 처리
    visited[x][y] = True
    #print(f"({x}, {y})", end=' ') # 방문 좌표 출력 (디버깅 이후에 주석 처리)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < rows and 0 <= ny < cols:
            if (visited[nx][ny] == False) and graph[nx][ny] != 'X':
                dfs_grid(nx, ny, visited, graph)

# 방문 기록을 위한 2D array 외부에 생성
visited_grid = [[False] * cols for _ in range(rows)]
dfs_grid(0, 0, visited_grid, graph2)