T=int(input())

for t in range(1, T+1):
    arr=[]
    N=int(input())
    for _ in range(N):
        arr.append(list(map(int, input())))
    
    print(arr)
    
    # for i in range(N):
    #     for j in range