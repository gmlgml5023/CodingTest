def where_word(arr):
    possible = 0
    for i in range(N):
        blank = 0
        for j in range(N):
            if arr[i][j] == 1:
                blank += 1
            else:
                if blank == K:  # 빈칸이 단어의 길이와 같으면
                    possible += 1  # 들어갈 수 있는 곳 +1
                blank = 0  # 0으로 초기화
        if blank == K:  # 단어의 길이와 같으면
            possible += 1  # 들어갈 수 있는 곳 +1
    return possible


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle_t = list(map(list, zip(*puzzle)))
    ans = where_word(puzzle) + where_word(puzzle_t)
    print(f'#{tc} {ans}')
