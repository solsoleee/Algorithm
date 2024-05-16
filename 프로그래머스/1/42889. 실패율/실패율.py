def solution(N, stages):
    answer = []
    
    stage_count = [0]*(N+2)
    
    for s in stages:
        stage_count[s]+=1 #도달한 플레이어 하지만 클리어를 하지 못한
    
    reached = len(stages)
    
    for i in range(1, N+1):
        if reached == 0:
            fail=0
        else:
            fail=stage_count[i]/reached
        answer.append((i, fail))
        reached-=stage_count[i]
    answer.sort(key=lambda x:(-x[1],x[0]))
    res=[answer[i][0] for i in range(N)]
    print(res)
    return res