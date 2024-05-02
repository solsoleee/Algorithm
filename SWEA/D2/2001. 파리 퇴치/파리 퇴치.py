T=int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr=[]
    for _ in range(N):
        arr.append(list(map(int, input().split())))
        
    ans=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            res=0
            for k in range(M):
                for v in range(M):
                    res+=arr[i+k][j+v]
                    
            ans=max(res, ans)

    print(f'#{test_case} {ans}')