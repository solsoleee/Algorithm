num={}
N=int(input())

for i in range(N):
    card=int(input())
    if card in num:
        num[card]+=1
    else:
        num[card]=1



result=sorted(num.items(), key=lambda x: (-x[1],x[0]))
print(result)

print(result[0][0])