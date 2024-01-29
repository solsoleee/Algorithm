n=int(input())

n_list=list(map(int, input().split()))

n_list.sort()

d=[0]*(n+1)

d[1]=n_list[0]
for i in range(2, n+1):
    d[i]=d[i-1]+n_list[i-1]

result=0
for j in range(1, n+1):
    result+=d[j]
    
print(result)