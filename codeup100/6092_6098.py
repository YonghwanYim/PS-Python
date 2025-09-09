"""
* Author : Yonghwan Yim
* Final Update : 25.09.09
* Title : CodeUp Python 기초 100제
* Sub : [기초-리스트] 6092 ~ 6098
"""

"""
* 6092 : [기초-리스트] 이상한 출석 번호 부르기1
"""

n = int(input())
number_list = list(map(int, input().split()))
students = list(0 for _ in range(23))  # 크기 23의 리스트 생성 (리스트 컴프리헨션)

for element in number_list: # 해당되는 번호를 학생 리스트에 count.
    students[element - 1] += 1

for student in students: # 학생 별 count 출력
    print(student, end=' ')

"""
* 6093 : [기초-리스트] 이상한 출석 번호 부르기2
"""

n = int(input())
number_list = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    print(number_list[i], end=' ')
    
# 쉬운 구현 버전 (여기선 의도에 맞지 않으니 제외)
#number_list.reverse() # 원본 list 뒤집음, 반환값 None
#print(number_list)


"""
* 6094 : [기초-리스트] 이상한 출석 번호 부르기3
"""

n = int(input())
n_list = list(map(int, input().split()))
min_num = 0
for i in range(0, n):
    if i == 0:
        min_num = n_list[i]
    else:
        if n_list[i] < min_num:
            min_num = n_list[i]
print(min_num)

"""
* 6095 : [기초-리스트] 바둑판에 흰 돌 놓기
"""

go_board = [[0 for j in range(19)] for i in range(19)]   # 19 * 19 바둑판 생성 및 0으로 초기화 (List Comprehension)
n = int(input())

for i in range(n): # 입력받는 횟수
    x, y = map(int, input().split())
    go_board[x-1][y-1] = 1

for i in range(19):
    print(*go_board[i])  # 리스트 앞에 *를 붙이면 각 요소가 개별인자로 print에 전달; 이렇게 하면 2중 for문 안해도 됨.


"""
* 6096 : [기초-리스트] 바둑알 십자 뒤집기
"""

go_board =  [[0 for j in range(19)] for i in range(19)]  # 크기는 19* 19 고정

for i in range(19): # 19 * 19 사이즈로 현 상황 입력
    go_board[i] = list(map(int, input().split()))

n = int(input())

# 바둑알 십자 뒤집기
for count in range(n):
    x, y = map(int, input().split())
    for i in range(19):
        if i != x-1:
            if go_board[i][y-1] == 0: # 0이면 1로
                go_board[i][y-1] = 1
            else:                   # 1이면 0으로
                go_board[i][y-1] = 0
    for j in range(19):
        if j != y-1:
            if go_board[x-1][j] == 0: # 0이면 1로
                go_board[x-1][j] = 1
            else:                   # 1이면 0으로
                go_board[x-1][j] = 0

# 결과 출력
for i in range(19):
    print(*go_board[i])


"""
* 6097 : [기초-리스트] 설탕과자 뽑기
"""

h, w = map(int, input().split())
grid = [[0 for j in range(w)] for i in range(h)]  # h, w에 맞는 grid 생성

n = int(input()) # 막대의 수
for count in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:  # 가로막대
        for j in range(y-1, y-1+l):
            grid[x-1][j] = 1
    else:      # 세로막대
        for i in range(x-1, x-1+l):
            grid[i][y-1] = 1

# 결과 출력
for i in range(h):
    for j in range(w):
        print(grid[i][j], end=' ')
    print('')


"""
* 6098 : [기초-리스트] 성실한 개미
"""

grid = [[0 for j in range(10)] for i in range(10)]  # 0으로 채운 10*10 그리드 생성
for i in range(10):                                 # 그리드 입력 받기
    grid[i] = list(map(int, input().split()))

# 개미 시작위치 지정
x, y = 1, 1

# 개미 움직임 시뮬레이션
while True:
    if grid[x][y] == 2:    # 현재 위치가 2이면 먹이 먹고 종료
        grid[x][y] = 9
        break

    grid[x][y] = 9         # 현재 위치 9로 지정 (먹이가 없는 경우)

    if grid[x][y+1] != 1:  # 오른쪽이 벽이 아니면 오른쪽으로 한칸 이동
        y += 1
        continue
    elif grid[x+1][y] != 1: # 아래가 벽이 아니면 아래로 한칸 이동
        x += 1
        continue
    else:                  # 오른쪽, 아래 모두 막히면 종료
        break

# 결과 출력
for row in grid:
    print(*row)