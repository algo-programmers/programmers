from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    answer = -1
    
    visited = [[0]*m for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    
    visited[0][0] = 1
    
    while q :
        a,b = q.popleft()
        
        if a == n-1 and b == m-1 :
            answer = visited[a][b]
            q.clear()
            break
        
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]] :
            ni,nj = a+di, b+dj
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj]:
                    
                    if maps[ni][nj] == 1 :
                        visited[ni][nj] = visited[a][b]+1
                        q.append((ni,nj))
    
    return answer