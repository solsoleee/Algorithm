n=int(input())
data_list=[]
for i in range(n):
    a,b=map(int,input().split())
    data_list.append((a,b))
for i in range(n):
    rank=1
    for j in range(n):
        if(data_list[i][0]<data_list[j][0] and data_list[i][1]<data_list[j][1]):
            rank+=1
    print(rank,end=' ')