sum=0
a,b,c,d=map(int,input().split())
n=a
for i in range(1,d):
    n=(n*b)+c
print(n)

