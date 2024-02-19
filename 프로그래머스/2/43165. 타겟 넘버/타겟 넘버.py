def solution(numbers, target):
    
    res=[0] # 모든계산결과
    answer = 0 # 개수
    
    for num in numbers:
        temp=[]
        
        for i in res:        
            temp.append(i+num) #현재 계산 결과
            temp.append(i-num)
        
        res=temp
    for r in res:
        if r==target:
            answer+=1
    
    return answer