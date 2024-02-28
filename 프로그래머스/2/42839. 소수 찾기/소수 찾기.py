from itertools import permutations
import math
def solution(numbers):
    
    def check(n): #소수 확인 함수
        if n==0 or n==1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False #소수가 아님
        return True
    
    arr=[]
    for i in range(1, len(numbers)+1):
        for n in permutations(numbers, i):
            arr.append(int(''.join(n)))
    
    arr=list(set(arr))
    answer = 0
    for j in arr:
        if check(j):
            answer+=1
            print(j)
        else:
            continue
    
    return answer