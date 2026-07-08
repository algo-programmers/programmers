# 1844번 bfs

from collections import deque

def bfs (x,y, mapss):
    n = len(mapss)
    m = len(mapss[0])
    visited = list([-1]*m for _ in range(n))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1
    queue = deque([(x,y)])
    
    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if nx == n-1 and ny == m-1:
                return visited[now_x][now_y]+1
            if 0<=nx<n and 0<=ny<m and mapss[nx][ny]==1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[now_x][now_y] + 1
                queue.append((nx, ny))
            
    return -1
            

def solution(maps):
    l = len(maps)
    answer = bfs(0, 0, maps)
    
    return answer