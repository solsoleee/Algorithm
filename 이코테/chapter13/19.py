n=int(input())
#연산을 수행하고자 하는 수 리스트
arr=list(map(int, input().split()))
#더하기 빼기 곱하기 나누기 연산의 개수
a,b,c,d=map(int, input().split())

min_value=1e10
max_value=-1e10

#깊이 우선 탐색 메서드
def dfs(i, now):
    global a,b,c,d, min_value, max_value
    #모든 연산자를 다 사용한 경우, 최솟값과 최대값 업데이트
    if i==n:
        max_value=max(max_value,now)
        min_value=min(min_value,now)
        
    else:
        if a>0: 
            a-=1
            dfs(i+1, now+arr[i])
            a+=1 #가능한 모든 경로를 탐색하고 다시 원상복구
        if b>0:
            b-=1
            dfs(i+1, now-arr[i])
            b+=1
        if  c>0:
            c-=1
            dfs(i+1, now*arr[i])
            c+=1
        if d>0:
            d-=1
            dfs(i+1, int(now / arr[i]))
            d+=1

dfs(1, arr[0])
print(max_value)
print(min_value)

