T=int(input())

dx=[0,1,0,-1]
dy=[1,0,-1,0]

for t in range(1, T+1):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    direction=0
    nx,ny = 0,0
    arr[nx][ny]=1
    for i in range(2, N*N + 1):
        nx+=dx[direction]
        ny+=dy[direction]

        if nx>=0 and nx<N and ny>=0 and ny<N and arr[nx][ny]==0:
            pass
        else:
            nx-=dx[direction]
            ny-=dy[direction]
            direction=(direction+1)%4
            nx+=dx[direction]
            ny+=dy[direction]
        arr[nx][ny]=i

    print(f'#{t}')
    for a in arr:
        print(*a)
    