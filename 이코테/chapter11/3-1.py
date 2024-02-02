s=input()
cnt0=0
cnt1=0
print(s)
if s[0]=='0':
    cnt1+=1
else:
    cnt0+=1
    
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=='0':
            cnt1+=1
        else:
            cnt0+=1

print(min(cnt0,cnt1))