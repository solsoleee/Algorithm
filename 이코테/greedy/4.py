n,m=map(int, input().split())

x, y, direction=map(int, input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))

visited=[[0]*m for _ in range(n)]


# 북, 동, 남, 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

cnt=0

#왼쪽으로 회전
def turn_left():
    global direction
    direction=(direction-1)%4 #회전
    

#시뮬레이션 시작
count=1
turn_time=0 #회전 수

while True:
    #왼쪽으로 회전
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction] 
    if visited[nx][ny]==0 and arr[nx][ny]==0: #아직 가보지 않은 칸이 존재한다면 #육지라면
                x,y=nx,ny
                visited[nx][ny]=1 #방문함
                cnt+=1
                turn_time=0 #회전 수
                continue
    else: #가보지 않은 칸이 없거나 바다라면
        turn_time+=1
        if turn_left==4:
            nx=x-dx[direction]
            ny=y-dy[direction]
            if arr[nx][ny]==0:
                x,y=nx,ny
            else:
                break
            turn_time=0
        
        