n=int(input())
n_list=list(map(int, input().split()))

m=int(input())
m_list=list(map(int, input().split()))

n_list.sort()

def binary(arr, start, end, target):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return True
        if arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return False


for i in m_list:
    if binary(n_list, 0, n-1, i):
        print(1, end=' ')
    else:
        print(0, end=' ')