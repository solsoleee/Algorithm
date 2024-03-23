def solution(arr):
    answer=0
    stack=[]
    pre=0
    for i in arr:
        if i == "(":
            stack.append(i)
        elif i ==")" and pre=="(": #지금 나오는 문자가 )이면서 이전 문자가 (이라면 레이저
            stack.pop()
            answer+=len(stack)
        elif i==")": #막대기 끝
            stack.pop()
            answer+=1
        pre=i
    
    return answer

if __name__ == "__main__":
    arr=input()
    print(solution(arr))