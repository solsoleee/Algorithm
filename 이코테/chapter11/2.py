s=list(map(int, input()))

res=s[0]
for i in range(1, len(s)):
    if res==0 or s[i]==0 or s[i]==1:
        res+=s[i]
    else:
        res*=s[i]

print(res)