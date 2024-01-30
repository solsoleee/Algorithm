n=int(input())

next=list(map(int, input().split()))

price=list(map(int, input().split()))



result=0
for i in range(n):
    result=price[0]*sum(next)
    

for i in range(n):
    result+=next[i]*price[i]
    result-=next[i]
    print(next[i])
    if result>=sum(next):
        break
print(result)
