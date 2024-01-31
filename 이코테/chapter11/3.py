s=list(map(int, input()))

cnt0=0 #0으로 바꿈
cnt1=0 #1로 바꿈

if s[0]==1:
    cnt0+=1

else:
    cnt1+=1


for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1]==1:
            cnt0+=1
        else:
            cnt1+=1
            
print(min(cnt0,cnt1))
    