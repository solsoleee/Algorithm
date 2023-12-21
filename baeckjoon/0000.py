n,k=map(int,input().split())

count=0

# if(n%k==0):
#         n=n//k
#         print(n)
#         count=+1


while(True):
    if(n%k==0):
        n=n//k
        count=count+1
        if(n==1):
            break
    else:
        n=n-1
        count=count+1
        if(n==1):
            break       

print(count)
