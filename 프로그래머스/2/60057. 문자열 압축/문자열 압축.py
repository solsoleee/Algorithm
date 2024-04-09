def solution(s):
    if len(s)==1:
        return 1
    result=[]#문자열 압축 후 담을거
    for i in range(1, len(s)):
        cnt=1
        now=s[:i] #현재 자른 문자열
        res=''
        for j in range(i, len(s)+i, i): #i만큼 자름
            if now==s[j:i+j]:
                cnt+=1
            else:
                if cnt<=1: #전이랑 같지도 않다는거
                    res=res+now
                else:
                    res=res+str(cnt)+now
                cnt=1
            now=s[j:i+j]
        result.append(len(res))
    
    answer = min(result)
    return answer