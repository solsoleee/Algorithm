#올바른 괄호 문자열인지 확인
def balance(p):
    count=0 #왼쪽 괄호의 개수
    for i in p:
        if i=='(':
            count+=1
        else: #)일때
            if count==0:
                return False
            count-=1
    return True

#u와 v로 분리하는 과정
def get_index(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return i

def solution(p):
    answer = ''
    if p=='':
        return answer
    
    index=get_index(p)
    
    u=p[:index+1]
    v=p[index+1:]
    
    if balance(u):
        answer=u+solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        u=u[1:-1]
        u=list(u)

        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
        answer+="".join(u) 
    return answer

solution(')(')