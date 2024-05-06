T=int(input())

for t in range(1, T+1):
    N=int(input())
    arr=[]
    for i in range(N):
        c,k=input().split()
        arr.append((c*int(k)))
    res=''
    res+=''.join(map(str, arr))
    print(f'#{t}')
    for i in range(0, len(res), 10):
        print(res[i:i+10])    