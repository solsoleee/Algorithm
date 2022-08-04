# n=input()
# if(n=="12" or "1" or "2"):
#     print("winter")
# elif(n=="3" or "4" or "5"):
#     print("spring")
# elif(n==6 or 7 or 8):
#     print("summer")
# else:
#     print("fall")
    
a=int(input())
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")