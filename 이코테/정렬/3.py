n,m=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
start=arr[0]
end=arr[-1]
result=0


def binary(start, end, arr):
    global result
    while start<=end:
        target=0
        mid=(start+end)//2
        for i in arr:
            if mid<i:
                target+=(i-mid)
        if target==m:
            return mid
        elif target>=m:
            start=mid+1
            result=mid
        else:
            end=mid-1
    return result

print(binary(start, end, arr))
