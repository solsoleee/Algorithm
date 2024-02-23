def solution(sizes):
    
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    max_value=0
    for s in sizes:
        max_value=max(max_value, s[1])

    answer = max_value * max(sizes)[0]
    return answer