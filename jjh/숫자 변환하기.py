from collections import deque

def solution(x, y, n):
    answer = 0
    
    dp = [1e9] * (y+1)
    q = deque()
    q.append((x, 0))
    dp[x] = 0
    
    while q:
        now, dist = q.popleft()
        for nxt in (now+n, now*2, now*3):
            if nxt < y+1 and (dp[nxt] == 1e9 or dist+1 < dp[nxt]):
                q.append([nxt, dist+1])
                dp[nxt] = dist+1
    
    if dp[y] == 1e9:
        return -1
    return dp[y]