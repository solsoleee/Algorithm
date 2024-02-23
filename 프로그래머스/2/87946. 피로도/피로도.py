from itertools import permutations

def solution(k, dungeons):
    
    res=[]
    for x in permutations(dungeons, len(dungeons)):
        cnt=0
        a=k
        for i in x:
            if a>=(i[0]):
                a-=(i[1])
                cnt+=1
            else:
                continue
        res.append(cnt)

    answer = max(res)
    return answer