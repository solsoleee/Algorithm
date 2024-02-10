# 문자열을 1부터 len(s)까지 잘라서 문자열 압축을 한다
# 문자열을 잘라서 반복되는 수를 반복되는 것 앞에 쓴다
# 반복되지 않는경우는 세어주지 않는다
# 그 만들어진 결과가 작은것을 출력한다

def solution(s):
    
    answer=len(s)
    for step in range(1,len(s)//2+1): #문자를 자르는 숫자
        result=''
        prev=s[0:step]
        count=1
        #그리고 prev랑 뒤랑 똑같은지 확인해야함
        for j in range(step, len(s), step):
            if prev==s[j:j+step]:
                count+=1
            else:
                result+=str(count)+prev if count>=2 else prev
                count=1
                prev=s[j:j+step]
        result+=str(count)+prev if count>=2 else prev
        print(result)
        answer=min(answer, len(result))
                    
    return answer

solution('aabbb')