from collections import Counter

word=input()
check_word=Counter(word)

cnt=0
result=''
mid=''

for k, v in list(check_word.items()):
    if v % 2 == 1: #홀수라면
        cnt += 1
        mid = k #중간에 들어갈 값으로 저장
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()
for k,v in sorted(check_word.items()): #정렬
    result += (k *(v//2)) #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수에서 2로 나눠줌

print(result + mid + result[::-1])