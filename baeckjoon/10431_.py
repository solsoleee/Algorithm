t=int(input())
for i in range(t):
    
    arr=list(map(int, input().split()))
    
    #첫번째랑 마지막 끝까지 비교를 해서 값을 교체한다.
    cnt=0
    for i in range(1, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                cnt+=1
    print(arr[0], cnt)