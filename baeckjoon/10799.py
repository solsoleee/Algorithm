a=input()
b=[]
cnt=0
pre=0
for i in a:
    if i=="(":
        b.append(i)
    elif i==")" and pre=="(":
        b.pop()
        cnt+=len(b)
    else:
        b.pop()
        cnt+=1
    pre=i
    
print(cnt)