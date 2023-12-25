num=[]
N=int(input())
for i in range(N):
    xy=list(map(int, input().split()))
    num.append(xy)

num.sort()

for i in range(N):
    print(num[i][0], num[i][1])