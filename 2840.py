
n,k = map(int, input().split())
cycle=['?']*n
word=[]
for i in range(k):
    word.append(input().split())

def solution(cycle, word):
    n=len(cycle)
    for w in word:
        s=int(w[0])%n
        a=w[1]
        cycle=cycle[-s:]+cycle[:-s]
        
        if cycle[0]=='?': #채워넣을차례
            if a in cycle:
                return "!"
            else:
                cycle[0]=a
        else:
            if cycle[0]==a:
                continue
            else: #이미 자리가 있는 경우
                return "!"

    answer=cycle
    return "".join(answer)

print(solution(cycle, word))