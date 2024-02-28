def solution(answers):
    answer1=[1,2,3,4,5]*2001
    answer2=[2,1,2,3,2,4,2,5]*2001
    answer3=[3,3,1,1,2,2,4,4,5,5]*2001
    cnt1, cnt2, cnt3=0,0,0
    
    
    for i in range(len(answers)):
        if answer1[i]==answers[i]:
            cnt1+=1
        if answer2[i]==answers[i]:
            cnt2+=1
        if answer3[i]==answers[i]:
            cnt3+=1
    print(cnt1, cnt2, cnt3)
    max_value=max(cnt1, cnt2, cnt3)
    answer = []
    if max_value==cnt1:
        answer.append(1)
    if max_value==cnt2:
        answer.append(2)
    if max_value==cnt3:
        answer.append(3)
            
    return answer