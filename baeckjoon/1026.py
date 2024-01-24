n=int(input())

a=list(map(int, input().split()))
b=list(map(int, input().split()))

cnt=[]
a.sort()

b_list=sorted(b, reverse=True)

for i in b_list:
    cnt.append(b.index(i))

result=0
for i in range(len(a)):
    result+=a[i]*b[cnt[i]]

print(result)