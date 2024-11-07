def solution(name):
    # 알파벳 변경에 필요한 최소 조작 횟수 계산
    move_count = sum(min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name)
    
    # 커서 이동 최소화
    n = len(name)
    min_move = n - 1  # 기본적으로 오른쪽 끝까지 이동하는 경우
    for i in range(n):
        # 다음에 나오는 비 'A' 문자의 위치를 찾습니다.
        next_index = i + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        # 현재 위치에서 왔다 갔다 하는 최소 이동 계산
        min_move = min(min_move, i + i + n - next_index, 2 * (n - next_index) + i)
    
    # 알파벳 변경 횟수와 커서 이동 최소 횟수 합산
    return move_count + min_move

# 예시 실행
print(solution('JAZ'))  # 결과: 11
