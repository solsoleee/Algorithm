from collections import deque

n=int(input())
board=[[0]*n for _ in range(n)]

k=int(input())
for i in range(k):
    a,b=map(int, input().split())
    board[a-1][b-1]=2

turn_dict=dict()

l=int(input())
for i in range(l):
    x,c=input().split()
    turn_dict[int(x)]=c

x,y=0,0 #뱀 초기 위치
direction=0 #현재 방향
cnt=0 #시간
#동, 남, 서, 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(c):
    global direction
    if c=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4

que=deque()
que.append((x,y))
board[x][y]=1 #뱀 처음 위치

while True:
    nx = x+dx[direction]
    ny = y+dy[direction]

    cnt+=1
    if nx>=0 and nx<n and ny>=0 and ny<n and board[nx][ny]!=1:
        if board[nx][ny]==2: #사과가 있다면
            board[nx][ny]=1
            que.append((nx, ny))
        else: #사과가 없다면
            board[nx][ny]=1
            que.append((nx, ny))

            #꼬리제거
            qx, qy = que.popleft()
            board[qx][qy]=0
            
        if cnt in turn_dict:
            turn(turn_dict[cnt])
        x,y = nx, ny
    else:
        break

print(cnt)
