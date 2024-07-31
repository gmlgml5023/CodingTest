for tc in range(1, 11):
    input()

    num_list = [list(map(int, input().split())) for _ in range(100)]

    N = len(num_list)

    max_sum = 0

    sum_dia_1 = 0
    sum_dia_2 = 0

    for row in range(N):
        # 1개의 행 별 합을 구하기 위한 변수 선언
        sum_row = 0
        sum_col = 0
        for col in range(N):
            # 1개의 행의 합을 구한 후 max_sum보다 클 경우 업데이트
            sum_row += num_list[row][col]
            if max_sum < sum_row : max_sum = sum_row

            # 1개의 열의 합을 구한 후 max_sum보다 클 경우 업데이트
            sum_col += num_list[col][row]
            if max_sum < sum_col : max_sum = sum_col

        # 두 대각성분의 합 계산
        sum_dia_1 += num_list[row][row]
        sum_dia_2 += num_list[row][N-1-row]

    # 두 대각성분의 합 중 큰 것 판별
    max_dia = sum_dia_2 if sum_dia_1 < sum_dia_2 else sum_dia_1

    # 결과 출력
    print(f'#{tc} {max_dia if max_dia >= max_sum else max_sum}')
    