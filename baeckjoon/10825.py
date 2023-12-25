N=int(input())
student=[]

for i in range(N):
    a,b,c,d=input().split()
    b,c,d=int(b),int(c),int(d)
    student.append((a,b,c,d))

student.sort(key=lambda x:(-x[1], x[2],-x[3], x[0]))

for j in student:
    print(j[0])