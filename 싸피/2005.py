T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0]=1
    for i in range(1, N):
        for j in range(N):
            if j==0:
                arr[i][j]=1
            else:
                arr[i][j]=arr[i-1][j-1]+arr[i-1][j]

    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            if arr[i][j]!=0:
                print(arr[i][j], end=' ')
        print()