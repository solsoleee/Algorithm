alp='abcdefghizklmnopqrstuvwxyz'
s=input()
cnt=0
for i in alp:
    if i in s:
        cnt+=1
        print(cnt)