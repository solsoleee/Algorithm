while(True):
    a=int(input())
    
    if a==-1:
        break
    
    factor=[]
    factor.clear()
    sum=0
    
    for i in range(1, a):
        if a % i ==0:
            factor.append(i)
  
    for j in range (0,len(factor)):
        sum = sum + int(factor[j])
    
    if a==sum:
        print(a, "=", end=" ")
        for k in range (len(factor)):
            if k==len(factor)-1:
                print(factor[k])
            else:
                print(factor[k], "+" , end=" ")
    else:
        print(a, "is NOT perfect.")