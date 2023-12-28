N=int(input())
cus=[]
for i in range(N):
    a,b=input().split()
    a=int(a)
    cus.append((a,b))

cus.sort(key=lambda x:(x[0]))

for i in cus:
    print(i[0], i[1])



