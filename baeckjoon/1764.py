import sys

n,m=map(int, sys.stdin.readline().split())
n_list=[]
m_list=[]

for i in range(n):
    n_list.append(sys.stdin.readline().rstrip())
for j in range(m):
    m_list.append(sys.stdin.readline().rstrip())

result=0
arr=[]

for i in n_list:
    if i in m_list:
        result+=1
        arr.append(i)

arr.sort()
print(len(arr))
for i in arr:
    print(i)