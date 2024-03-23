from collections import Counter

name=input()
def solution(name):
    name_dic=Counter(name)

    mid=''
    cnt=0 #홀수의 개수
    result=''
    #가운데 정함
    for k,v in name_dic.items():
        if v%2!=0: #홀수이면
            mid=k
            cnt+=1
        if cnt >=2:
            return "I'm Sorry Hansoo"

    for k, v in sorted(name_dic.items()):
        result+=k*(v//2)

    return (result+mid+result[::-1])

print(solution(name))