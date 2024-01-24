def binary_search(arr, target, start, end):
    while start <=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid] > target:
            end=mid-1
        else: start=mid+1
    return None

n,target=list(map(int,input().split()))
array=list(map(int, input().split()))

result=binary_search(array, target, 0, n-1)
if result==None:
    print("X")
else:
    print(result+1)