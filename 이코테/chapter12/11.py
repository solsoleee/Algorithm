n=int(input())
graph=[[0]*n for i in range(n)]
k=int(input())

for i in range(k):
    a,b=map(int, input().split())
    graph[a-1][b-1]=1

command=[]
l=int(input())
for i in range(l):
    x,c=input().split()
    command.append((int(x),c))

def turn(direction, c):
    if c=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction

#동 남 서 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

#뱀이 위치한 곳
def simulate():
    x,y=0,0 #뱀의 머리 현재 위치
    graph[x][y]==2 #뱀이 존재하는 것을 2로 표현
    direction=0 #처음에는 동쪽을 보고 있음
    time=0 #시작한 후 시간
    index=0 #다음에 회전할 정보
    q=[(x,y)] #뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽)
    while q:
        nx=x+dx[direction]
        ny=y+dy[direction]
        #뱀의 몸통이 없는 위치라면
        if nx>=0 and nx>n and ny>=0 and ny>n and graph[nx][ny]!=2:
            if graph[nx][ny]==1:
                graph[nx][ny]=2
                q.append((nx, ny))
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                q.append((nx,ny))
                px, py =q.pop(0)
                graph[px][py]=0 
        #벽이나 뱀의 몸통과 부딪혔다면
        else:
            time+=1
            break  
        x,y=nx, ny #다음 위치로 머리를 이동
        time+=1
        if index < l and time==command[index][0]:
            direction=turn(direction, command[index][1])
            index+=1
    return time
            
            
print(simulate())

# 모르겠는 이유.
# 방향 바꾸는 방법을 모르겠음, D가 나와서 방향을 어떻게 해야할지
# 뱀의 길이가 바뀌는거.. 이거 구현
# 