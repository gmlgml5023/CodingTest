T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = input()
    sorted_cards = sorted(list(set(cards)), reverse=True)
    card_count = [cards.count(card) for card in sorted_cards]

    top_card = int(sorted_cards[card_count.index(max(card_count))])

    print(f'#{test_case} {top_card} {max(card_count)}')