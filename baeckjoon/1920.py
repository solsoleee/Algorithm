n=int(input())
n_list=list(map(int, input().split()))

m=int(input())
m_list=list(map(int, input().split()))

n_list.sort()

def binary_search(target, start, end, arr):
    while start <= end:
        mid=(start+end)//2
        if target==arr[mid]:
            return True
        elif target > arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return False

for target in m_list:
    if binary_search(target, 0, n-1, n_list):
        print(1)
    else:
        print(0)
