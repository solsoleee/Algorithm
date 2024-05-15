def solution(p):
    
    def check1(arr): #올바른 문자열 확인
        stack=[]
        for a in arr:
            if a=='(':
                stack.append(a)
            else:
                if stack:
                    stack.pop()
                else:
                    return False #올바른게
        return not stack
    
    def check2(arr):
        cnt1=0
        cnt2=0
        for a in arr:
            if a=='(':
                cnt1+=1
            else:
                cnt2+=1
        return cnt1==cnt2
    
    def divide(arr): #u와v로분리해주는 함수
        u1=''
        v1=''
        for i in range(len(arr)):
            u1+=arr[i]
            if check2(u1):
                v1=arr[i+1:]
                break
        return u1, v1
    
    def process(p):
        if p=='':
            return ''
        answer = ''
        u, v = divide(p)
        if check1(u): #u가 올바른 문자열 이라면 1단계부터 실행
            answer=answer+u+process(v)
        else:
            answer=answer+'('
            answer=answer+process(v)
            answer=answer+')'
            u=u[1:len(u)-1]
            u_reverse=''
            for i in u:
                if i=='(':
                    u_reverse=u_reverse+')'
                else:
                    u_reverse=u_reverse+'('
            answer=answer+u_reverse
        return answer
    return process(p)