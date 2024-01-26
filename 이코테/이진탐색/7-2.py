def binary_search(array, target, start, end):
    if start > end:
        return None
    mid=(start+end)//2
    
    if array[mid]==target:
        return mid
    
    elif array[mid] > target:
        binary_search(array, target, start, mid-1)
    else:
        binary_search(array, target, mid+1, end)
    
    n,target=list(map(int,input().split()))
    array=list(map(int, input().split()))
    
    result=binary_search(array, target, 0, n-1)
    if result==None:
        print("X")
    else:
        print(result+1)
        
