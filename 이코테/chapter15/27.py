from bisect import bisect_left, bisect_right
n,x=map(int, input().split())

arr=list(map(int, input().split()))

answer=bisect_right(arr, x)-bisect_left(arr, x)

if answer<=0:
    print(-1)
else:
    print(answer)

