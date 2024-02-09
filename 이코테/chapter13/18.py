
#u와 v로 분리하는 과정
def balance_index(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        else:    
            count-=1
        if count==0:
            return i

#올바른 괄호 문자열인지 확인
def balance(p):
    stack=[]
    for i in p:
        if i=='(':
            stack.append(i)
        elif i==')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True

#최종
def solution(p):
    answer=''
    if balance(p):
        return p
    index=balance_index(p)
    u=p[:index+1]
    v=p[index+1:]
    if balance(u):
        answer=u+solution(v)
        return answer
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        u=list(u[1:-1])
        for i in range(len(u)):
            print(u[i])
            if u[i] =='(':
                u[i]=')'
            else:
                u[i]='('
        answer+="".join(u)
    return answer

print(solution('))))(((('))
