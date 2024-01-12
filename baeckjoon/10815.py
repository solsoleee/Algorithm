n=int(input())
card=list(map(int,input().split()))
m=int(input())
card_list=list(map(int,input().split()))

for i in card_list:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')