import math

def gcd_game(N, X, A):
    
    available_cards = [a for a in A if math.gcd(a, X) > 1]
    is_choos_turn = True

    while available_cards:
        if not any(math.gcd(a, X) > 1 for a in available_cards):
            break

        for card in available_cards:
            if math.gcd(card, X) > 1:
                X = math.gcd(card, X)  # 칠판 업데이트
                available_cards.remove(card)  # 선택한 카드 제거
                break
        is_choos_turn = not is_choos_turn

    # 승자 결정
    if is_choos_turn:
        return "Second"  # 철수의 턴에서 게임이 끝났다면 영희가 승자
    else:
        return "First"  # 영희의 턴에서 게임이 끝났다면 철수가 승자


N, X = map(int, input().split())
A = list(map(int, input().split()))

print(gcd_game(N, X, A))
