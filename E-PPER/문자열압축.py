def solution(s):
    answer=[]

    if len(s)==1:
        return 1
    
    for i in range(1, len(s)+1):
        tmp=s[:i]
        result=''
        cnt=1
        for j in range(i, len(s)+i, i):
            #이전거랑 같다면
            if tmp==s[j:j+i]:
                cnt+=1
            else: #이전이랑 같이 않을 때
                if cnt>=2: #문자열 압축
                    result+=str(cnt)+tmp
                else: #이전거랑 같지도 않고 압축도 안됨
                    result+=tmp
                tmp=s[j:j+i] #이전거로
                cnt=1
        answer.append(len(result))
                    
            
    return min(answer)

print(solution("abcabcabcabcdededededede"))
