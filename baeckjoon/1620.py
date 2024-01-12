import sys

a,b=map(int, sys.stdin.readline().split())
arr=[]

for i in range(a):
    arr.append(sys.stdin.readline().strip('\n'))

for j in range(b):
    m=sys.stdin.readline().strip('\n')
    if m.isalpha():
        print((arr.index(m))+1)
    elif m.isdigit():
        m=int(m)
        print(arr[m-1])