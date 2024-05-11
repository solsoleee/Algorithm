from collections import deque
n,k = map(int, input().split())

virus=[]
cnt=0
for _ in range(n):
    virus.append(list(map(int, input().split())))
    
#que에 넣는데 번호도 같이 넣기
s,x,y = map(int, input().split())
dx=[0,1,0,-1]
dy=[1,0,-1,0]

que=deque()

for i in range(n):
    for j in range(n):
        if virus[i][j]!=0:
            que.append((i,j,virus[i][j]))

while que:
    x,y,v=que.popleft()
    # if cnt==s:
    #     break
    for i in range(4):
        
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and virus[nx][ny]==0:
            virus[nx][ny]=v
            que.append((nx,ny,virus[nx][ny]))
    cnt+=1
    print(cnt)
    print(virus)
print(virus[x-1][y-1])
