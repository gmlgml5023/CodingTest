for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    view = 0
    # 양 끝 높이가 0인 빌딩 제외 순회
    for i in range(2, N-2):
        # 타겟 빌딩의 왼쪽 두개 빌딩 중 높은 빌딩의 높이
        if buildings[i-2] > buildings[i-1] : left_high = buildings[i-2]
        else : left_high = buildings[i-1]

        # 타겟 빌딩의 오른쪽 두개 빌딩 중 높은 빌딩의 높이
        if buildings[i+2] > buildings[i+1] : right_high = buildings[i+2]
        else : right_high = buildings[i+1]

        # 왼쪽 뷰와 오른쪽 뷰 계산
        left_view = buildings[i] - left_high
        right_view = buildings[i] - right_high

        # 왼쪽 뷰와 오른쪽 뷰의 공통분모 (더 작은거) 찾기
        if left_view < right_view : result_view = left_view
        else : result_view = right_view

        # 양수만 최종 합산
        if result_view > 0:
            view += result_view

    print(f'#{tc} {view}')
        