
from collections import Counter



def solution(name):
    answer=0
    
    name_dic=Counter(name)
    cnt = 0 # 홀수의 갯수
    result='' # 결과
    mid='' #가운데 홀수
    
    for k, v in (name_dic.items()):
        print(k,v)
        if v%2==1: #홀수라면
            cnt+=1
            mid=k
            if cnt>1:
                return "I'm Sorry Hansoo"
            
    for k, v in sorted(name_dic.items()):
        result+=(k*(v//2))
    
    return result + mid + result[::-1]
    

name=input()
print(solution(name))