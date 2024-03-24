def solution(s):
    answer = []
    cnt=1
    for i in range(1, len(s)+1): #i개씩 자름
        result='' #문자열 저장
        tmp=s[:i] #이전 문자열
        for j in range(i, len(s)+i, i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1: #문자열이 같을 때 (압축해야함)
                    result=result+str(cnt)+tmp
                else: #압축 안될 때 그냥 더함
                    result=result+tmp
                tmp=s[j:i+j]
                cnt=1
        answer.append(len(result))
    return min(answer)