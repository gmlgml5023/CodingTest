def solution(n, m, section):
    answer = 0
    current_position = 0  # 현재 페인트칠이 끝난 지점
    
    for start in section:
        if start > current_position:  # 페인트칠이 필요한 구역에 도달한 경우
            answer += 1
            current_position = start + m - 1  # 롤러 길이만큼 칠한 후, 끝나는 위치 갱신
            
    return answer
