T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_bomb = 0
    for row in range(N):  # 행 순회
        for col in range(M):  # 열 순회
            bomb = arr[row][col]  # 꽃가루 개수를 더할 bomb 변수에 가운데 값 할당
            for i in range(1, bomb+1):
                if col - i >= 0:  # 왼쪽
                    bomb += arr[row][col-i]
                if col + i < M:  # 오른쪽
                    bomb += arr[row][col+i]
                if row - i >= 0:  # 위쪽
                    bomb += arr[row-i][col]
                if row + i < N:  # 아래쪽
                    bomb += arr[row+i][col]
                # 최댓값 갱신
                if max_bomb < bomb : max_bomb = bomb
    print(f'#{tc} {max_bomb}')