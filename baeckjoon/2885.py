k=int(input())
cnt=0

for i in range(k):
    if 2**i >= k: #초콜릿을 사야할 최소 갯수
        cnt=i
        break
    
result=0

c=2**cnt #총 몇개이있는지

for i in range(k):
    if k%c==0: #초콜렛 잘라지면 멈춤
        break
    else:
        c//=2 #초콜렛 자름
        result+=1 #몇번 자를지

print(2**cnt, result)