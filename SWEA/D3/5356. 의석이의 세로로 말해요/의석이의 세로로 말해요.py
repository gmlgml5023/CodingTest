T = int(input())
for tc in range(1, T + 1): # 테스트케이스 수만큼 순회
    arr = [list(input()) for _ in range(5)] # 문자열 입력 받아서 2차원 배열을 만들어줌
    # 가장 긴 문자열의 길이 구하기
    max_len = 0 
    for i in range(len(arr)):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    # 정답 문자열 만들 변수 선언
    result = ''
    for x in range(max_len):  # 가장 긴 문자열의 길이만큼 순회
        for y in range(5):  # 문자열의 개수 5만큼 순회
            # 특이케이스 처리
            # 1) 문자열의 길이가 최대 길이 문자열보다 짧고,
            # 2) 문자의 x좌표가 이번 문자열의 길이보다 크거나 같으면,
            if (len(arr[y]) < max_len) and (x >= len(arr[y])):
                continue
            else:
                result += arr[y][x] # 열 방향으로 result에 누적
    print(f'#{tc} {result}')