N=int(input())
cus=[]
for i in range(N):
    a=list(input().split())
    cus.append(a)

cus.sort(key=lambda x:(x[0]))

for i in cus:
    print(i[0], i[1])



