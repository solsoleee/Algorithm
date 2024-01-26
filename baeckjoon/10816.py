n=int(input())
n_list=list(map(int, input().split()))

d=[0]*(500000)

for i in n_list:
    d[i]+=1

m=int(input())
m_list=map(int, input().split())

for j in m_list:
    print(d[j], end=' ')
