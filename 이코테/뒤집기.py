S=input()

count0=0
count1=0

if S[0]=='0':
    count1+=1
else:
    count0+=1
    
for i in range(1, len(S)-1):
    if S[i] == S[i+1]:
        pass
    else:
        if S[i]=='0':
            count1+=1
        else:
            count0+=1
print(min(count0,count1))