n=list(map(int, input()))

cnt=[0]*10

for i in n:
    if i == 9:
        cnt[6]+=1
    else:
        cnt[i]+=1

cnt[6]=-(-cnt[6]//2)

print(max(cnt))