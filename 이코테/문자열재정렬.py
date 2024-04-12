S=input()

a=[]
b=[]

for i in S:
    if i.isdigit():
        b.append(int(i))
    else:
        a.append(i)

a.sort()
a.append(sum(b))
for i in a:
    print(i, end="")