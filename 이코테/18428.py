n=int(input())

arr=[]
temp = [[0]*n for _ in range(n)]
for _ in range(n):
    arr.append(list(input().split()))


def check(temp):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for i in range(n):
        for j in range(n):
            if temp[i][j]=='T':
                for direction in range(4):
                    nx, ny = i, j
                    while True:
                        nx += dx[direction]
                        ny += dy[direction]
                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            break
                        if temp[nx][ny]=='S':
                            return False
                        if temp[nx][ny]=='O':
                            break #다른 방향으로 변경
    return True


def dfs(count):
    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j]=arr[i][j]
        
        if check(temp):
            return True
        return False
        
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='X':
                arr[i][j]='O'
                count+=1
                if dfs(count):
                    return True
                arr[i][j]='X'
                count-=1

if dfs(0):
    print("YES")
else:
    print("NO")