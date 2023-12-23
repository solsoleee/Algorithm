N,M=map(int,input().split())
list=[i for i in range(1,N+1)]
for j in range(M):
    a,b,c=map(int,input().split())
    list[j:b-c+1]=list[c:b]
    list[c:b+1]=list[a:c]
print(list)