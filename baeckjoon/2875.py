n,m,k=map(int, input().split())
cnt=0
m=m-1
print(m)
while n>0 and m>0:
    #방법1 n을 뺀다
    #방법2 m을 뺀다
    n-=2
    m=m-1
    cnt+=1
    print(n,m,cnt)

print(cnt)