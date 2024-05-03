T=int(input())

for t in range(1, T+1):
    arr=[]
    N, K = map(int, input().split())
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    #행 검사
    cnt=0
    res=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                cnt+=1
            else:#현재 0이라면
                if cnt==K:
                    res+=1
                    cnt=0
                cnt=0
        if cnt==K:
            res+=1
        cnt=0

    cnt=0
    #열검사
    for i in range(N):
        for j in range(N):
            if arr[j][i]==1:
                cnt+=1
            else:
                if cnt==K:
                    res+=1
                    cnt=0
                cnt=0
        if cnt==K:
            res+=1
        cnt=0
    print(f'#{t} {res}')