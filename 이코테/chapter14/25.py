# def solution(N, stages):
#     answer=[]
#     length=len(stages)
#     for i in range(1, N+1):
#         c=stages.count(i)
#         if length==0:
#             res=0
#         else:
#             res=c/length
#         answer.append((i, res))
#         length-=c
#         #실패율=클리어하지못한플레이어수/스테이지 도달한 플레이어수
#     answer.sort(key=lambda x: -x[1])
#     answer=[i[1] for i in answer]
#     return answer

# print(solution(4, [4,4,4,4,4]))



def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
        print(result)
    return sorted(result, key=lambda x : result[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))