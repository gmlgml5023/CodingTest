T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    possible = 0
    for i in range(N):
        # 행 검사
        row = 0
        for j in range(N):
            if puzzle[i][j] == 1:  # 행 우선 순회하며 1이면 빈칸수 +1
                row += 1
            else:                  # 중간에 막힌 경우
                if row == K:     # 빈칸이 단어의 길이와 같으면
                    possible += 1  # 들어갈 수 있는 곳 +1
                row = 0          # 0으로 초기화
        if row == K:             # 단어의 길이와 같으면
            possible += 1          # 들어갈 수 있는 곳 +1

        # 열 검사
        col = 0
        for j in range(N):
            if puzzle[j][i] == 1:  # 열 우선 순회하며 1이면 빈칸수 +1
                col += 1
            else:                  # 중간에 막힌 경우
                if col == K:     # 빈칸이 단어의 길이와 같으면
                    possible += 1  # 들어갈 수 있는 곳 +1
                col = 0          # 0으로 초기화
        if col == K:             # 단어의 길이와 같으면
            possible += 1          # 들어갈 수 있는 곳 +1

    print(f'#{tc} {possible}')