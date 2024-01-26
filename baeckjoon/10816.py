n=int(input())

n_list=list(map(int, input().split()))

m=int(input())

m_list=list(map(int, input().split()))

n_list.sort()

def binary_search(start, end, arr, target):
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
    if binary_search(0, n-1, n_list, target):
        print(n_list.count(target), end=' ')
    else:
        print(0, end=' ')

