'''
1. 배열의 끝이나, D가 나와야만 멈출 수 있다.
 - 배열의 가장자리를 D로 감싸기?
2. 가는 길에 G가 있어도 멈출 수 없다.
3. 델타탐색을 해서
 - 자기 자신이 아니고, visited 배열에 없으면, 이동
4. 큐에 하나씩 넣으면서 길을 찾고, 길에서 갈 수 있는 노드들을 계속 삽입
5. 다시 하나씩 빼고, 뺀 코드가 G라면 종료

'''
from pprint import pprint
from collections import deque


def solution(arr):
    arr = [list(a) for a in arr]

    # 시작점, 목표지점 찾기
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                start_i, start_j = i, j
            elif arr[i][j] == 'G':
                goal_i, goal_j = i, j

    # BFS 탐색
    queue = deque([(start_i, start_j, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[start_i][start_j] = 1

    while queue:
        i, j, moves = queue.popleft()

        if (i, j) == (goal_i, goal_j):
            return moves
        
        # 델타탐색
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i, j

            while 0 <= ni+di < n and 0 <= nj + dj < m and arr[ni+di][nj+dj] != 'D':
                ni += di
                nj += dj
        
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj, moves+1))

    return -1
