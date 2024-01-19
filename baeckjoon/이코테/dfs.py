def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    if graph[x][y] == 0: #현재 노드를 아직 방문하지 않았다면
        graph[x][y] = 1 # 방문처리
        dfs(x-1, y) #상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x,y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

N,M=map(int,input().split())
graph=[]      
for i in range(N+1):
    graph.append(list(map(int, input())))

#모든 노드(위치)에 대하여 음료수 채우기
result=0
for j in range(N):
    for k in range(M):
        if dfs(j,k) == True:
            result+=1
            
print(result)