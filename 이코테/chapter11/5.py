n,m=map(int, input().split())

n_list=list(map(int, input().split()))

cnt=0

for i in range(0, n):
    for j in range(1, n):
        if n_list[i]==n_list[j] or j<=i:
            continue
        else:
            cnt+=1

print(cnt)