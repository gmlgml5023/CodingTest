T = int(input())
for tc in range(1, T+1):
    N = int(input())
    triangle = []
    for line in range(1, N+1):
        triangle.append([1]*line)

    for j in range(2, N):
        for k in range(j-1):
            triangle[j][k+1] = triangle[j-1][k] + triangle[j-1][k+1]

    print(f'#{tc}')
    for t in triangle:
        print(*t)
