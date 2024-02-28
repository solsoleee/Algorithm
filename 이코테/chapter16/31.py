n,m=map(int, input().split())

arr=list(map(int, input().split()))

d=[]
for i in range(0,len(arr),m):
    d.append(arr[i:i+m])

for j in range(1,m):
    for i in range(n):
        #왼쪽위에서 오는 경우 -1
        if i==0: #현재 위치가 0이면 위로 갈 곳이 없음 0이라는건 행에서 0을 말함 첫번째줄
            left_up=0
        else:
            left_up=d[i-1][j-1]
        #왼쪽 아래서 오는 경우
        #현재 위치가 마지막이면
        if i==n-1:
            left_down=0
        else:
            left_down=d[i+1][j-1]
        #왼쪽에서 오는 경우    
        left=d[i][j-1]
        d[i][j]=d[i][j]+max(left_up, left_down, left)

result=0
for i in range(n):
    result=max(result, d[i][m-1])

print(result)




for i in range(2, n+1):
    for j in range(2, m+1):
        d[i][j]=d[i][j]+max(d[i][j-1], d[i-1][j-1], d[i+1][j+1])

print(d)