k=int(input())
cnt=0
for i in range(k):
    if 2**i >= k:
        cnt=i
        break
    
result=0
c=2**cnt
for i in range(k):
    if k%c==0:
        break
    else:
        c//=2
        result+=1

print(2**cnt, result)