from collections import deque

def solution(x, y, n):
    answer = -1
    
    visited = [0]* (y+1)
    
    queue = deque()
    queue.append(x)
    
    visited[x] = 1
    
    while queue :
        cur = queue.popleft()
        
        if cur == y :
            answer = visited[cur] -1
            break
        
        for nxt in (cur+n, cur*2, cur*3):
            if 0 <= nxt < (y+1) and not visited[nxt]:
                visited[nxt] = visited[cur] + 1
                queue.append(nxt)
                
    
    return answer