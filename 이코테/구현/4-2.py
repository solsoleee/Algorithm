
n=int(input())
cnt=0

for k in range(0,n+1):
    for j in range(0, 60):
        for i in range(0,60): #초
            if '3' in str(k)+str(i)+str(j):
                cnt+=1

print(cnt)