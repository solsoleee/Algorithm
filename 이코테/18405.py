from collections import deque
n,k = map(int, input().split())

data=[]
for _ in range(n):
    data.append(list(map(int, input().split())))
    
#que에 넣는데 번호도 같이 넣기
s,x1,y1 = map(int, input().split())
dx=[0,1,0,-1]
dy=[1,0,-1,0]

virus=[]
for i in range(n):
    for j in range(n):
        if data[i][j]!=0:
            virus.append((data[i][j], i,j,0))
virus.sort() #우선순위대로 퍼지기 떄문
que=deque(virus)
while que:
    v,x,y,m=que.popleft()
    if m==s:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and data[nx][ny]==0:
            data[nx][ny]=v
            que.append((v, nx,ny,m+1))

print(data[x1-1][y1-1])
