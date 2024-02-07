s=input()
cnt0=0 #0으로 바뀔 때
cnt1=1 #1로 바뀔 때

if s[0]=='0':
    cnt1+=1
else:
    cnt0+=1

for i in range(len(s)-1):
    if (s[i]!=s[i+1]):
        #다음수가 1인지 0인지
        if s[i]=='1': #다음수가 1이면 0으로 바뀌는 수 
            cnt0+=1
        else:
            cnt1+=1

print(min(cnt0,cnt1))



# pointer=int(s[0])
# res=0

# for i in range(1, len(s)):
#     if pointer == int(s[i]):
#         continue
#     else:
#         res+=1
#         pointer=int(s[i])

# print(-(-res//2))
