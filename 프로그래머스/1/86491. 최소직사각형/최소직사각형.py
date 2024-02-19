def solution(sizes):
    n=len(sizes)
    m=2
    
    for i in range(n):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    max_value=0
    for j in range(n):
        max_value=max(sizes[j][1], max_value)

    
    
    answer = max(sizes)[0]*max_value
    return answer