import heapq

def solution(n, k, enemy):
    answer = k
    if k >= len(enemy):
        return len(enemy)
    
    stk = enemy[:k]
    heapq.heapify(stk)
    
    while True:
        if answer >= len(enemy):
            break
        heapq.heappush(stk, enemy[answer])
        n -= heapq.heappop(stk)
        if n < 0:
            break
        answer += 1
    
    return answer