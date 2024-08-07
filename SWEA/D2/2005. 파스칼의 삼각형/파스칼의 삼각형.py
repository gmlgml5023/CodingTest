triangle = [[1] * line for line in range(1, 11)]

for i in range(2, 10):
    for j in range(i - 1):
        triangle[i][j + 1] = triangle[i - 1][j] + triangle[i - 1][j + 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    result = triangle[:N]
    for t in result:
        print(*t)