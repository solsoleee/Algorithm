n,m=map(int, input().split())

d=[0]*10001
coin=[]
for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(2, n+1):
        if m%i==0:
            d[j]=d[m//i]
            
