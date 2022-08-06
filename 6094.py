n=int(input())
a = input().split() 

for i in range(n) : 
  a[i] = int(a[i])

min=0

for i in range(n-1) : 
  if a[i]<a[i+1]:
      min=a[i]
print(min)