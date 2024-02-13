def solution(N, stages):
    answer=[]
    #스테이지에 도달한 수 전체
    #스테이지에 도달하지 못한 수 (그 스테이지에 멈춘 수)
    length=len(stages)
    for i in range(1,N+1):
        #1번 스테이지 실패율
        s=stages.count(i) #스테이지에 멈춤 
        if length==0:
            res=0
        else:
            res=s/length
        answer.append((i, res))
        length-=s
    answer.sort(key=lambda x:(x[1]), reverse=True)
    answer=[i[0] for i in answer]
    return answer