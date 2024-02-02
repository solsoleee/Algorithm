def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i, value in enumerate(arr):
        s=s.replace(value, str(i))
               
    return int(s)