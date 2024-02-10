s=input()

d=[]
a=[]
result=''
for i in s:
    if i.isdigit():
        d.append(int(i))
    else:
        a.append(i)

a.sort()
for i in a:
    result+=i

result+=str(sum(d))

print(result)