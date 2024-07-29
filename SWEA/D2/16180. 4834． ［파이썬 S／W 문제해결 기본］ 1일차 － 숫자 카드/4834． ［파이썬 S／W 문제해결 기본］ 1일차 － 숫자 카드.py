T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = input()
    cards_cnt = {}
    for card in cards:
        if card in cards_cnt:
            cards_cnt[card] += 1
        else:
            cards_cnt[card] = 1

    max_num = max(cards_cnt, key = lambda x: (cards_cnt[x], x))
    max_num_cnt = cards_cnt[max_num]
    
    print(f'#{test_case} {max_num} {max_num_cnt}')