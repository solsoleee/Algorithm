n,m,v=map(int,input().split())

graph=[]

for i in range(m):
    a,b=map(int,input().split())
    graph.append([a,b])

print(graph)