s=input().upper()
word=list(set(s))

cnt=[]
for i in word:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) >=2:
    print("?")

else:
    print(word[cnt.index(max(cnt))])