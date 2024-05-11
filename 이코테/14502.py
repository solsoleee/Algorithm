from collections import deque
n,m = map(int, input().split())
arr=[]
temp=[[0]*m for _ in range(n)] #바이러스 복사본
for _ in range(n):
    arr.append(list(map(int, input().split())))

ans=0 #최종 정답

#virus를 퍼뜨림
def virus(x,y):
    que=deque()
    que.append((x,y))
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and temp[nx][ny]==0:
                temp[nx][ny]=2
                que.append((nx, ny))

def safe_count():
    res=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                res+=1
    return res

def dfs(count):
    global ans
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=arr[i][j] #복사

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j) #2인거 바이러스 호출
        
        ans=max(safe_count(), ans) #계산
        return
    
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    arr[i][j]=1
                    count+=1
                    dfs(count)
                    arr[i][j]=0
                    count-=1
dfs(0)
print(ans)
