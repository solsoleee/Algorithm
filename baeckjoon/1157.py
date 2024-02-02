cnt=[0]*100000

s=input()

for i in s:
    i=i.lower()
    cnt[ord(i)]+=1
    
print(chr(cnt.index(max(cnt))).upper())
