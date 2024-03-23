from collections import deque

n = int(input())
graph = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
turn_dic = dict()
for _ in range(l):
    x, c = input().split()
    turn_dic[int(x)] = c

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(d):
    global direction
    if d == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

cnt = 0
direction = 0
x, y = 0, 0
que = deque([[x, y]]) # 뱀의 위치 초기화 수정
graph[x][y] = 1  # 뱀의 초기 위치를 1로 설정

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    cnt += 1  # 시간(이동 횟수) 증가
    
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1:
        # 사과가 있을 때
        if graph[nx][ny] == 2:
            graph[nx][ny] = 1
            que.append([nx, ny])
        # 사과가 없을 때
        else:
            graph[nx][ny] = 1
            que.append([nx, ny])
            tx, ty = que.popleft() #꼬리 부분 제거 
            graph[tx][ty] = 0
        
        x, y = nx, ny  # 다음 위치로 머리 이동
        
        if cnt in turn_dic:  # 회전 체크
            turn(turn_dic[cnt])
    else:
        break  # 벽이나 자기 자신의 몸과 부딪혔을 때

print(cnt)
