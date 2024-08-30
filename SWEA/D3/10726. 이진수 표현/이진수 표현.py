T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} ON' if bin(M)[-N:] == '1'*N else f'#{tc} OFF')