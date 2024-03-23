def solution(stick):
    stack=[]
    cnt=0
    pre='' #이전
    for s in stick:
        if s=="(":
            stack.append(s)
        else:
            if pre=="(":
                stack.pop()
                cnt+=len(stack)
            else:
                stack.pop()
                cnt+=1
        pre=s
    return cnt

print(solution(input()))