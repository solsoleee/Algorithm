S=input()

cnt=0
first=S[0]
pre=S[0]

for i in range(1, len(S)):
    if S[i]!=pre and S[i]!=first:
        cnt+=1    
    pre=S[i]

print(cnt)