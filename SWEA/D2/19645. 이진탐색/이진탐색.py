def book_binarySearch(book_page, target):
    """
    이진 탐색을 통해 타겟 페이지를 찾는 데 필요한 시도 횟수를 반환하는 함수

    Parameters:
    - book_page: 책의 전체 페이지 수
    - target: 찾아야 하는 페이지

    Returns:
    - cnt : 목표 페이지를 찾을 때까지 이진 탐색을 시행한 횟수
    """
    left, right = 1, book_page  # 탐색 범위의 초기 왼쪽과 오른쪽 설정
    cnt = 0  # 탐색 횟수를 세기 위한 변수

    while left <= right:  # 탐색 범위가 유효할 동안 반복
        cnt += 1  # 탐색 단계 수 증가
        center = (left + right) // 2  # 센터 페이지 계산
        if center < target:  # 센터보다 타겟페이지가 뒤에 있을 경우
            left = center  # 왼쪽 경계를 중간페이지 바로 뒷장으로 업데이트 (타겟 기준 왼쪽 부분 버림)
        elif center > target:  # 센터보다 타겟페이지가 앞에 있을 경우
            right = center  # 왼쪽 경계를 중간페이지 바로 앞장으로 업데이트 (타겟 기준 오른쪽 부분 버림)
        else:  # 목표 페이지를 찾은 경우
            return cnt  # 바로 횟수 return
    return cnt

# 테스트케이스 수 입력
T = int(input())

for tc in range(1, T+1):  # 테스트케이스 수만큼 반복
    page, A_target, B_target = map(int, input().split())

    # A와 B의 탐색 횟수 계산
    A_cnt = book_binarySearch(page, A_target)
    B_cnt = book_binarySearch(page, B_target)

    if A_cnt < B_cnt:
        print(f'#{tc} A')
    elif B_cnt < A_cnt:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')