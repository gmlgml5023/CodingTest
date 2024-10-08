T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for i in range(N):
        for j in range(M):
            total = balloons[i][j]
            for di, dj in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                ni, nj = i, j
                for _ in range(balloons[i][j]):
                    ni += di
                    nj += dj
                    if 0 <= ni < N and 0 <= nj < M:
                        total += balloons[ni][nj]
            if max_total < total:
                max_total = total
    print(f'#{tc} {max_total}')
    
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     balloons = [list(map(int, input().split())) for _ in range(N)]
# 
#     max_total = 0
#     di = [0, 0, -1, 1]
#     dj = [-1, 1, 0, 0]
# 
#     for i in range(N):
#         for j in range(M):
#             total = balloons[i][j]
#             for d in range(4):
#                 for k in range(1, balloons[i][j]+1):
#                     ni = i + di[d] * k
#                     nj = j + dj[d] * k
#                     if 0 <= ni < N and 0 <= nj < M:
#                         total += balloons[ni][nj]
# 
#             if max_total < total:
#                 max_total = total
#     print(f'#{tc} {max_total}')
