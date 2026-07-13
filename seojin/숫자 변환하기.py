from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = [-1] * 1000001
    visited[x] = 0
    
    while queue :
        cur, cnt = queue.popleft()
        
        for nxt in [cur+n, cur*2, cur*3]:
            if nxt<=y and visited[nxt] == -1:
                visited[nxt]=visited[cur]+1
                queue.append((nxt, cnt+1))
            
    
    answer = visited[y]
    return answer