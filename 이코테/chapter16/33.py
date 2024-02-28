n=int(input())

t=[]
p=[]

for i in range(1,n+1):
    a,b=map(int, input().split())
    t.append(a)
    p.append(b)

d=[0]*16

max_value=0

for i in range(n-1, -1, -1):
    time=t[i]+i #현재 상담을 마친 일자의 이윤
    if t[i]+i<=n: #회사에 있는 경우 
        d[i]=max(d[time]+p[i],max_value) #현재 시간+지금까지 이윤, 현재 큰값     
    else:
        d[i], max_value