A,X = map(int, input().split())
# for i in range(0, A):
a = list(map(int, input().split()))
b=[]
for i in a:
    if i<X:
        b.append(i)

print(' '.join(str(x) for x  in b))
