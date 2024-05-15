n=int(input())

arr=list(map(int, input().split()))

a,b,c,d= map(int, input().split())

max_value = -1e9 #최댓값
min_value = 1e9

#dfs 메서드 정의
def dfs(i, res):
    global a,b,c,d, max_value,min_value
    if i==n:
        max_value=max(max_value, res)
        min_value=min(min_value, res)
    else:
        if a > 0:
            a-=1
            dfs(i+1, res+arr[i])
            a+=1
        if b > 0:
            b-=1
            dfs(i+1, res-arr[i])
            b+=1
        if c > 0:
            c-=1
            dfs(i+1, res*arr[i])
            c+=1
        if d > 0:
            d-=1
            dfs(i+1, int(res/arr[i]))
            d+=1
            
dfs(1, arr[0])

print(max_value)
print(min_value)