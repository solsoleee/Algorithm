
def dfs(x,y,arr):
    if x >= b or x-1<0 or y>=a or y-1<0:
        return False
    if arr[x][y] == 1:
        print("whq")
        arr[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

arr=[]
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    
    arr=[[0]*(a+1) for i in range(b+1)]
    result=0
    for j in range(c):
        x,y=map(int,input().split())
        arr[y][x]=1
    print(arr)
    if dfs(0,0,arr):
        print("ddd")
        result+=1
print(result)
        
        