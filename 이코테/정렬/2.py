n=int(input())
n_list=list(map(int, input().split()))

m=int(input())
m_list=list(map(int, input().split()))

start=0
end=n

n_list.sort()
m_list.sort()

def binary(start, end, arr,k):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==k:
            return True
        elif arr[mid]>k:
            end=mid-1
        else:
            start=mid+1
    return False



for i in m_list:
    if binary(0, n, n_list, i):
        print("yes")
    else:
        print("no")