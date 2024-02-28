def solution(n, lost, reserve):
    
    _lost=[i for i in lost if i not in reserve]
    _reserve=[k for k in reserve if k not in lost]
    
    answer = n - len(_lost)
    _lost.sort()
    _reserve.sort()
    
    for i in _lost:
        if i-1 in _reserve:
            answer+=1
            _reserve.remove(i-1)
        elif i+1 in _reserve:
            answer+=1
            _reserve.remove(i+1)
    
    
    return answer
