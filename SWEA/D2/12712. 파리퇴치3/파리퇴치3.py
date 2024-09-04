T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    max_catch = 0
    for i in range(N):
        for j in range(N):
            catch = arr[i][j]
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ni, nj = i, j
                for k in range(M-1):
                    ni += di
                    nj += dj
                    if 0 <= ni < N and 0 <= nj < N:
                        catch += arr[ni][nj]
            if max_catch < catch:
                max_catch = catch

    for i in range(N):
        for j in range(N):
            catch = arr[i][j]
            for di, dj in [[-1, 1], [1, 1], [1, -1], [-1, -1]]:
                ni, nj = i, j
                for k in range(M-1):
                    ni += di
                    nj += dj
                    if 0 <= ni < N and 0 <= nj < N:
                        catch += arr[ni][nj]
            if max_catch < catch:
                max_catch = catch

    print(f'#{tc} {max_catch}')