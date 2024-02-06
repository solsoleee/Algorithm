def solution(N, stages):
    answer=[]
    length=len(stages)
    for i in range(1, N+1):
        c=stages.count(i)
        if length==0:
            res=0
        else:
            res=c/length
        answer.append((i, res))
        length-=c
        #실패율=클리어하지못한플레이어수/스테이지 도달한 플레이어수
    answer.sort(key=lambda x: -x[1])
    answer=[i[0] for i in answer]
    return answer


