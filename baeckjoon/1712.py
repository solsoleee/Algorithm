a,b,c=map(int,(input().split()))
if(b>=c):
    print(-1)
else:
    point=-a/(b-c)
    point+=1
    print(int(point))