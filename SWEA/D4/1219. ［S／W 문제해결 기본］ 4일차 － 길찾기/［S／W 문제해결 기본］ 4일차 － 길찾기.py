# dfs 함수
def dfs(start_node):         # start_node : 탐색을 시작할 노드
    stack = [start_node]     # 스택에 처음 시작 노드 push
    visited = [0] * 100      # 방문 여부 기록할 리스트
    visited[start_node] = 1  # 시작 노드를 방문 처리

    # 스택이 비어있지 않은 동안 반복
    while stack:
        current_node = stack.pop()  # 스택에서 노드를 꺼내서 현재 노드로 설정 (시작 노드)
        if current_node == 99:      # 탐색할 목적지인 99면
            return 1                # 1을 return하고 함수 종료

        # 현재 노드와 인접한 모든 노드들을 탐색
        for neighbor in adjL[current_node]:
            if visited[neighbor] == 0:  # 아직 방문하지 않은 노드면
                stack.append(neighbor)  # 스택에 push (탐색할 준비)
                visited[neighbor] = 1   # 방문 처리
    # 목적 노드 99에 도착하지 못한 경우 0 반환
    return 0


for _ in range(1, 11):
    tc, N = map(int, input().split())  # 테케 수와 길의 수
    arr = list(map(int, input().split()))  # 간선 정보

    adjL = [[] for _ in range(100)]  # 인접 리스트 (100개의 노드를 위한 빈 리스트)
    for i in range(N):
        start, end = arr[2*i], arr[2*i+1]
        adjL[start].append(end)

    visited = [0] * 100

    # DFS 호출 및 결과 저장
    result = dfs(0)

    # 결과 출력
    print(f'#{tc} {result}')