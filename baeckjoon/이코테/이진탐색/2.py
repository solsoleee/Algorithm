import sys




def binary_search(array, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end=mid-1
        else:
            start=mid+1
    return 'no'



n=int(input())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
m=int(input())
arr_list=list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

for i in arr_list:
    print(binary_search(arr,i,0,n-1), end=' ')


