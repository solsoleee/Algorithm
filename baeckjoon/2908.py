a,b=input().split()

a=list(str(a))
a.reverse() 
a=''.join(a)
b=list(str(b))
b.reverse()
b=''.join(b)
if(int(a)>int(b)):
    print(a)
else:
    print(b)
