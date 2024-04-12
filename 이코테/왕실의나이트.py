

location=input()
a=int(ord(location[0]))-97
b=int(location[1])-1

dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]
cnt=0
for i in range(8):
    nx=b+dx[i]
    ny=a+dy[i]
    if 0<=nx<8 and 0<=ny<8:
        cnt+=1
        
print(cnt)