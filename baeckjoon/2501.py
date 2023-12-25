a,b = map(int, input().split())
factor=[]

for i in range(1, a+1):
    if a % i == 0:
        factor.append(i)

if len(factor)>b-1:
    print(factor[b-1])
else:
    print(0)
    
