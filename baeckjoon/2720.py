# T = int(input())
# case=[]
# for i in range(T):    
#     Quarter, Dime, Nickel, Penny, Quarter_1,Dime_1,Nickel_1 =0,0,0,0,0,0,0
#     change = int(input())
#     Quarter = int(change/25)
#     Quarter_1 = (change%25)
#     Dime = int(Quarter_1/10)
#     Dime_1 = Quarter_1%10
#     Nickel = int(Dime_1/5)
#     Nickel_1 = Dime_1%5
#     Penny = int(Nickel_1/1)
#     case.append(Quarter)
#     case.append(Dime)
#     case.append(Nickel)
#     case.append(Penny)


# for i in range(0, len(case), 4):
#     print(case[i:i+4])


n = int(input())

for _ in range(n):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i
    
        