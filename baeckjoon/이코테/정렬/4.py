n,k=map(int, input().split())

a=list(map(int, input().split()))
b=list(map(int, input().split()))

for i in range(k):
    index1=a.index(min(a))
    index2=b.index(max(b))
    if min(a) < max(b):
        a[index1],b[index2] = max(b), min(a)

print(sum(a))
