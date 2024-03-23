n,k = map(int, input().split())
command=[]
for i in range(k):
    command.append(list(input().split()))

def solution(command):
    wheel=['?']*n

    for s,a in command:
        s=int(s)%n
        wheel=wheel[-s:]+wheel[:-s]
        
        if a==wheel[0]:
            continue
        
        if wheel[0]=="?":
            if a in wheel: #이미 있으면
                return ("!")
                
            else:
                wheel[0]=a
        else: #겹치면
            return("!")
    return "".join(wheel)

print(solution(command))