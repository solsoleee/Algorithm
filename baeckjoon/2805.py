n,m=map(int, input().split())
tree=list(map(int, input().split()))
tree.sort()


start=0
end=max(tree)
cnt=0

while start <= end:
    result=0
    mid=(start+end)//2
    for i in tree:
        if i > mid:
            result+=i-mid
        else:
            result+=0
    if result == m:
        cnt=mid
        break
    elif result > m:
        start=mid+1
        cnt=mid
    else:
        end=mid-1
print(cnt)