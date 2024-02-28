command=list(input())
command[0]=ord(command[0])-97

# 수평, 수직
dx=[2,-2,-2,2,1,-1,1,-1]
dy=[1,-1,1,-1,2,-2,-2,2]
cnt=0

x=command[0]
y=int(command[1])-1

for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx>=0 and nx<8 and ny>=0 and ny<8:
        cnt+=1
print(cnt)

