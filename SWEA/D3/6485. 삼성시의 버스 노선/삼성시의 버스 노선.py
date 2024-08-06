T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line_list = []
    for i in range(N):
        line_list.append(list(map(int, input().split())))  # [A, B]

    P = int(input())
    cnt_list = [0] * P
    for j in range(P):
        C = int(input())
        cnt = 0
        for line in line_list:
            if line[0] <= C <= line[1]:
                cnt += 1
        cnt_list[j] = cnt

    print(f'#{tc}', *cnt_list)
