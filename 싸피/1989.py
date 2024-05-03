T=int(input())

for t in range(1, T+1):
    word=input()
    reverse_word=word[::-1]
    if word==reverse_word:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')