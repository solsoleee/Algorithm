def solution(s):
    answer=[]
    
    if len(s)==1:
        return 1
    
    for i in range(1, len(s)+1): #i만큼 자름
        b=''
        cnt=1
        tmp=s[:i] #몇으로 문자열 압축

        for j in range(i, len(s)+i, i):
            
            if tmp == s[j:i+j]: #이전과 같은 경우
                cnt+=1
            else: #이전이랑 같지 않음 
                if cnt!=1: #cnt2이상 압축해야 하는 경우
                    b=b+str(cnt)+tmp
                else: #cnt가 1인경우 같지 않을 때 그냥 더함
                    b=b+tmp
                tmp=s[j:j+i]
                cnt = 1
        answer.append(len(b))

    return min(answer)
