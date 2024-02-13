n=int(input())

arr=list(map(int, input().split()))

def binary(arr, start, end):
    mid=(start+end)//2
    if start > end:
        return False
    if mid==arr[mid]:
        return mid
    if arr[mid]>mid:
        return binary(arr, start, mid-1)
    if arr[mid]<mid:
        return binary(arr, mid+1, end)

answer=binary(arr, 0, n)
if answer:
    print(answer)
else:
    print(-1)
