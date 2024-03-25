
from collections import Counter

def solution(name):
    
    name_dic=Counter(name)

    cnt=0
    mid=''
    result=''
    
    for k,v in name_dic.items():
        if v%2!=0:
            cnt+=1
            mid=k
        if cnt>=2:
            return "I'm Sorry Hansoo"

    for k, v in sorted(name_dic.items()):
        result+=k*(v//2)
    
    return result + mid + result[::-1]


name=input()
print(solution(name))