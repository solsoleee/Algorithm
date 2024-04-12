from collections import deque


n=int(input())
k=int(input())
board=[[0]*n for _ in range(n)]
for _ in range(k):
    a,b=map(int, input().split())
    board[a-1][b-1]=1

l=int(input())
turn_info=dict()
for i in range(l):
    a,b=input().split()
    turn_info[int(a)]=b



def turn(d):
    global direction
    if d=='L':
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4

timer=0


que=deque()
que.append([0,0])
x,y=0,0
board[x][y]=2 #뱀의 위치
direction=0
dx=[0,1,0,-1]
dy=[1,0,-1,0] #동님서북
while True:
    timer+=1
    nx=x+dx[direction]
    ny=y+dy[direction]
    if nx<0 or nx>=n or ny<0 or ny>=n or board[nx][ny]==2:
        break

    if board[nx][ny]==1: #사과가 있다면
        que.append([nx,ny])
        board[nx][ny]=2
    else: #사과가 없다면
        board[nx][ny]=2
        que.append([nx,ny])
        px, py = que.popleft()
        board[px][py]=0 #꼬리가 위치한 칸을 비워줌
    
    x,y=nx,ny #이동
        
    if timer in turn_info:
        turn(turn_info[timer])

print(timer)