def solution(maps):
    n, m = len(maps), len(maps[0])
    
    queue = [(0, 0)]
    
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    maps[0][0] = 1
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    maps[nx][ny] = maps[x][y] + 1
    if visited[n-1][m-1] != 0:
        return maps[n-1][m-1]
    else:
        return -1