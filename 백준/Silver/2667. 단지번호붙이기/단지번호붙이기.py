n=int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int, input())))
    
result=0
cnt=0
def dfs(x,y):
    
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if arr[x][y]==1:
        global cnt
        cnt+=1
        arr[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        return True
    return False
cnt=0
cnt_list=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j)== True:
            result+=1
            cnt_list.append(cnt)
            cnt=0
cnt_list.sort()
print(result)
for i in cnt_list:
    print(i)