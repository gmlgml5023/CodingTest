T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0 for _ in range(1, N+1)]
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for n in range(L, R+1):
            boxes[n-1] = i
    print(f'#{tc}', *boxes)
