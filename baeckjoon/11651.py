N=int(input())
num=[]
for i in range(N):
    xy=list(map(int,input().split()))
    num.append(xy)
    
num.sort(key=lambda x:(x[1], x[0]))

for i in range(N):
    print(num[i][0], num[i][1])