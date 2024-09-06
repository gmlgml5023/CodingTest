T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_room = 0
    start = N*N+1

    for i in range(N):
        for j in range(N):
            room = 1
            cur_i, cur_j = i, j
            while True:
                moved = False
                for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 좌 우 상 하
                    ni, nj = cur_i, cur_j
                    ni += di
                    nj += dj

                    if 0 <= ni < N and 0 <= nj < N and arr[cur_i][cur_j] + 1 == arr[ni][nj]:
                        cur_i, cur_j = ni, nj
                        room += 1
                        moved = True
                        break
                if not moved:
                    break

            if max_room < room:
                max_room = room
                start = arr[i][j]
            elif room == max_room and arr[i][j] < start:
                start = arr[i][j]

    print(f'#{tc} {start} {max_room}')