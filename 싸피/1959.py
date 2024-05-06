T=int(input())

for t in range(1, T+1):
    N, M =map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    res=0
    cnt=0
    if N < M:
        for i in range(abs(M-N)+1):
            for j in range(N):
                cnt+=m_list[i+j]*n_list[j]
            res=max(res, cnt)
            cnt=0
    else:
        for i in range(abs(M-N)+1):
            for j in range(M):
                cnt+=m_list[j]*n_list[i+j]
            res=max(res, cnt)
            cnt=0
    print(f'#{t} {res}')
    
    
    
    
    