T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    total = 0
    for i in range(N):
        if i <= N//2:
            for j in range(N//2-i, N//2+i+1):
                total += arr[i][j]
        else:
            for j in range(N//2-(N-i-1), N//2+(N-i-1)+1):
                total += arr[i][j]
    print(f'#{tc} {total}')
